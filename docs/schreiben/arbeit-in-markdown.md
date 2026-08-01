---
werkzeug:
  schwierigkeit: Fortgeschritten
  kosten: gratis
  wofuer: >-
    die ganze Arbeit in Markdown schreiben, Word nur noch als Export
    behandeln
---

# Die Arbeit in Markdown aufbauen

Wer seine Arbeit direkt in Word schreibt, arbeitet im schlechtesten Format
für die Zusammenarbeit mit LLMs (siehe
[Markdown als Arbeitsformat](../grundlagen/markdown-arbeitsformat.md)).
Die Alternative: Die Arbeit lebt als Sammlung von Markdown-Dateien, und das
abgabefertige Word-Dokument wird daraus **per Werkzeug erzeugt**.

!!! merksatz "Das Grundprinzip"
    Markdown ist die einzige Quelle der Wahrheit. Das Word-Dokument ist ein
    Export, der jederzeit neu erzeugt werden kann, und wird **nie von Hand
    bearbeitet**. Jede inhaltliche Änderung passiert in den Markdown-Dateien.

## Warum sich der Umstieg lohnt

- LLMs können Kapitel lesen, gegenlesen und überarbeiten, ohne an
  Word-Markup zu scheitern; du siehst jede Änderung im Klartext.
- Kapitel sind einzelne Dateien: Du gibst dem Modell gezielt das Kapitel,
  um das es geht, statt der ganzen Arbeit
  (Stichwort [Kontextfenster](../grundlagen/kontextfenster.md)).
- Mit Git hast du eine lückenlose Versionsgeschichte, statt
  `arbeit_final_v3_wirklich.docx`.
- Zitate und Literaturverzeichnis kommen automatisch aus Zotero, im
  gewünschten Zitierstil.

## Die Werkzeugkette

- **Ordner mit Kapiteldateien** als Quelle
- **[Pandoc](https://pandoc.org)** (gratis, Kommandozeile) erzeugt daraus
  das Word-Dokument
- **`reference.docx`** als Formatvorlage: ein Word-Dokument, dessen
  Formatvorlagen (Schrift, Abstände, Überschriften) Pandoc auf den Export
  anwendet. Hier hinterlegst du die Layoutvorgaben deiner Hochschule.
- **Zotero mit Better BibTeX** exportiert die Literatur als `.bib`-Datei,
  ein **CSL-Stil** (z. B. APA) bestimmt das Zitierformat.

## Aufbau

```text
meine-arbeit/
├── kapitel/
│   ├── 01-einleitung.md
│   ├── 02-theorie.md
│   ├── 03-methoden.md
│   ├── 04-ergebnisse.md
│   └── 05-diskussion.md
├── literatur.bib        # Export aus Zotero (Better BibTeX)
├── apa.csl              # Zitierstil, von zotero.org/styles
├── vorlage.docx         # reference.docx mit dem Hochschul-Layout
└── arbeit.docx          # der Export (wird immer neu erzeugt)
```

Zitiert wird im Text mit Schlüsseln aus der `.bib`-Datei:

```markdown
Frühere Arbeiten zeigen dies deutlich [@mueller2024; @smith2023, S. 15].
```

Der Export ist ein einziger Befehl:

```bash
pandoc kapitel/*.md --citeproc --bibliography literatur.bib \
  --csl apa.csl --reference-doc vorlage.docx -o arbeit.docx
```

Pandoc fügt die Kapitel zusammen, löst alle Zitatschlüssel auf, erzeugt das
Literaturverzeichnis und wendet die Formatvorlage an.

## Schritt für Schritt zum Einstieg

1. **Pandoc installieren** (Installer von der offiziellen Seite).
2. **Klein testen:** eine einzelne Markdown-Datei nach Word exportieren,
   bevor die ganze Kette steht.
3. **Vorlage bauen:** `pandoc -o vorlage.docx --print-default-data-file reference.docx`
   erzeugt die Standardvorlage; darin die Formatvorlagen ans Layout der
   Hochschule anpassen.
4. **Zotero anschliessen:** Better-BibTeX-Plugin installieren, Bibliothek
   als `.bib` exportieren (mit automatischer Aktualisierung), CSL-Stil
   herunterladen.
5. **Kapitelweise schreiben.** Der Export bleibt immer ein Befehl.

Die Einrichtung ist übrigens eine ideale Aufgabe für ein LLM: Fehlermeldungen
hineinkopieren, erklären lassen, nachbessern. Wer gar nicht an die
Kommandozeile will, findet in **[Quarto](https://quarto.org)** dasselbe
Prinzip mit mehr Komfort (baut intern ebenfalls auf Pandoc auf).

## Grenzen

- Feinlayout (Deckblatt, spezielle Tabellen, exakte Seitenumbrüche) macht
  man am Schluss einmalig im finalen Word, wenn nichts Inhaltliches mehr
  kommt. Bis dahin: alles in Markdown.
- Der Umstieg lohnt sich am meisten zu **Beginn** einer Arbeit. Mitten im
  Projekt wechseln geht (Pandoc konvertiert auch Word nach Markdown),
  kostet aber einen Aufräum-Nachmittag.
- Und was, wenn die Betreuungsperson im Word kommentiert? Dafür gibt es
  einen eigenen Umgang: [Mit Word-Feedback umgehen](word-feedback.md).
