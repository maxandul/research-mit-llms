---
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: "API-Nutzung: Fortgeschritten"
  kosten: Freemium
  kosten_zusatz: fünf Graphen pro Monat gratis
  verarbeitung: Cloud
  wofuer: Das Umfeld eines Papers als Karte sehen
  phase: [finden]
  stand: August 2026
---

# Connected Papers

Du gibst ein Paper an, und Connected Papers zeichnet daraus eine Karte
verwandter Arbeiten. Verwandt heisst hier nicht "zitiert sich
gegenseitig", sondern "teilt Zitationsmuster": Zwei Arbeiten stehen nah
beieinander, wenn sie dieselbe Literatur zitieren und von denselben
Arbeiten zitiert werden. Deshalb tauchen auch Papers auf, die einander
nie erwähnen, aber am selben Problem arbeiten.

Die Daten kommen von [Semantic Scholar](semantic-scholar.md).

## Wofür es taugt

- **Ein unbekanntes Feld überblicken.** Aus einem Paper, das du schon
  hast, wird sichtbar, welche Gruppen und Stränge es gibt.
- **Vorläufer und Nachfolger finden.** Die Ansichten "Prior Works" und
  "Derivative Works" zeigen die einflussreichsten Arbeiten davor und
  danach.
- **Lücken in der eigenen Liste entdecken.** Wenn ein grosser Knoten in
  der Karte in deiner Literaturverwaltung fehlt, hast du etwas übersehen.
- **Von mehreren Startpunkten ausgehen.** Multi-Origin-Graphen bauen die
  Karte aus mehreren Papers gleichzeitig auf.

## Grenzen

- **Fünf Graphen pro Monat in der Gratis-Stufe.** Alle Funktionen sind
  enthalten, aber die Zahl der Karten ist gedeckelt. Wer ein Feld
  systematisch erschliesst, ist damit an einem Nachmittag durch. Für
  unbegrenzte Graphen gibt es einen akademischen Tarif, der deutlich
  günstiger ist als der geschäftliche.
- **Ähnlichkeit ist nicht Relevanz.** Die Karte zeigt, was zitatstrukturell
  zusammengehört. Ob eine Arbeit für deine Fragestellung taugt, sagt sie
  nicht.
- **Junge Arbeiten sind unterrepräsentiert.** Ein Paper, das noch kaum
  zitiert wurde, hat wenig Struktur, an der sich Ähnlichkeit festmachen
  liesse.
- **Erbt die Abdeckungslücken von Semantic Scholar.** Was dort fehlt,
  fehlt auch hier.

Für den Datenschutz unkritisch: Du gibst einen Papertitel oder eine DOI
ein, keine eigenen Dokumente.

## Wann etwas anderes passt

Für die reine Suche ist [Semantic Scholar](semantic-scholar.md) direkter
und unbegrenzt. Wenn du nicht das Umfeld sehen, sondern Angaben aus
mehreren Arbeiten vergleichen willst, ist [Elicit](elicit.md) das
passendere Werkzeug.

??? randnotiz "Für Fortgeschrittene: die API"
    Es gibt eine API mit Python- und JS-Client. Sie ist "early access"
    (Zugangs-Token auf Anfrage) und kommerziell, für den
    niederschwelligen Einstieg nicht nötig. Token-Anfrage:
    hello@connectedpapers.com ·
    Clients: <https://github.com/ConnectedPapers/connectedpapers-py>

Offizielle Seite: <https://www.connectedpapers.com>

---

Nächstes Werkzeug: [Elicit](elicit.md) trägt Angaben aus vielen Arbeiten
in eine gemeinsame Vergleichstabelle ein.
