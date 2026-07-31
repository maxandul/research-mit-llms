---
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: "API-Nutzung: Fortgeschritten"
  kosten: gratis
  wofuer: visuelle Literatur-Landkarten
  stand: Juni 2026
---

# Connected Papers

## Was ist es?

Ein Werkzeug, das aus einem Start-Paper eine visuelle Landkarte ähnlicher
Arbeiten erzeugt, gruppiert nach inhaltlicher Ähnlichkeit, nicht nur nach
direkten Zitaten. Basiert auf dem Korpus von
[Semantic Scholar](semantic-scholar.md).

## Was bringt es für Research?

- Schneller Überblick über ein neues Forschungsfeld.
- "Prior Works" und "Derivative Works" entdecken.
- Wichtige, evtl. übersehene Arbeiten visuell erkennen.

## Voraussetzungen

- Nur ein Browser. Im Gratis-Rahmen eine begrenzte Zahl an Graphen.

## Einrichtung / Nutzung (High-Level)

1. Start-Paper suchen (Titel, DOI oder Semantic-Scholar-ID).
2. Graph erzeugen lassen; Knoten anklicken, um verwandte Arbeiten zu sehen.
3. Interessante Treffer in deine Literaturverwaltung übernehmen.

## Grenzen & Datenschutz

- Öffentliche Daten, keine sensiblen Eingaben.
- Gratis-Kontingent begrenzt.

??? note "Für Fortgeschrittene: die API"
    Es gibt eine API mit Python- und JS-Client. Sie ist allerdings
    "early access" (Zugangs-Token per Anfrage) und kommerziell, für den
    niederschwelligen Einstieg nicht nötig. Token-Anfrage:
    hello@connectedpapers.com
    Clients: <https://github.com/ConnectedPapers/connectedpapers-py>

## Offizielle Links

- Website: <https://www.connectedpapers.com>

---

Nächstes Werkzeug: [Elicit](elicit.md) fasst Erkenntnisse aus mehreren
Arbeiten in strukturierten Vergleichstabellen zusammen.
