"""MkDocs-Hook: erzeugt beim Build eine graph.json aus den Markdown-Links
des Forschungsstand-Wikis (docs/wiki/). Eingebunden in mkdocs.yml unter
`hooks:`. Der Graph wird auf der Wiki-Startseite mit d3 gerendert.

Knoten:  alle Wiki-Seiten (ohne index.md) plus von dort verlinkte
         Website-Seiten. Schicht ergibt sich aus dem Pfad, Beschriftung und
         Zusatzangaben aus dem OKF-Frontmatter (siehe CLAUDE.md).
Kanten:  jeder relative Markdown-Link zwischen diesen Seiten. Gescannt wird
         nur der Fliesstext, nicht das Frontmatter, damit Pfadangaben in
         `sources:` keine Scheinkanten erzeugen.
"""
import json
import re
from pathlib import Path

from mkdocs.utils import meta

LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)")


def _lesen(pfad: Path) -> tuple[str, dict]:
    """Gibt (Fliesstext ohne Frontmatter, Frontmatter als dict) zurueck."""
    try:
        rumpf, kopf = meta.get_data(pfad.read_text(encoding="utf-8"))
    except Exception:
        return pfad.read_text(encoding="utf-8"), {}
    return rumpf, kopf or {}


def _titel(rumpf: str, kopf: dict, pfad: Path) -> str:
    if kopf.get("title"):
        return str(kopf["title"])
    for zeile in rumpf.splitlines():
        if zeile.startswith("# "):
            return zeile[2:].strip()
    return pfad.stem


def _url(rel: str) -> str:
    """Verzeichnis-URL relativ zur Wiki-Startseite (/wiki/)."""
    return "../" + rel[:-3] + "/"


def _schicht(rel: str) -> str:
    if rel.startswith("wiki/quellen/"):
        return "quelle"
    if rel.startswith("wiki/konzepte/"):
        return "konzept"
    if rel.startswith("wiki/synthese/"):
        return "synthese"
    return "seite"


def _knoten(pfad: Path, rel: str) -> dict:
    rumpf, kopf = _lesen(pfad)
    eintrag = {
        "id": rel,
        "label": _titel(rumpf, kopf, pfad),
        "layer": _schicht(rel),
        "url": _url(rel),
    }
    # Zusatzangaben nur setzen, wenn vorhanden: der Graph zeigt sie im Tooltip.
    if kopf.get("evidenzstufe"):
        eintrag["evidenzstufe"] = str(kopf["evidenzstufe"])
    if kopf.get("status") and kopf["status"] != "stable":
        eintrag["status"] = str(kopf["status"])
    return eintrag


def on_post_build(config, **kwargs):
    docs = Path(config["docs_dir"]).resolve()
    site = Path(config["site_dir"])
    wiki = docs / "wiki"

    def rel(p: Path) -> str:
        return p.resolve().relative_to(docs).as_posix()

    knoten: dict = {}
    kanten: set = set()

    dateien = [f for f in wiki.rglob("*.md") if f.name != "index.md"]
    for f in dateien:
        r = rel(f)
        knoten[r] = _knoten(f, r)

    for f in dateien:
        start = rel(f)
        rumpf, _ = _lesen(f)
        for m in LINK_RE.finditer(rumpf):
            ziel = (f.parent / m.group(1)).resolve()
            if not ziel.exists() or ziel.name == "index.md":
                continue
            try:
                zr = ziel.relative_to(docs).as_posix()
            except ValueError:
                continue
            if zr not in knoten:
                knoten[zr] = _knoten(ziel, zr)
            if start != zr:
                kanten.add((start, zr))

    ausgabe = site / "wiki" / "graph.json"
    ausgabe.parent.mkdir(parents=True, exist_ok=True)
    ausgabe.write_text(
        json.dumps(
            {
                "nodes": list(knoten.values()),
                "links": [{"source": s, "target": z} for s, z in sorted(kanten)],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
