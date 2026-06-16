# Glossar

**LLM** — Grosses Sprachmodell (Large Language Model), z.B. hinter ChatGPT,
Claude oder Gemini.

**Kontextfenster** — Die Textmenge, die ein Modell pro Anfrage "gleichzeitig
sehen" kann (Frage, Verlauf und hochgeladene Inhalte zusammen). Ist es voll,
passt nichts mehr hinein.

**Kontext / Datei in den Chat laden** — Einen Text direkt ins Kontextfenster
geben, sodass das Modell ihn komplett liest. Kein Embedding, kein Abruf. Siehe
[Datei in den Chat, RAG oder LLM-Wiki?](../grundlagen/rag-vs-wiki.md).

**Embedding** — Die Umwandlung von Text in einen Zahlenvektor, sodass sich
inhaltlich aehnliche Texte rechnerisch finden lassen. Grundlage von RAG.

**RAG** — Retrieval-Augmented Generation. Dokumente werden zerstueckelt,
als Embeddings gespeichert und bei jeder Frage werden nur die passendsten
Stuecke abgerufen und ins Kontextfenster gegeben. Im Gegensatz zum direkten
Laden (oben) sieht das Modell nie das ganze Dokument.

**Custom GPT** — Ein selbst konfigurierter GPT in ChatGPT, optional mit
"Actions" zu externen Diensten.

**Action / Connector / Tool** — Eine Anbindung, ueber die ein LLM externe
Dienste aufruft (suchen, lesen, schreiben).

**API** — Schnittstelle, ueber die Programme miteinander sprechen. Oft mit
einem "API-Key" (Zugangsschluessel) abgesichert.

**Markdown** — Einfaches Textformat mit leichter Formatierung. Grundlage von
LLM-Wikis und dieser Seite.

**ingest / query / lint** — Die drei Operationen eines LLM-Wikis: Quellen
einpflegen, Fragen stellen, Wissensbasis pruefen.
