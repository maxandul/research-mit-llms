# ScholarAI (Custom GPT)

!!! info "Auf einen Blick"
    **Schwierigkeit:** Einsteiger · **Kosten:** ChatGPT Plus (zum Erstellen eigener GPTs) · **Wofuer:** Literatursuche & Volltext-Analyse im Chat

## Was ist es?

ScholarAI ist eine Anbindung (eine "Action"), mit der ein eigener Custom GPT
in ChatGPT wissenschaftliche Datenbanken durchsuchen, Volltexte lesen und
Fragen zu einzelnen Papers beantworten kann.

## Was bringt es fuer Research?

- Im Chat nach Papers suchen — mit echten, verlinkten Quellen statt
  erfundenen.
- PDFs/Volltexte gezielt befragen (Methoden, Limitationen, Daten).
- Mit weiteren Anbindungen (z.B. Zotero, Notion) zu einem durchgaengigen
  Arbeitsablauf verketten — siehe Workflow
  [Vom Thema zur Literaturuebersicht](../../workflows/thema-zu-uebersicht.md).

## Voraussetzungen

- ChatGPT Plus (Custom GPTs erstellen).
- Ein kostenloser ScholarAI-API-Schluessel.

## Einrichtung (High-Level)

1. API-Schluessel bei ScholarAI anfordern.
2. In ChatGPT einen neuen GPT anlegen und eine "Action" erstellen.
3. Authentifizierung: API-Key, Custom-Header `X-ScholarAI-API-Key`.
4. Schema importieren von `https://api.scholarai.io/openapi.yaml`.
5. Instruktion (System-Prompt) einsetzen — siehe Bausteine unten.

Die verbindliche, stets aktuelle Schritt-fuer-Schritt-Anleitung:
<https://docs.scholarai.io/make-a-gpt>

## System-Prompt-Bausteine je Einsatzzweck

Setze den passenden Baustein als Instruktion ein oder nutze ihn als
Eroeffnungs-Prompt. Alle Bausteine teilen eine Grundregel: **keine Aussage
ohne verlinkte Quelle, keine erfundenen Zitate.**

### 1. Explorativer Ueberblick

```text
Rolle: Du kartierst ein mir neues Forschungsfeld.
Aufgabe: Finde via search_abstracts die wichtigsten Arbeiten und
Review-Artikel zum Thema. Gib mir eine Landkarte des Feldes.
Ausgabe:
- 3-5 zentrale Arbeiten / Reviews, je mit [Autor et al., Jahr](URL)
- die wichtigsten Teilthemen / Stroemungen in Stichworten
- 3 offene Fragen, die ich als naechstes verfolgen koennte
Regel: Keine Aussage ohne verlinkte Quelle.
```

### 2. Gezielte Literatursuche

```text
Rolle: Du bist ein praeziser Literatur-Rechercheassistent.
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
Rolle: Du analysierst eine einzelne Arbeit gruendlich.
Aufgabe: Nutze getFullText fuer das PDF und question fuer Detailfragen.
Beantworte zu diesem Paper:
- Fragestellung und Kernbeitrag
- Methode und Datengrundlage
- zentrale Ergebnisse
- Limitationen und offene Punkte
Ausgabe: kompakte Stichpunkte, mit Verweis auf Abschnitt/Seite, wo moeglich.
Regel: Wenn etwas im Text nicht steht, sag das ausdruecklich.
```

### 4. Synthese / Mini-Review

```text
Rolle: Du vergleichst mehrere Arbeiten und synthetisierst.
Aufgabe: Fuer die folgenden Papers (oder deine Suchtreffer):
- stelle die Befunde gegenueber
- markiere Uebereinstimmungen und Widersprueche
- benenne Forschungsluecken
Ausgabe:
- Vergleichstabelle (Arbeit | Befund | Methode | Einschraenkung)
- 1 Absatz Synthese
- 3 Luecken / Anschlussfragen
Regel: Jede Zeile mit verlinkter Quelle. Widersprueche nicht glaetten.
```

### 5. Zitations-Verfolgung

```text
Rolle: Du zeichnest die Entwicklung eines Feldes nach.
Aufgabe: Ausgehend von der genannten Arbeit, nutze literature_map /
verwandte Arbeiten, um fruehere Grundlagen und spaetere Weiterentwicklungen
zu finden.
Ausgabe:
- "Baut auf" (Prior Works), 3-5 Arbeiten mit Link
- "Wurde weiterentwickelt in" (Derivative Works), 3-5 Arbeiten mit Link
- 1 Satz, wie sich das Feld ueber die Zeit verschoben hat
Regel: Keine Aussage ohne verlinkte Quelle.
```

!!! tip "Templates als Ausgabeformat"
    Du kannst dem GPT zusaetzlich ein festes Ausgabeformat vorgeben — etwa
    Markdown fuer dein [LLM-Wiki](../sammeln/llm-wiki.md) oder eine
    Struktur, die direkt nach [Notion](../sammeln/notion.md) /
    [Zotero](../sammeln/zotero.md) passt. So sind Funde sofort ablagefertig.

## Grenzen & Datenschutz

- Laeuft ueber ChatGPT (Cloud). Keine vertraulichen unveroeffentlichten
  Daten hochladen, ausser die institutionellen Vorgaben erlauben es.
- In den ChatGPT-Einstellungen pruefen, ob Eingaben zum Training genutzt
  werden.

## Offizielle Links

- Anleitung "Make a GPT": <https://docs.scholarai.io/make-a-gpt>
- ScholarAI: <https://scholarai.io>
