"""Einmalige Migration: Prosa-Kopf der Quellnotizen ins Frontmatter.

Vorher stand in jeder Quellnotiz unter der Ueberschrift:

    **Evidenzstufe:** Policy (Doku eines Verlags) ·
    **Geprüft:** 06.07.2026, Original vollständig gelesen (Stand Juni 2026)

Diese Angaben stehen groesstenteils schon im Frontmatter (`evidenzstufe`,
`verified`), aber eben nicht ganz: Der Klammerzusatz zur Evidenzstufe und
der Prosateil des Pruefvermerks fehlten dort. Ein blosses Loeschen der
Zeilen wuerde also Information vernichten.

Das Skript holt beides ins Frontmatter (`evidenzstufe_zusatz`,
`pruefnotiz`) und entfernt danach die Prosazeilen. Vor dem Schreiben
prueft es, dass jedes inhaltstragende Wort der alten Prosa im neuen
Frontmatter wieder vorkommt; sonst bricht es ab.

Aufruf:  python tools/migration_notizkopf.py [--schreiben]
Ohne --schreiben laeuft nur der Trockenlauf.
"""
import re
import sys
import unicodedata
from pathlib import Path

QUELLEN = Path("docs/wiki/quellen")

KOPF = re.compile(
    r"^\*\*Evidenzstufe:\*\*\s*(?P<stufe>.+?)\s*·?\s*\n"
    r"\*\*Geprüft:\*\*\s*(?P<geprueft>.+?)(?=\n\s*\n)",
    re.M | re.S,
)

# Wortmaterial, das beim Vergleich ignoriert wird: reine Struktur.
IGNORIEREN = {"evidenzstufe", "geprüft", "und", "der", "die", "das", "aus",
              "im", "in", "am", "vom", "von", "als", "mit", "auf", "zu",
              "ein", "eine", "einer", "einem", "den", "dem", "des"}


def woerter(text: str) -> set:
    """Wortmenge fuer den Verlustvergleich. Datumsangaben werden auf ISO
    normalisiert, weil dieselbe Angabe in der Prosa als 06.07.2026 und im
    Frontmatter als 2026-07-06 steht."""
    text = unicodedata.normalize("NFC", text.lower())
    text = re.sub(r"\b(\d{2})\.(\d{2})\.(\d{4})\b", r"\3-\2-\1", text)
    return {w for w in re.findall(r"[a-zäöüß0-9./-]{3,}", text)
            if w not in IGNORIEREN}


def frontmatter_teilen(inhalt: str):
    if not inhalt.startswith("---"):
        raise ValueError("kein Frontmatter")
    ende = inhalt.index("\n---", 3)
    return inhalt[4:ende], inhalt[ende + 5:]


def stufe_zerlegen(roh: str):
    """'Policy (Doku eines Verlags)' -> ('Policy', 'Doku eines Verlags')"""
    m = re.match(r"^([^(]+?)\s*\((.+)\)\s*$", roh.strip())
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return roh.strip(), None


def notiz_kuerzen(geprueft: str) -> str:
    """Datum und Umfangsangabe stehen schon im Frontmatter; hier bleibt
    der erklaerende Rest. Das Datum am Anfang wird abgeschnitten."""
    text = " ".join(geprueft.split())
    text = re.sub(r"^\d{2}\.\d{2}\.\d{4},\s*", "", text)
    return text.strip()


def yaml_block(text: str) -> str:
    """Mehrzeiliger YAML-Skalar, damit Sonderzeichen unproblematisch sind."""
    umbrochen = []
    zeile = ""
    for wort in text.split():
        if len(zeile) + len(wort) + 1 > 68:
            umbrochen.append(zeile)
            zeile = wort
        else:
            zeile = f"{zeile} {wort}".strip()
    if zeile:
        umbrochen.append(zeile)
    return ">-\n" + "\n".join(f"  {z}" for z in umbrochen)


def main() -> int:
    schreiben = "--schreiben" in sys.argv
    fehler, geaendert = [], []

    for pfad in sorted(QUELLEN.glob("*.md")):
        if pfad.name == "index.md":
            continue
        inhalt = pfad.read_text(encoding="utf-8")
        treffer = KOPF.search(inhalt)
        if not treffer:
            print(f"  uebersprungen (kein Prosakopf): {pfad.name}")
            continue

        kopf_yaml, rumpf = frontmatter_teilen(inhalt)
        stufe, zusatz = stufe_zerlegen(treffer.group("stufe"))
        notiz = notiz_kuerzen(treffer.group("geprueft"))

        # Frontmatter ergaenzen, direkt nach der Zeile evidenzstufe:
        neu_yaml = kopf_yaml
        if zusatz and "evidenzstufe_zusatz:" not in neu_yaml:
            neu_yaml = re.sub(
                r"^(evidenzstufe:.*)$",
                lambda m: f'{m.group(1)}\nevidenzstufe_zusatz: "{zusatz}"',
                neu_yaml, count=1, flags=re.M)
        if notiz and "pruefnotiz:" not in neu_yaml:
            neu_yaml = re.sub(
                r"^(evidenzstufe:.*(?:\nevidenzstufe_zusatz:.*)?)$",
                lambda m: f"{m.group(1)}\npruefnotiz: {yaml_block(notiz)}",
                neu_yaml, count=1, flags=re.M)

        # Gegenprobe 1: Ist die Evidenzstufe im Frontmatter dieselbe wie
        # in der Prosa? Beide wurden bisher getrennt gepflegt.
        fm_stufe = re.search(r"^evidenzstufe:\s*(.+)$", kopf_yaml, re.M)
        if fm_stufe and fm_stufe.group(1).strip().strip('"') != stufe:
            fehler.append(f"{pfad.name}: Evidenzstufe weicht ab "
                          f"(Prosa '{stufe}', Frontmatter '{fm_stufe.group(1).strip()}')")

        # Gegenprobe 2: Stimmt das Pruefdatum aus der Prosa mit dem im
        # Frontmatter ueberein?
        prosa_datum = re.match(r"(\d{2})\.(\d{2})\.(\d{4})",
                               treffer.group("geprueft").strip())
        fm_datum = re.search(r"^\s*-\s*\{[^}]*at:\s*(\d{4}-\d{2}-\d{2})",
                             kopf_yaml, re.M)
        if prosa_datum and fm_datum:
            iso = f"{prosa_datum.group(3)}-{prosa_datum.group(2)}-{prosa_datum.group(1)}"
            if iso != fm_datum.group(1):
                fehler.append(f"{pfad.name}: Prüfdatum weicht ab "
                              f"(Prosa {iso}, Frontmatter {fm_datum.group(1)})")

        # Verlustpruefung: jedes Wort der alten Prosa muss im neuen
        # Frontmatter wieder auftauchen.
        verloren = woerter(treffer.group(0)) - woerter(neu_yaml)
        if verloren:
            fehler.append(f"{pfad.name}: Wörter gingen verloren: {sorted(verloren)}")
            continue

        neuer_rumpf = rumpf.replace(treffer.group(0), "", 1)
        neuer_rumpf = re.sub(r"\n{3,}", "\n\n", neuer_rumpf)
        ergebnis = f"---\n{neu_yaml}\n---\n{neuer_rumpf}"

        geaendert.append(pfad.name)
        if schreiben:
            pfad.write_text(ergebnis, encoding="utf-8")

    print(f"\n{'GESCHRIEBEN' if schreiben else 'TROCKENLAUF'}: "
          f"{len(geaendert)} Notizen, {len(fehler)} Probleme")
    for f in fehler:
        print("  PROBLEM:", f)
    return 1 if fehler else 0


if __name__ == "__main__":
    raise SystemExit(main())
