# Glossar

**LLM**: Grosses Sprachmodell (Large Language Model), z.B. hinter ChatGPT,
Claude oder Gemini.

**Token**: Wortbaustein von wenigen Zeichen, in die ein LLM allen Text
zerlegt. Kontextfenster und Kosten werden in Tokens gemessen. Siehe
[Wie ein LLM arbeitet](../grundlagen/wie-llms-arbeiten.md).

**Kontextfenster**: Die Textmenge, die ein Modell pro Anfrage "gleichzeitig
sehen" kann (Frage, Verlauf und hochgeladene Inhalte zusammen). Ist es voll,
passt nichts mehr hinein.

**Kontext / Datei in den Chat laden**: Einen Text direkt ins Kontextfenster
geben, sodass das Modell ihn komplett liest. Kein Embedding, kein Abruf. Siehe
[Datei in den Chat, RAG oder LLM-Wiki?](../grundlagen/rag-vs-wiki.md).

**Embedding**: Die Umwandlung von Text in einen Zahlenvektor, sodass sich
inhaltlich ähnliche Texte rechnerisch finden lassen. Grundlage von RAG.

**RAG**: Retrieval-Augmented Generation. Dokumente werden zerstückelt,
als Embeddings gespeichert und bei jeder Frage werden nur die passendsten
Stücke abgerufen und ins Kontextfenster gegeben. Im Gegensatz zum direkten
Laden (oben) sieht das Modell nie das ganze Dokument.

**Custom GPT**: Ein selbst konfigurierter GPT in ChatGPT, optional mit
"Actions" zu externen Diensten.

**Action / Connector / Tool**: Eine Anbindung, über die ein LLM externe
Dienste aufruft (suchen, lesen, schreiben).

**MCP (Model Context Protocol)**: Offener Standard, der solche Anbindungen
vereinheitlicht: Ein MCP-Server stellt einem LLM die Funktionen eines
Dienstes (etwa Zotero) als Werkzeuge bereit, unabhängig vom verwendeten
Chat-Programm. Siehe das Praxisbeispiel auf
[Zotero](../werkzeuge/sammeln/zotero.md).

**API**: Schnittstelle, über die Programme miteinander sprechen. Oft mit
einem "API-Key" (Zugangsschlüssel) abgesichert.

**Markdown**: Einfaches Textformat mit leichter Formatierung. Grundlage von
LLM-Wikis und dieser Seite. Siehe
[Markdown als Arbeitsformat](../grundlagen/markdown-arbeitsformat.md).

**ingest / query / lint**: Die drei Operationen eines LLM-Wikis: Quellen
einpflegen, Fragen stellen, Wissensbasis prüfen.

**Diarisierung**: Automatisches Erkennen und Unterscheiden von
Sprecher:innen in einer Audioaufnahme, wichtig bei der
[Transkription](../erheben/transkription.md) von Interviews.

**Pseudonymisierung**: Ersetzen von Identifikatoren durch Platzhalter
(P01, Stadt B) mit einer lokal verwahrten Zuordnungstabelle. Rückgängig
machbar, darum rechtlich weiterhin Personendaten. Siehe
[Daten anonymisieren](../erheben/anonymisieren.md).

**Anonymisierung**: Entfernen des Personenbezugs, sodass er auch mit
Zusatzwissen nicht mehr herstellbar ist. Strenger als Pseudonymisierung.

**Codebuch**: Verzeichnis aller Codes einer qualitativen Auswertung, je
mit Definition, Ankerbeispiel und Abgrenzung. Grundlage für das
[Codieren mit LLMs](../analysieren/qualitativ-codieren.md).

**Pandoc**: Freies Kommandozeilen-Werkzeug, das Dokumentformate
konvertiert, z. B. Markdown nach Word. Herzstück des Workflows
[Die Arbeit in Markdown aufbauen](../schreiben/arbeit-in-markdown.md).

**CSL**: Citation Style Language. Dateiformat für Zitierstile (etwa APA),
das Pandoc und Zotero nutzen, um Zitate und Literaturverzeichnisse
automatisch zu formatieren.
