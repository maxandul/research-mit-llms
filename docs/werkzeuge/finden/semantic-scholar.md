---
werkzeug:
  schwierigkeit: Einsteiger
  kosten: gratis
  wofuer: wissenschaftliche Suchmaschine und Datenbasis
---

# Semantic Scholar

## Was ist es?

Eine kostenlose, KI-gestützte Suchmaschine für wissenschaftliche Literatur
mit einem riesigen Paper-Korpus. Viele andere Werkzeuge (u.a.
[Connected Papers](connected-papers.md)) bauen auf dieser Datenbasis auf,
deshalb steht Semantic Scholar hier zuoberst.

## Was bringt es für Research?

- Paper suchen und Zusammenfassungen ("TLDR") lesen.
- Zitationen und referenzierte Arbeiten verfolgen.
- Stabile Paper-IDs (Corpus-ID / "ShaID"), die andere Tools weiterverwenden.

## Voraussetzungen

- Nur ein Browser. Konto optional (für gespeicherte Bibliotheken).
- Für Entwickler:innen gibt es eine kostenlose API (siehe unten).

## Die API: auch ohne Key nutzbar

Die Semantic-Scholar-API ist öffentlich und funktioniert **ohne
Registrierung und ohne API-Key** — praktisch z.B., wenn ein LLM-Agent für
dich Literatur suchen soll. Eine Suchanfrage ist eine simple URL:

```text
https://api.semanticscholar.org/graph/v1/paper/search?query=llm+qualitative+coding&fields=title,authors,year,venue,externalIds
```

Zwei Betriebsarten:

- **Ohne Key:** gemeinsames, striktes Ratenlimit für alle anonymen
  Nutzer:innen. Für gelegentliche Recherchen völlig ausreichend; bei
  Überlastung kurz warten und erneut versuchen.
- **Mit Key** (kostenlos auf Antrag): eigenes Kontingent, derzeit
  1 Anfrage pro Sekunde. Der Key wird als HTTP-Header `x-api-key`
  mitgeschickt. Achtung: Der Key ist ein Geheimnis — nie in ein
  öffentliches Repo committen und nicht in Chats einfügen.

## Einrichtung / Nutzung (High-Level)

1. Seite öffnen und Stichwort oder Paper-Titel suchen.
2. Auf der Paper-Seite die TLDR-Zusammenfassung, Zitationen und References
   nutzen, um verwandte Arbeiten zu finden.
3. Die Paper-ID aus der URL kopieren, wenn ein anderes Tool sie braucht.

## Grenzen & Datenschutz

- Abdeckung je nach Fachgebiet unterschiedlich; erfasst wird nur öffentlich
  Zugängliches. **Ersetzt die Recherche in den lizenzierten Fachdatenbanken
  deines Fachs (via Hochschulbibliothek) nicht.**
- Gefundene Quellen bleiben Kandidaten: Was du verwenden willst, liest du
  selbst im Volltext.
- Öffentliche Suchmaschine; keine sensiblen eigenen Daten nötig.

## Offizielle Links

- Website: <https://www.semanticscholar.org>
- API-Doku: <https://api.semanticscholar.org>
