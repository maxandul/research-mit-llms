---
title: Quarto
werkzeug:
  schwierigkeit: Fortgeschritten
  kosten: gratis
  verarbeitung: lokal
  wofuer: Dieselbe Export-Kette wie Pandoc, mit mehr Komfort und Code-Ausgabe
  phase: [schreiben, analysieren]
  stand: August 2026
---

# Quarto

Quarto ist ein Publikationssystem, das intern auf
[Pandoc](pandoc.md) aufbaut und darum herum Komfort ergänzt: eine
Vorschau während des Schreibens, Projektdateien statt langer Befehle,
Integration in VS Code und RStudio, und Ausgabe nach Word, PDF, HTML
oder Präsentation aus derselben Quelle.

Der zweite Unterschied ist die Code-Ausführung: Analysecode kann direkt
im Dokument stehen und beim Export ausgeführt werden. Tabellen und
Abbildungen entstehen dann aus den Daten, statt hineinkopiert zu werden.

## Wofür es taugt

- **Dieselbe Kette wie Pandoc, mit weniger Kommandozeile.** Zitate,
  Literaturverzeichnis und Hochschul-Layout funktionieren gleich, die
  Einstellungen stehen in einer Projektdatei.
- **Reproduzierbar auswerten und schreiben in einem.** Wer ohnehin
  [quantitativ auswertet](../../analysieren/quantitativ-auswerten.md),
  kann Code und Text zusammenhalten. Ändern sich die Daten, ändern sich
  Tabellen und Abbildungen beim nächsten Export mit.
- **Mehrere Ausgabeformate aus einer Quelle**, ohne den Text zu
  duplizieren.

## Grenzen

- **Mehr Software als Pandoc.** Wer nur Markdown nach Word exportieren
  will, installiert mit Quarto deutlich mehr, als er braucht.
- **Der Nutzen der Code-Ausführung hängt an der Arbeitsweise.** Wer
  seine Auswertung nicht selbst schreibt, sondern im Chat rechnen lässt,
  hat davon wenig.
- **Feinlayout bleibt Handarbeit**, wie bei Pandoc auch.

## Wann etwas anderes passt

Für den reinen Word-Export aus Markdown genügt [Pandoc](pandoc.md), und
es ist die kleinere Abhängigkeit. Wer weder das eine noch das andere
will, findet in
[Die Arbeit in Markdown aufbauen](../../schreiben/arbeit-in-markdown.md)
die Einordnung, was der Verzicht kostet.

Offizielle Seite: <https://quarto.org>

---

Weiter zum Umgang mit Rückmeldungen:
[Mit Word-Feedback umgehen](../../schreiben/word-feedback.md).
