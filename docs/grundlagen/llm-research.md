# Drei Arten, LLMs zu nutzen

Es gibt drei grundlegend verschiedene Arten, ein LLM für die Forschung zu
nutzen. Wer den Unterschied kennt, wählt für jede Aufgabe das richtige
Werkzeug.

## 1. Reiner Chat

Du stellst einem Modell (ChatGPT, Claude, Gemini ...) eine Frage und bekommst
eine Antwort aus dem Trainingswissen.

- **Stärke:** schnell, gut zum Brainstorming, Erklären, Formulieren.
- **Schwäche:** das Modell kann veraltet sein, Quellen erfinden
  ("halluzinieren") und kennt deine eigenen Dokumente nicht.

## 2. Chat mit Werkzeugen (Tools / Actions / Connectors)

Das Modell kann während des Gesprächs externe Dienste aufrufen: eine
Literaturdatenbank durchsuchen, ein PDF lesen, in deine Zotero-Bibliothek
schreiben. Genau das macht z.B. ein
[Custom GPT mit ScholarAI](../werkzeuge/dialog/scholarai.md). Auch die
Code-Ausführung beim [quantitativen Auswerten](../analysieren/quantitativ-auswerten.md)
gehört in diese Kategorie: Das Modell ruft ein Werkzeug (die
Programmier-Umgebung) auf, statt selbst zu "rechnen".

- **Stärke:** aktuelle, belegbare Antworten mit echten Quellen; kann auf
  deine eigenen Daten zugreifen und verlässlich rechnen.
- **Schwäche:** Einrichtung nötig; Qualität hängt von den angebundenen
  Quellen ab.

## 3. Persistente Wissensbasis (LLM-Wiki)

Statt bei jeder Frage neu zu suchen, baut das Modell eine *wachsende*,
verlinkte Sammlung von Notizen auf, siehe
[RAG vs. LLM-Wiki](rag-vs-wiki.md) und das
[LLM-Wiki nach Karpathy](../werkzeuge/sammeln/llm-wiki.md).

- **Stärke:** Wissen sammelt sich an, statt jedes Mal neu zusammengesucht
  zu werden; ideal für längere Projekte.
- **Schwäche:** mehr Pflege; je nach Variante etwas Technik nötig.

---

Wie sich Ansatz 2 und 3 technisch unterscheiden und wann welcher passt,
klärt die nächste Seite: [Kontext, RAG & LLM-Wiki](rag-vs-wiki.md).
