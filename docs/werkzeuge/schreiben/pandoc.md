---
title: Pandoc
werkzeug:
  schwierigkeit: Fortgeschritten
  kosten: gratis
  verarbeitung: lokal
  wofuer: Markdown nach Word exportieren, mit Zitaten und Literaturverzeichnis
  phase: [schreiben]
  stand: August 2026
---

# Pandoc

Pandoc wandelt Dokumente zwischen Formaten um. Für diese Website ist
genau eine Richtung wichtig: von Markdown nach Word, mit aufgelösten
Zitaten, erzeugtem Literaturverzeichnis und dem Layout deiner
Hochschule. Damit wird der Ansatz aus
[Die Arbeit in Markdown aufbauen](../../schreiben/arbeit-in-markdown.md)
überhaupt erst praktikabel.

Es ist quelloffen, kostenlos, läuft lokal und wird über die
Kommandozeile bedient. Ein einziger Befehl erzeugt die abgabefertige
Datei.

## Wofür es taugt

- **Kapitel zusammenfügen und exportieren.** Aus einem Ordner
  Markdown-Dateien wird ein Word-Dokument.
- **Zitate auflösen.** Mit `--citeproc` und einer `.bib`-Datei aus
  [Zotero](../sammeln/zotero.md) werden Zitierschlüssel zu formatierten
  Belegen, das Literaturverzeichnis entsteht automatisch.
- **Den Zitierstil bestimmen.** Eine CSL-Datei legt fest, ob APA, MLA
  oder der Hausstil deines Instituts gilt.
- **Das Layout der Hochschule anwenden.** Ein `reference.docx` mit den
  vorgegebenen Formatvorlagen wird auf den Export angewendet.
- **Den Rückweg gehen.** Ein kommentiertes Word lässt sich mit
  `--track-changes=all` nach Markdown wandeln, sodass Anmerkungen im
  Text sichtbar werden; siehe
  [Mit Word-Feedback umgehen](../../schreiben/word-feedback.md).

## Grenzen

- **Kommandozeile.** Es gibt keine Oberfläche. Der Befehl ist kurz, aber
  er muss getippt werden.
- **Feinlayout bleibt Handarbeit.** Deckblatt, spezielle Tabellen und
  exakte Seitenumbrüche macht man am Schluss einmalig im finalen Word,
  wenn inhaltlich nichts mehr kommt.
- **Fehlermeldungen sind knapp.** Wenn eine CSL-Datei oder ein
  Zitierschlüssel nicht passt, ist die Meldung selten selbsterklärend.
  Das ist eine der Aufgaben, bei denen ein LLM gut hilft: Meldung
  hineinkopieren, erklären lassen.

## Wann etwas anderes passt

Wer dieselbe Kette ohne Kommandozeile will, findet in
[Quarto](quarto.md) mehr Komfort; es baut intern ebenfalls auf Pandoc
auf. Wer die Arbeit ohnehin in Word schreibt, braucht Pandoc nicht,
verliert dafür die Vorteile aus
[Markdown als Arbeitsformat](../../grundlagen/markdown-arbeitsformat.md).

Offizielle Seite: <https://pandoc.org> ·
Zitierstile: <https://www.zotero.org/styles>

---

Weiter zum Umgang mit Rückmeldungen:
[Mit Word-Feedback umgehen](../../schreiben/word-feedback.md).
