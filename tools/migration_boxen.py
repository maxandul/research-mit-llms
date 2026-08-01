"""Einmalige Migration: 51 Hinweisboxen auf drei Typen plus Randnotiz.

Vorher gab es acht Boxentypen ohne Konvention. Die Auszaehlung zeigte
drei Probleme:

1. Keine der sechs `quote`-Boxen war ein Zitat. Es waren Merksaetze der
   Website ("Die Regel", "Der rote Faden").
2. Rund ein Drittel der Boxen sprach nicht ueber das Thema, sondern ueber
   die Website ("im Aufbau", "noch nicht abgedeckt", "fuer wen ist diese
   Seite?"). Sie sahen aus wie inhaltliche Warnungen.
3. Viele Boxen waren Absaetze, die eine Box bekommen hatten, weil eine
   Box verfuegbar war.

Neu gibt es `merksatz`, `warnung` und `evidenz` als Boxen, `randnotiz`
als leises Register ohne Kasten, und fuer den Rest Fliesstext.

Die Zuordnung unten ist von Hand erstellt: Jede Box wurde einzeln
gelesen. Sie steht hier, damit die Entscheidungen nachlesbar bleiben.
Merksaetze wurden bewusst nicht vermehrt; es sind genau die sechs, die
vorher als `quote` schon diese Rolle hatten.

Aufruf:  python tools/migration_boxen.py [--schreiben]
"""
import re
import sys
from pathlib import Path

DOCS = Path("docs")

# (Datei, alter Typ, Titel) -> neuer Typ
# Sonderfall "TEXT:<Ersatz>" loest die Box zu Fliesstext auf. Steht dort
# eine Ueberschrift, wird sie vorangestellt; steht dort **Lead.**, wird
# es dem ersten Absatz vorangestellt; leer heisst ersatzlos.
ZUORDNUNG = {
    # --- Merksatz: die sechs, die vorher `quote` waren -----------------
    ("grundlagen/llms-verstehen.md", "Der gemeinsame Nenner"): "merksatz",
    ("grundlagen/rag-vs-wiki.md", "Der Kernunterschied"): "merksatz",
    ("grundlagen/wie-llms-arbeiten.md", "Der rote Faden"): "merksatz",
    ("haltung/ki-deklarieren.md", "Die Haltung dahinter"): "merksatz",
    ("schreiben/arbeit-in-markdown.md", "Das Grundprinzip"): "merksatz",
    ("schreiben/word-feedback.md", "Die Regel"): "merksatz",

    # --- Warnung: Fallstrick, Grenze, Risiko ---------------------------
    ("analysieren/qualitativ-codieren.md", "Stolperstein: das LLM schätzt über den Daumen"): "warnung",
    ("daten/index.md", "Reihenfolge zählt"): "warnung",
    ("erheben/anonymisieren.md", "Die Tabelle ist der Schlüssel"): "warnung",
    ("grundlagen/datenschutz.md", "Grundregel"): "warnung",
    ("grundlagen/kontextfenster.md", "Faustregel"): "warnung",
    ("grundlagen/llms-verstehen.md", "Nicht delegierbar"): "warnung",
    ("ressourcen/prompt-bibliothek.md", "Eine Regel für alle Prompts"): "warnung",
    ("ressourcen/wiki-vorlagen.md", "Verifikation ist der wichtigste Schritt"): "warnung",
    ("werkzeuge/dialog/perplexity.md", "Abgrenzung beachten"): "warnung",
    ("werkzeuge/sammeln/zotero.md", "API-Key lokal halten"): "warnung",
    ("workflows/thema-zu-uebersicht.md", "Was dieser Workflow nicht ersetzt"): "warnung",
    ("workflows/thema-zu-uebersicht.md", "Eine Regel für alle Templates"): "warnung",

    # --- Evidenz: Verweis in den Forschungsstand -----------------------
    ("analysieren/qualitativ-codieren.md", "Evidenz zuletzt geprüft: Juli 2026"): "evidenz",
    ("grundlagen/llms-verstehen.md", "Evidenz zuletzt geprüft: Juli 2026"): "evidenz",
    ("haltung/ki-deklarieren.md", "Evidenz zuletzt geprüft: Juli 2026"): "evidenz",

    # --- Randnotiz: alles ueber die Website statt ueber das Thema ------
    ("grundlagen/datenschutz.md", "Hinweis pro Werkzeug"): "randnotiz",
    ("grundlagen/kontextfenster.md", "Grösse variiert"): "randnotiz",
    ("grundlagen/llms-verstehen.md", "Keine feste Zuordnung"): "randnotiz",
    ("haltung/index.md", "Was hier noch fehlt"): "randnotiz",
    ("index.md", "Diese Seite ist im Aufbau"): "randnotiz",
    ("index.md", "Für wen ist diese Seite?"): "randnotiz",
    ("index.md", "Wichtig zu den Anleitungen"): "randnotiz",
    ("literatur/index.md", "Wenn du nur eines lesen willst"): "randnotiz",
    ("ressourcen/wiki-vorlagen.md", "Warum im Frontmatter und nicht im Text?"): "randnotiz",
    ("schreiben/index.md", "Noch nicht abgedeckt"): "randnotiz",
    ("werkzeuge/finden/connected-papers.md", "Für Fortgeschrittene: die API"): "randnotiz",
    ("werkzeuge/sammeln/llm-wiki.md", "Wie neu das ist"): "randnotiz",
    ("wiki/index.md", "Im Aufbau"): "randnotiz",
    ("wiki/index.md", "Warum die Verifikation so betont wird"): "randnotiz",
    ("wiki/index.md", "Grenzen dieser Recherche"): "randnotiz",
    ("workflows/thema-zu-uebersicht.md", "Vor dem Produktiveinsatz prüfen"): "randnotiz",

    # --- Fliesstext: die Box trug nichts bei ---------------------------
    ("analysieren/qualitativ-codieren.md", "Lohnt sich das bei einer kleinen Interviewstudie?"):
        "TEXT:### Lohnt sich das bei einer kleinen Interviewstudie?",
    ("grundlagen/kontextfenster.md", "Praxis-Trick: erst detailliert zusammenfassen lassen"):
        "TEXT:### Praxis-Trick: erst detailliert zusammenfassen lassen",
    ("grundlagen/markdown-arbeitsformat.md", "Der nächste Schritt"): "TEXT:",
    ("haltung/ki-deklarieren.md", "Faustregel für den Detailgrad"):
        "TEXT:**Faustregel für den Detailgrad.**",
    ("index.md", "Gratis oder bezahlt?"): "TEXT:### Gratis oder bezahlt?",
    ("werkzeuge/dialog/scholarai.md", "Templates als Ausgabeformat"):
        "TEXT:**Templates als Ausgabeformat.**",
    ("workflows/forschungs-wiki.md", "Gelebtes Beispiel auf dieser Website"):
        "TEXT:### Gelebtes Beispiel auf dieser Website",
    ("workflows/forschungs-wiki.md", "Der Kreislauf"): "TEXT:### Der Kreislauf",
    ("workflows/forschungs-wiki.md", "Erst klein, dann automatisieren"):
        "TEXT:**Erst klein, dann automatisieren.**",
    ("workflows/paper-lesen-ablegen.md", "Das Rezept in einem Bild"):
        "TEXT:### Das Rezept in einem Bild",
    ("workflows/paper-lesen-ablegen.md", "Konsistenz zahlt sich aus"):
        "TEXT:**Konsistenz zahlt sich aus.**",
    ("workflows/thema-zu-uebersicht.md", "Das Rezept in einem Bild"):
        "TEXT:### Das Rezept in einem Bild",
    ("workflows/thema-zu-uebersicht.md", "Warum das Template der Trick ist"):
        "TEXT:**Warum das Template der Trick ist.**",
}

BOX = re.compile(
    r'^(?P<marke>!!!|\?\?\?\+?) (?P<typ>[a-z]+)(?: "(?P<titel>[^"]*)")?\n'
    r'(?P<rumpf>(?:^[ \t]+.*\n|^[ \t]*\n(?=[ \t]))*)', re.M)


def entruecken(rumpf: str) -> str:
    """Vier Leerzeichen Einrueckung entfernen, relative Struktur behalten."""
    zeilen = []
    for zeile in rumpf.splitlines():
        if zeile.startswith("    "):
            zeilen.append(zeile[4:])
        elif zeile.startswith("\t"):
            zeilen.append(zeile[1:])
        else:
            zeilen.append(zeile.strip())
    while zeilen and not zeilen[-1].strip():
        zeilen.pop()
    return "\n".join(zeilen)


def main() -> int:
    schreiben = "--schreiben" in sys.argv
    zaehler, offen, fehler = {}, [], []

    for pfad in sorted(DOCS.rglob("*.md")):
        rel = pfad.relative_to(DOCS).as_posix()
        inhalt = pfad.read_text(encoding="utf-8")
        neu = inhalt

        for treffer in reversed(list(BOX.finditer(inhalt))):
            titel = treffer.group("titel") or ""
            ziel = ZUORDNUNG.get((rel, titel))
            if ziel is None:
                offen.append(f"{rel}: '{titel}' ({treffer.group('typ')}) ohne Zuordnung")
                continue

            if ziel.startswith("TEXT:"):
                lead = ziel[5:]
                text = entruecken(treffer.group("rumpf"))
                if lead.startswith("###"):
                    ersatz = f"{lead}\n\n{text}\n"
                elif lead:
                    ersatz = f"{lead} {text.lstrip()}\n"
                else:
                    ersatz = f"{text}\n"
                zaehler["Fliesstext"] = zaehler.get("Fliesstext", 0) + 1
            else:
                kopf = f'{treffer.group("marke")} {ziel}'
                if titel:
                    kopf += f' "{titel}"'
                ersatz = kopf + "\n" + treffer.group("rumpf")
                zaehler[ziel] = zaehler.get(ziel, 0) + 1

            neu = neu[:treffer.start()] + ersatz + neu[treffer.end():]

        neu = re.sub(r"\n{3,}", "\n\n", neu)
        if schreiben and neu != inhalt:
            pfad.write_text(neu, encoding="utf-8")

    print(f"\n{'GESCHRIEBEN' if schreiben else 'TROCKENLAUF'}")
    for typ, n in sorted(zaehler.items()):
        print(f"  {typ:12} {n}")
    print(f"  {'SUMME':12} {sum(zaehler.values())}")
    if offen:
        print(f"\n  ohne Zuordnung ({len(offen)}):")
        for o in offen:
            print("   -", o)
    return 1 if (offen or fehler) else 0


if __name__ == "__main__":
    raise SystemExit(main())
