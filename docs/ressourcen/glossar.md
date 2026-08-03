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
[Wie du ein LLM einspannst](../grundlagen/llm-einspannen.md).

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

**Frontmatter**: Block mit Metadaten am Anfang einer Markdown-Datei,
oben und unten durch drei Bindestriche abgetrennt. Hier stehen Angaben
wie Titel, Datum oder Schlagworte maschinenlesbar, ohne im Text
aufzutauchen.

**YAML**: Schreibweise für strukturierte Angaben nach dem Muster
Schlüssel, Doppelpunkt, Wert. Einrückung ersetzt Klammern. Wird für
Frontmatter und Konfigurationsdateien verwendet, etwa `mkdocs.yml`.

**ingest / query / lint**: Die drei Operationen eines LLM-Wikis: Quellen
einpflegen, Fragen stellen, Wissensbasis prüfen.

**OKF**: Open Knowledge Format, eine offene Spezifikation dafür, welche
Felder im Frontmatter eines LLM-Wikis stehen. Siehe
[Ein eigenes LLM-Wiki](../werkzeuge/sammeln/llm-wiki.md).

**Diarisierung**: Automatisches Erkennen und Unterscheiden von
Sprecher:innen in einer Audioaufnahme, wichtig bei der
[Transkription](../erheben/transkription.md) von Interviews.

**SRT**: Untertitelformat, das den Text in Blöcke mit Zeitstempeln
teilt. Transkriptionswerkzeuge geben es neben reinem Text aus; damit
lässt sich eine Textstelle im Audio wiederfinden.

**VTT**: Ebenfalls ein Untertitelformat mit Zeitstempeln (WebVTT),
etwas neuer als SRT und im Web verbreitet.

**Pseudonymisierung**: Ersetzen von Identifikatoren durch Platzhalter
(P01, Stadt B) mit einer lokal verwahrten Zuordnungstabelle. Rückgängig
machbar, darum rechtlich weiterhin Personendaten. Siehe
[Daten anonymisieren](../erheben/anonymisieren.md).

**Anonymisierung**: Entfernen des Personenbezugs, sodass er auch mit
Zusatzwissen nicht mehr herstellbar ist. Strenger als Pseudonymisierung.

**Codebuch**: Verzeichnis aller Codes einer qualitativen Auswertung, je
mit Definition, Ankerbeispiel und Abgrenzung. Grundlage für das
[Codieren mit LLMs](../analysieren/qualitativ-codieren.md).

**QDA-Software**: Programme für die qualitative Datenanalyse wie MAXQDA
oder ATLAS.ti, in denen Material codiert, geordnet und ausgewertet wird.

**COREQ**: Prüfliste mit 32 Punkten dafür, was ein Bericht über eine
qualitative Studie offenlegen soll (Consolidated Criteria for Reporting
Qualitative Research). Für LLM-gestütztes Codieren ist eine Erweiterung
"COREQ + LLM" vorgeschlagen worden, die Modell, Prompts und Prüfschritte
mitverlangt.

**Pandoc**: Freies Kommandozeilen-Werkzeug, das Dokumentformate
konvertiert, z. B. Markdown nach Word. Herzstück des Workflows
[Die Arbeit in Markdown aufbauen](../schreiben/arbeit-in-markdown.md).

**CSL**: Citation Style Language. Dateiformat für Zitierstile (etwa APA),
das Pandoc und Zotero nutzen, um Zitate und Literaturverzeichnisse
automatisch zu formatieren.

**APA**: Zitierstil der American Psychological Association, in den
Sozial- und Geisteswissenschaften weit verbreitet.

**MLA**: Zitierstil der Modern Language Association, vor allem in den
Sprach- und Literaturwissenschaften verbreitet.

**DOI**: Dauerhafte Kennung einer Publikation, die sich als Link
auflösen lässt und gültig bleibt, auch wenn die Verlagsseite umzieht.
Die zuverlässigste Art, eine Quelle eindeutig anzugeben.

**RIS**: Austauschformat für Literaturangaben, das die meisten
Fachdatenbanken exportieren und alle gängigen Literaturverwaltungen
einlesen.

**BIB**: Dateiendung für BibTeX, ein Textformat für Literaturangaben.
Wird vor allem zusammen mit LaTeX, Pandoc und Quarto verwendet.

**CSV**: Tabelle als reine Textdatei, eine Zeile pro Datensatz, die
Felder durch Komma oder Semikolon getrennt. Jedes Tabellenprogramm liest
sie, und sie lässt sich gut in einen Chat einfügen.

**TLDR**: Kurz für "too long, didn't read", also eine sehr knappe
Zusammenfassung. Auf Semantic Scholar bezeichnet TLDR die maschinell
erzeugte Ein-Satz-Zusammenfassung eines Papers.

**Freemium**: Preismodell mit kostenlosem Grundangebot und
kostenpflichtigen Zusatzfunktionen. Auf dieser Website eine der drei
Kostenstufen im Steckbrief oben auf den Werkzeugseiten.

**VRAM**: Arbeitsspeicher der Grafikkarte. Er begrenzt, wie gross ein
Modell sein darf, das lokal auf dem eigenen Rechner läuft.

**ICMJE**: Gremium von Herausgebern medizinischer Fachzeitschriften,
dessen Empfehlungen zu Autorschaft und Offenlegung weit über die Medizin
hinaus als Massstab gelten.

**COPE**: Committee on Publication Ethics, ein Zusammenschluss von
Verlagen und Zeitschriften, der Leitlinien zu Publikationsethik und zum
Umgang mit Fehlverhalten herausgibt.

**DSGVO**: Datenschutz-Grundverordnung der EU. Sie regelt, wie
Personendaten verarbeitet werden dürfen. In der Schweiz gilt
sinngemäss das revidierte Datenschutzgesetz (revDSG).

**RLHF**: Nachtraining eines Sprachmodells anhand menschlicher
Bewertungen (Reinforcement Learning from Human Feedback). Es prägt, wie
hilfsbereit und wie zustimmend ein Modell antwortet.
