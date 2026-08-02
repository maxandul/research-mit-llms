---
title: Gemini Notebook
werkzeug:
  schwierigkeit: Einsteiger
  kosten: Freemium
  verarbeitung: Cloud
  wofuer: Mit den eigenen Quellen chatten, mit Beleg in den Dokumenten
  phase: [befragen, analysieren]
  stand: August 2026
---

# Gemini Notebook (früher NotebookLM)

Du legst ein Notizbuch an, lädst eigene Quellen hinein (PDFs, Texte,
Links) und stellst Fragen dazu. Geantwortet wird ausschliesslich aus
diesen Quellen, mit Verweis auf die Stelle im Dokument. Das ist der
Unterschied zu einem gewöhnlichen Chat: Das Modell darf nicht aus dem
Trainingswissen ergänzen, und du kannst jede Aussage bis in die
Originalseite zurückverfolgen.

!!! randnotiz "Neuer Name seit Juli 2026"
    Google hat NotebookLM am 16. Juli 2026 in **Gemini Notebook**
    umbenannt. Es bleibt dasselbe eigenständige Produkt, ist aber enger
    mit der Gemini-App und der Google-Suche verzahnt. Bestehende Links
    und geteilte Notizbücher funktionieren laut Anbieter weiter.

## Wofür es taugt

- **Eine Papersammlung befragen**, ohne dass Quellen erfunden werden.
  Was nicht in den hochgeladenen Dokumenten steht, wird nicht behauptet.
- **Belege nachverfolgen.** Jede Aussage verweist auf die Stelle im
  Original, das macht das Gegenprüfen schnell statt mühsam.
- **Überblick über viele Quellen gewinnen**, etwa thematische
  Zusammenfassungen über eine ganze Sammlung hinweg.
- **Daten aus den eigenen Quellen auswerten.** Seit Juli 2026 kann jedes
  Notizbuch Code schreiben und in einer abgesicherten Umgebung ausführen.
  Das entspricht dem Prinzip aus
  [Quantitativ auswerten](../../analysieren/quantitativ-auswerten.md):
  Nicht das Modell rechnet, sondern ein Programm.

Die Code-Ausführung war bei Redaktionsschluss noch nicht für alle
Kontostufen verfügbar; Google kündigte die Ausweitung für die Wochen
danach an.

## Grenzen

- **Es arbeitet nur mit dem, was du gibst.** Das ist der Zweck, aber es
  heisst auch: Kein Blick ins Feld, keine Literatursuche. Die Quellen
  musst du vorher selbst gefunden haben.
- **Belegtreue ist nicht Interpretationstreue.** Der Verweis zeigt, wo
  etwas herkommt, nicht ob es richtig verstanden wurde. Bei
  Zusammenfassungen längerer Argumentationen bleibt das Nachlesen nötig.
- **Deine Dokumente liegen in Googles Cloud.** Google gibt an, Daten von
  Organisationen und Schulen nicht fürs Training zu verwenden und bei
  Privatkonten nur dann, wenn Feedback gegeben wird. Ob du unveröffentlichte
  Manuskripte oder Interviewmaterial dort hochladen darfst, entscheidet
  nicht diese Angabe, sondern die
  [Grundregel zum Datenschutz](../../grundlagen/datenschutz.md) und was
  für dein Material gilt.
- **Google-Konto nötig.**

## Wann etwas anderes passt

Wenn du Literatur erst *finden* musst, führt der Weg über
[Semantic Scholar](../finden/semantic-scholar.md) oder
[Elicit](../finden/elicit.md). Wenn du Angaben aus vielen Arbeiten
tabellarisch vergleichen willst, ist Elicit näher dran. Für Fragen ans
offene Web statt an die eigenen Quellen ist
[Perplexity](perplexity.md) gedacht. Und wenn das Wissen über ein
einzelnes Projekt hinaus bleiben soll, statt in einem Notizbuch zu
liegen, lohnt der Blick auf das
[LLM-Wiki](../sammeln/llm-wiki.md).

Offizielle Seite: <https://notebooklm.google>

---

Für den schnellen Überblick über das offene Web statt der eigenen
Quellen: [Perplexity](perplexity.md).
