# Drei Arten, LLMs zu nutzen

Es gibt drei grundlegend verschiedene Arten, ein LLM fuer Research zu nutzen.
Wer den Unterschied kennt, waehlt fuer jede Aufgabe das richtige Werkzeug.

## 1. Reiner Chat

Du stellst einem Modell (ChatGPT, Claude, Gemini ...) eine Frage und bekommst
eine Antwort aus dem Trainingswissen.

- **Staerke:** schnell, gut zum Brainstorming, Erklaeren, Formulieren.
- **Schwaeche:** das Modell kann veraltet sein, Quellen erfinden
  ("halluzinieren") und kennt deine eigenen Dokumente nicht.

## 2. Chat mit Werkzeugen (Tools / Actions / Connectors)

Das Modell kann waehrend des Gespraechs externe Dienste aufrufen — eine
Literaturdatenbank durchsuchen, ein PDF lesen, in deine Zotero-Bibliothek
schreiben. Genau das macht z.B. ein
[Custom GPT mit ScholarAI](../werkzeuge/dialog/scholarai.md).

- **Staerke:** aktuelle, belegbare Antworten mit echten Quellen; kann auf
  deine eigenen Daten zugreifen.
- **Schwaeche:** Einrichtung noetig; Qualitaet haengt von den angebundenen
  Quellen ab.

## 3. Persistente Wissensbasis (LLM-Wiki)

Statt bei jeder Frage neu zu suchen, baut das Modell eine *wachsende*,
verlinkte Sammlung von Notizen auf — siehe
[RAG vs. LLM-Wiki](rag-vs-wiki.md) und das
[LLM-Wiki nach Karpathy](../werkzeuge/sammeln/llm-wiki.md).

- **Staerke:** Wissen sammelt sich an, statt jedes Mal neu zusammengesucht
  zu werden; ideal fuer laengere Projekte.
- **Schwaeche:** mehr Pflege; je nach Variante etwas Technik noetig.

!!! note "Merksatz"
    Chat beantwortet eine Frage. Werkzeuge holen Belege dazu. Ein Wiki
    *behaelt* die Antworten und baut darauf auf.
