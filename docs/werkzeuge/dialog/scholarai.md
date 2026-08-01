---
werkzeug:
  schwierigkeit: Fortgeschritten
  kosten: ChatGPT Plus
  kosten_zusatz: nötig zum Erstellen eigener GPTs
  wofuer: Literatursuche und Volltext-Analyse im Chat
---

# ScholarAI (Custom GPT)

## Was ist es?

ScholarAI ist eine Anbindung (eine "Action"), mit der ein eigener Custom GPT
in ChatGPT wissenschaftliche Datenbanken durchsuchen, Volltexte lesen und
Fragen zu einzelnen Papers beantworten kann.

## Was bringt es für Research?

- Im Chat nach Papers suchen, mit echten, verlinkten Quellen statt
  erfundenen.
- PDFs/Volltexte gezielt befragen (Methoden, Limitationen, Daten).
- Mit weiteren Anbindungen (z.B. Zotero, Notion) zu einem durchgängigen
  Arbeitsablauf verketten, siehe Workflow
  [Vom Thema zur Literaturübersicht](../../workflows/thema-zu-uebersicht.md).

## Voraussetzungen

- ChatGPT Plus (Custom GPTs erstellen).
- Ein kostenloser ScholarAI-API-Schlüssel.

## Einrichtung (High-Level)

1. API-Schlüssel bei ScholarAI anfordern.
2. In ChatGPT einen neuen GPT anlegen und eine "Action" erstellen.
3. Authentifizierung: API-Key, Custom-Header `X-ScholarAI-API-Key`.
4. Schema importieren von `https://api.scholarai.io/openapi.yaml`.
5. Instruktion (System-Prompt) einsetzen, siehe Bausteine unten.

Die verbindliche, stets aktuelle Schritt-für-Schritt-Anleitung:
<https://docs.scholarai.io/make-a-gpt>

## System-Prompt-Bausteine je Einsatzzweck

Setze den passenden Baustein als Instruktion ein oder nutze ihn als
Eröffnungs-Prompt. Alle Bausteine teilen eine Grundregel: **keine Aussage
ohne verlinkte Quelle, keine erfundenen Zitate.**

### 1. Explorativer Überblick

```text
Rolle: Du kartierst ein mir neues Forschungsfeld.
Aufgabe: Finde via search_abstracts die wichtigsten Arbeiten und
Review-Artikel zum Thema. Gib mir eine Landkarte des Feldes.
Ausgabe:
- 3-5 zentrale Arbeiten / Reviews, je mit [Autor et al., Jahr](URL)
- die wichtigsten Teilthemen / Strömungen in Stichworten
- 3 offene Fragen, die ich als nächstes verfolgen könnte
Regel: Keine Aussage ohne verlinkte Quelle.
```

### 2. Gezielte Literatursuche

```text
Rolle: Du bist ein präziser Literatur-Rechercheassistent.
Aufgabe: Beantworte meine Frage ausschliesslich auf Basis von Quellen,
die du via search_abstracts findest. Bei Unsicherheit nutze getFullText
oder question am Paper selbst, statt zu raten.
Ausgabe:
- 5-8 relevante Arbeiten, je mit [Autor et al., Jahr](URL)
- 1 Satz, warum die Arbeit relevant ist
- am Ende: 2-3 offene Anschlussfragen
Regel: Keine Aussage ohne verlinkte Quelle. Keine erfundenen Zitate.
```

### 3. Deep Read (ein Paper tief befragen)

```text
Rolle: Du analysierst eine einzelne Arbeit gründlich.
Aufgabe: Nutze getFullText für das PDF und question für Detailfragen.
Beantworte zu diesem Paper:
- Fragestellung und Kernbeitrag
- Methode und Datengrundlage
- zentrale Ergebnisse
- Limitationen und offene Punkte
Ausgabe: kompakte Stichpunkte, mit Verweis auf Abschnitt/Seite, wo möglich.
Regel: Wenn etwas im Text nicht steht, sag das ausdrücklich.
```

### 4. Synthese / Mini-Review

```text
Rolle: Du vergleichst mehrere Arbeiten und synthetisierst.
Aufgabe: Für die folgenden Papers (oder deine Suchtreffer):
- stelle die Befunde gegenüber
- markiere Übereinstimmungen und Widersprüche
- benenne Forschungslücken
Ausgabe:
- Vergleichstabelle (Arbeit | Befund | Methode | Einschränkung)
- 1 Absatz Synthese
- 3 Lücken / Anschlussfragen
Regel: Jede Zeile mit verlinkter Quelle. Widersprüche nicht glätten.
```

### 5. Zitations-Verfolgung

```text
Rolle: Du zeichnest die Entwicklung eines Feldes nach.
Aufgabe: Ausgehend von der genannten Arbeit, nutze literature_map /
verwandte Arbeiten, um frühere Grundlagen und spätere Weiterentwicklungen
zu finden.
Ausgabe:
- "Baut auf" (Prior Works), 3-5 Arbeiten mit Link
- "Wurde weiterentwickelt in" (Derivative Works), 3-5 Arbeiten mit Link
- 1 Satz, wie sich das Feld über die Zeit verschoben hat
Regel: Keine Aussage ohne verlinkte Quelle.
```

**Templates als Ausgabeformat.** Du kannst dem GPT zusätzlich ein festes Ausgabeformat vorgeben, etwa
Markdown für dein [LLM-Wiki](../sammeln/llm-wiki.md) oder eine
Struktur, die direkt nach [Notion](../sammeln/notion.md) /
[Zotero](../sammeln/zotero.md) passt. So sind Funde sofort ablagefertig.

## Grenzen & Datenschutz

- Läuft über ChatGPT (Cloud). Keine vertraulichen unveröffentlichten
  Daten hochladen, ausser die institutionellen Vorgaben erlauben es.
- In den ChatGPT-Einstellungen prüfen, ob Eingaben zum Training genutzt
  werden.

## Offizielle Links

- Anleitung "Make a GPT": <https://docs.scholarai.io/make-a-gpt>
- ScholarAI: <https://scholarai.io>

---

Statt eigene Quellen anzubinden, kannst du auch nur mit deinen eigenen
Dokumenten chatten: [NotebookLM](notebooklm.md).
