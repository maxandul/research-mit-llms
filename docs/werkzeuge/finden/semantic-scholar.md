---
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: "API-Nutzung: Fortgeschritten"
  kosten: gratis
  verarbeitung: Cloud
  wofuer: Wissenschaftliche Suchmaschine und Datenbasis vieler anderer Werkzeuge
  phase: [finden]
  stand: August 2026
---

# Semantic Scholar

Eine Suchmaschine für wissenschaftliche Literatur, betrieben vom
Non-Profit-Institut Ai2 (Allen Institute for AI). Nach Anbieterangaben
umfasst der Korpus 214 Millionen Arbeiten, 2,49 Milliarden Zitationen und
79 Millionen Autorenprofile.

Semantic Scholar steht in diesem Bereich zuoberst, weil viele andere
Werkzeuge darauf aufbauen. [Connected Papers](connected-papers.md) etwa
bezieht seine Daten von hier. Wer den Unterbau kennt, versteht auch die
Abdeckungslücken der darauf aufsetzenden Werkzeuge.

## Wofür es taugt

- **Suchen und schnell einordnen.** Zu vielen Arbeiten gibt es eine
  maschinell erzeugte Ein-Satz-Zusammenfassung ("TLDR").
- **Zitationsnetze verfolgen.** Von einem Paper aus vorwärts zu den
  zitierenden und rückwärts zu den zitierten Arbeiten.
- **Stabile Kennungen liefern.** Die Corpus-ID aus der URL nehmen andere
  Werkzeuge als Ausgangspunkt entgegen.
- **Als Datenquelle für Agenten dienen**, über die offene API (siehe
  unten).

## Die API: auch ohne Schlüssel nutzbar

Die Semantic-Scholar-API ist öffentlich und funktioniert **ohne
Registrierung**, praktisch etwa, wenn ein LLM-Agent für dich Literatur
suchen soll. Eine Suchanfrage ist eine simple URL:

```text
https://api.semanticscholar.org/graph/v1/paper/search?query=llm+qualitative+coding&fields=title,authors,year,venue,externalIds
```

Zwei Betriebsarten:

- **Ohne Schlüssel:** Die meisten Endpunkte sind frei zugänglich, teilen
  sich aber ein gemeinsames Kontingent von 1000 Anfragen pro Sekunde
  über alle anonymen Nutzenden hinweg. Bei Andrang wird zusätzlich
  gedrosselt. Für gelegentliche Recherchen reicht das; bei Fehlern kurz
  warten und erneut versuchen.
- **Mit Schlüssel** (kostenlos auf Antrag, kommt per E-Mail): ein eigenes
  Kontingent von einer Anfrage pro Sekunde, also verlässlich statt
  geteilt. Der Schlüssel wird als HTTP-Header `x-api-key` mitgeschickt.

!!! warnung "Schlüssel nicht weitergeben"
    Ein API-Schlüssel ist ein Geheimnis. Er gehört nicht in ein
    öffentliches Repository und nicht in einen Chat.

## Grenzen

- **Abdeckung je nach Fachgebiet unterschiedlich**, und erfasst wird nur
  öffentlich Zugängliches. Die Recherche in den lizenzierten
  Fachdatenbanken deines Fachs über die Hochschulbibliothek ersetzt das
  nicht.
- **TLDR-Zusammenfassungen sind maschinell erzeugt** und teilen die
  Schwächen jedes generierten Textes. Sie taugen zum Sortieren, nicht zum
  Zitieren.
- **Gefundene Quellen bleiben Kandidaten.** Was du verwendest, liest du
  im Volltext.

Für den Datenschutz ist die Seite unkritisch: Sie ist eine öffentliche
Suchmaschine, eigene Dokumente lädst du nicht hoch.

## Wann etwas anderes passt

Wenn du das Umfeld eines einzelnen Papers *sehen* statt lesen willst,
zeichnet [Connected Papers](connected-papers.md) daraus eine Karte. Wenn
du Angaben aus vielen Arbeiten strukturiert nebeneinander brauchst, nimmt
[Elicit](elicit.md) dir die Tabellenarbeit ab. Beide bauen auf demselben
Korpus auf, sind also bei Abdeckungslücken keine Alternative, sondern
teilen sie.

Offizielle Seite: <https://www.semanticscholar.org> ·
API-Doku: <https://api.semanticscholar.org>

---

Vom Suchen zum Sehen: [Connected Papers](connected-papers.md) macht aus
einem Start-Paper eine visuelle Landkarte des Forschungsfelds.
