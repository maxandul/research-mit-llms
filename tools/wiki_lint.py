"""Prueft das Forschungsstand-Wiki gegen die Regeln aus CLAUDE.md.

Aufruf aus dem Repository-Wurzelverzeichnis:

    python tools/wiki_lint.py

Geprueft wird, was sich aus dem OKF-Frontmatter maschinell ableiten laesst:
fehlendes oder unvollstaendiges Frontmatter, vorlaeufige Notizen (nur
Abstract geprueft), fehlende Verifikation, abgelaufene Pruefdaten,
ueberholte Notizen, verwaiste Notizen und tote interne Links.

Inhaltliche Aufgaben aus CLAUDE.md bleiben Handarbeit: Widersprueche
zwischen Konzepten markiert dieses Skript nicht.

Rueckgabewert: 0 wenn keine Befunde, sonst 1 (fuer CI verwendbar).
"""
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

from mkdocs.utils import meta

LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)")
PFLICHT_QUELLE = ("type", "title", "description", "resource", "evidenzstufe",
                  "verified", "stale_after")
PFLICHT_UEBRIGE = ("type", "title", "description")


def _lesen(pfad: Path):
    rumpf, kopf = meta.get_data(pfad.read_text(encoding="utf-8"))
    return rumpf, kopf or {}


def _trust_stufe(kopf: dict) -> str:
    """Vertrauensstufe nach OKF v0.2, abgeleitet aus `verified`."""
    verified = kopf.get("verified") or []
    if not verified:
        return "unverified"
    if any(str(v.get("by", "")).startswith("human:") for v in verified):
        return "human-reviewed"
    return "machine-confirmed"


def pruefen(wurzel: Path, heute: dt.date | None = None) -> list[str]:
    heute = heute or dt.date.today()
    wiki = (wurzel / "docs" / "wiki").resolve()
    befunde: list[str] = []
    eingehend: dict[str, int] = defaultdict(int)
    notizen: dict[str, dict] = {}

    for pfad in sorted(wiki.rglob("*.md")):
        if pfad.name == "index.md":
            continue
        rel = pfad.relative_to(wiki).as_posix()
        try:
            rumpf, kopf = _lesen(pfad)
        except Exception as fehler:
            befunde.append(f"{rel}: Frontmatter nicht lesbar ({fehler})")
            continue
        notizen[rel] = kopf

        if not kopf.get("type"):
            befunde.append(f"{rel}: kein Frontmatter mit `type` (nicht OKF-konform)")
            continue

        pflicht = PFLICHT_QUELLE if kopf["type"] == "Quellnotiz" else PFLICHT_UEBRIGE
        fehlend = [feld for feld in pflicht if not kopf.get(feld)]
        if fehlend:
            befunde.append(f"{rel}: Frontmatter unvollstaendig, fehlt: {', '.join(fehlend)}")

        if kopf["type"] == "Quellnotiz":
            stufe = _trust_stufe(kopf)
            if stufe == "unverified":
                befunde.append(f"{rel}: keine Verifikation hinterlegt")
            for eintrag in kopf.get("verified") or []:
                if "abstract" in str(eintrag.get("umfang", "")).lower():
                    befunde.append(
                        f"{rel}: Verifikation stuetzt sich ganz oder teilweise auf "
                        f"ein Abstract ({eintrag['umfang']}), Volltext nachruesten")

        faellig = kopf.get("stale_after")
        if isinstance(faellig, dt.date) and faellig < heute:
            befunde.append(f"{rel}: seit {faellig} faellig zur Nachpruefung")

        if kopf.get("status") == "deprecated":
            befunde.append(f"{rel}: als ueberholt markiert, Verweise pruefen")
        if kopf.get("status") == "draft":
            befunde.append(f"{rel}: als Entwurf markiert")

        for treffer in LINK_RE.finditer(rumpf):
            ziel = (pfad.parent / treffer.group(1)).resolve()
            if not ziel.exists():
                befunde.append(f"{rel}: toter Link auf {treffer.group(1)}")
                continue
            if ziel.name == "index.md":
                continue
            try:
                eingehend[ziel.relative_to(wiki).as_posix()] += 1
            except ValueError:
                pass  # Link auf eine Website-Seite ausserhalb des Wikis

    for rel in notizen:
        if eingehend[rel] == 0:
            befunde.append(f"{rel}: verwaist, kein eingehender Link aus dem Wiki")

    return befunde


def main() -> int:
    wurzel = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    befunde = pruefen(wurzel)
    if not befunde:
        print("wiki_lint: keine Befunde.")
        return 0
    print(f"wiki_lint: {len(befunde)} Befunde\n")
    for zeile in befunde:
        print(f"  - {zeile}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
