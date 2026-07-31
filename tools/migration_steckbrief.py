"""Einmalige Migration: "Auf einen Blick" ins Frontmatter.

Vorher stand auf 15 Seiten oben ein Kasten:

    !!! info "Auf einen Blick"
        **Schwierigkeit:** Einsteiger bis Profi (Grundfunktionen einfach,
        LLM-Anbindung anspruchsvoller) · **Kosten:** gratis (Speicher-Abo
        optional) · **Wofür:** Literaturverwaltung

Als Fliesstext war das weder einheitlich noch auswertbar: Die Stufen
kamen als Spannen und Klammerzusaetze vor, "Kosten" mischte Preis und
Vorbehalt. Die Zuordnung unten trennt beides in ein festes Feld und einen
freien Zusatz. Sie ist von Hand erstellt, weil die Umformung Urteil
verlangt; sie steht hier, damit die Entscheidungen nachlesbar bleiben.

`stand:` wird nur gesetzt, wo die Seite selbst ein Datum nannte. Wo es
fehlt, meldet es tools/wiki_lint.py als Luecke.

Aufruf:  python tools/migration_steckbrief.py [--schreiben]
"""
import re
import sys
from pathlib import Path

DOCS = Path("docs")

ZUORDNUNG = {
    "analysieren/qualitativ-codieren.md": dict(
        schwierigkeit="Einsteiger", kosten="gratis bis Abo",
        wofuer="Interviews und offene Antworten mit einem LLM als zweitem "
               "Codierer auswerten"),
    "analysieren/quantitativ-auswerten.md": dict(
        schwierigkeit="Einsteiger", kosten="Freemium",
        wofuer="Daten deskriptiv und statistisch auswerten, ohne selbst zu "
               "programmieren"),
    "erheben/anonymisieren.md": dict(
        schwierigkeit="Einsteiger", kosten="gratis",
        wofuer="sensible Daten so aufbereiten, dass sie in Cloud-Diensten "
               "bearbeitet werden können"),
    "erheben/transkription.md": dict(
        schwierigkeit="Profi",
        schwierigkeit_zusatz="Einsteiger-Alternativen ohne Kommandozeile vorhanden",
        kosten="gratis",
        wofuer="Audio- und Videoaufnahmen lokal transkribieren, auch "
               "Schweizerdeutsch",
        stand="Juli 2026"),
    "schreiben/arbeit-in-markdown.md": dict(
        schwierigkeit="Fortgeschritten", kosten="gratis",
        wofuer="die ganze Arbeit in Markdown schreiben, Word nur noch als "
               "Export behandeln"),
    "schreiben/word-feedback.md": dict(
        schwierigkeit="Einsteiger",
        schwierigkeit_zusatz="maschineller Weg über Pandoc: Fortgeschritten",
        kosten="gratis",
        wofuer="Kommentare aus Word zurück in die Markdown-Quelle bringen, "
               "ohne die Kette zu brechen"),
    "werkzeuge/dialog/notebooklm.md": dict(
        schwierigkeit="Einsteiger", kosten="gratis",
        wofuer="mit den eigenen Quellen chatten", stand="Juni 2026"),
    "werkzeuge/dialog/perplexity.md": dict(
        schwierigkeit="Einsteiger", kosten="Freemium",
        wofuer="Antwortmaschine mit Quellenangaben"),
    "werkzeuge/dialog/scholarai.md": dict(
        schwierigkeit="Fortgeschritten", kosten="ChatGPT Plus",
        kosten_zusatz="nötig zum Erstellen eigener GPTs",
        wofuer="Literatursuche und Volltext-Analyse im Chat"),
    "werkzeuge/finden/connected-papers.md": dict(
        schwierigkeit="Einsteiger",
        schwierigkeit_zusatz="API-Nutzung: Fortgeschritten",
        kosten="gratis", wofuer="visuelle Literatur-Landkarten",
        stand="Juni 2026"),
    "werkzeuge/finden/elicit.md": dict(
        schwierigkeit="Einsteiger", kosten="Freemium",
        kosten_zusatz="Kontingente sind eine Schätzung",
        wofuer="LLM-gestützte Literaturreviews", stand="Juni 2026"),
    "werkzeuge/finden/semantic-scholar.md": dict(
        schwierigkeit="Einsteiger", kosten="gratis",
        wofuer="wissenschaftliche Suchmaschine und Datenbasis"),
    "werkzeuge/sammeln/llm-wiki.md": dict(
        schwierigkeit="Einsteiger",
        schwierigkeit_zusatz="je nach Variante bis Fortgeschritten",
        kosten="gratis", wofuer="persistente, wachsende Wissensbasis"),
    "werkzeuge/sammeln/notion.md": dict(
        schwierigkeit="Einsteiger", kosten="Freemium",
        wofuer="Notizen und Datenbanken als Wissensbasis"),
    "werkzeuge/sammeln/zotero.md": dict(
        schwierigkeit="Einsteiger",
        schwierigkeit_zusatz="Grundfunktionen einfach, LLM-Anbindung bis Profi",
        kosten="gratis", kosten_zusatz="Speicher-Abo optional",
        wofuer="Literaturverwaltung"),
}

BLOCK = re.compile(r'^!!! info "Auf einen Blick"\n(?:^[ \t]+.*\n)+', re.M)

# Der wiederkehrende Kasten am Seitenende. Sein Inhalt steckt jetzt im
# `stand`-Feld des Steckbriefs, deshalb faellt er weg.
KOSTENHINWEIS = re.compile(r'^!!! note "Hinweis zu Kosten[^"\n]*"\n(?:^[ \t]+.*\n|^\n(?=[ \t]))+',
                           re.M)


def yaml_wert(text: str) -> str:
    text = " ".join(str(text).split())
    if len(text) <= 60:
        return f'"{text}"' if any(c in text for c in ':#"') else text
    zeilen, zeile = [], ""
    for wort in text.split():
        if len(zeile) + len(wort) + 1 > 66:
            zeilen.append(zeile)
            zeile = wort
        else:
            zeile = f"{zeile} {wort}".strip()
    zeilen.append(zeile)
    return ">-\n" + "\n".join(f"    {z}" for z in zeilen)


def block_bauen(felder: dict) -> str:
    reihenfolge = ["schwierigkeit", "schwierigkeit_zusatz", "kosten",
                   "kosten_zusatz", "wofuer", "stand"]
    zeilen = ["werkzeug:"]
    for schluessel in reihenfolge:
        if schluessel in felder:
            zeilen.append(f"  {schluessel}: {yaml_wert(felder[schluessel])}")
    return "\n".join(zeilen)


def main() -> int:
    schreiben = "--schreiben" in sys.argv
    fehler, ok = [], []

    for rel, felder in sorted(ZUORDNUNG.items()):
        pfad = DOCS / rel
        if not pfad.exists():
            fehler.append(f"{rel}: Datei fehlt")
            continue
        inhalt = pfad.read_text(encoding="utf-8")

        treffer = BLOCK.search(inhalt)
        if not treffer:
            fehler.append(f"{rel}: kein Block 'Auf einen Blick' gefunden")
            continue

        # Gegenprobe: Steht der Wert aus der Zuordnung auch wirklich im
        # alten Block? Schuetzt vor Vertippern in der Tabelle oben.
        alt = " ".join(treffer.group(0).split())
        for schluessel in ("schwierigkeit", "kosten"):
            wert = felder[schluessel].split()[0]
            if wert.lower() not in alt.lower():
                fehler.append(f"{rel}: '{wert}' steht nicht im alten Block: {alt[:110]}")

        rumpf = inhalt
        block = block_bauen(felder)
        if rumpf.startswith("---"):
            ende = rumpf.index("\n---", 3)
            rumpf = rumpf[:ende] + "\n" + block + rumpf[ende:]
        else:
            rumpf = f"---\n{block}\n---\n\n" + rumpf

        rumpf = BLOCK.sub("", rumpf, count=1)
        if "stand" in felder:
            rumpf = KOSTENHINWEIS.sub("", rumpf)
        rumpf = re.sub(r"\n{3,}", "\n\n", rumpf)

        ok.append(rel)
        if schreiben:
            pfad.write_text(rumpf, encoding="utf-8")

    print(f"\n{'GESCHRIEBEN' if schreiben else 'TROCKENLAUF'}: "
          f"{len(ok)} Seiten, {len(fehler)} Probleme")
    for f in fehler:
        print("  PROBLEM:", f)
    return 1 if fehler else 0


if __name__ == "__main__":
    raise SystemExit(main())
