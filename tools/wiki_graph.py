"""MkDocs-Hook: erzeugt beim Build eine graph.json aus den Markdown-Links
des Forschungsstand-Wikis (docs/wiki/). Eingebunden in mkdocs.yml unter
`hooks:`. Der Graph wird auf der Wiki-Startseite mit d3 gerendert.

Knoten:  alle Wiki-Seiten (ohne index.md) plus von dort verlinkte
         Website-Seiten. Schicht ergibt sich aus dem Pfad.
Kanten:  jeder relative Markdown-Link zwischen diesen Seiten.
"""
import json
import re
from pathlib import Path

LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)")


def _titel(pfad: Path) -> str:
    for zeile in pfad.read_text(encoding="utf-8").splitlines():
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
        knoten[r] = {"id": r, "label": _titel(f), "layer": _schicht(r), "url": _url(r)}

    for f in dateien:
        start = rel(f)
        for m in LINK_RE.finditer(f.read_text(encoding="utf-8")):
            ziel = (f.parent / m.group(1)).resolve()
            if not ziel.exists() or ziel.name == "index.md":
                continue
            try:
                zr = ziel.relative_to(docs).as_posix()
            except ValueError:
                continue
            if zr not in knoten:
                knoten[zr] = {"id": zr, "label": _titel(ziel), "layer": _schicht(zr), "url": _url(zr)}
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
