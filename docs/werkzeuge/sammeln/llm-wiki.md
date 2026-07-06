# LLM-Wiki (nach Karpathy)

!!! info "Auf einen Blick"
    **Schwierigkeit:** Einsteiger bis Fortgeschritten (je nach Variante) · **Kosten:** gratis · **Wofür:** persistente, wachsende Wissensbasis

## Was ist es?

Eine Arbeitsweise (kein einzelnes Programm): Statt bei jeder Frage neu zu
suchen, pflegt ein LLM eine wachsende Sammlung verlinkter Markdown-Notizen.
Hintergrund: [RAG vs. LLM-Wiki](../../grundlagen/rag-vs-wiki.md).

Die Architektur hat drei Schichten:

- **Raw / Quellen**: deine unveränderten Originaldokumente.
- **Wiki**: die vom LLM gepflegten, verlinkten Markdown-Seiten.
- **Schema**: eine Anleitungsdatei (z.B. `CLAUDE.md`), die festlegt, wie
  das Wiki strukturiert ist und wie neue Quellen eingepflegt werden.

## Drei Umsetzungsvarianten

Du kannst klein und ganz ohne Technik starten und später automatisieren.

=== "Stufe 1: Händisch (Einsteiger)"

    Keine API, kein Spezial-Tool nötig.

    - Lege einen Ordner mit Markdown-Dateien an (z.B. in Obsidian oder
      direkt im GitHub-Repo).
    - Kopiere Quelltexte in ein normales Chat-LLM und lass dir
      Zusammenfassungen und Querverweise erzeugen.
    - Füge die Ergebnisse selbst als `.md`-Seiten ein und verlinke sie.

    *Gewinn:* du verstehst das Prinzip und hast sofort Ergebnisse.
    *Aufwand:* das Einpflegen machst du von Hand.

=== "Stufe 2: Claude Cowork (Mittel)"

    Eine agentische Anwendung für Wissensarbeit, gedacht auch für
    Nicht-Entwickler:innen.

    - Der Agent übernimmt das Lesen, Zusammenfassen und Einpflegen
      halb-automatisch.
    - Du kuratierst Quellen und stellst Fragen; die Pflege läuft mit.

    *Gewinn:* deutlich weniger Handarbeit als Stufe 1.
    *Aufwand:* etwas Einrichtung, kein Programmieren nötig.

=== "Stufe 3: Claude Code / eigener Aufbau (Fortgeschritten)"

    Volle Automatisierung mit einem Coding-Agenten.

    - Der ganze Kreislauf *ingest -> query -> lint* läuft automatisiert.
    - Optional eigene Such-Tools, MCP-Anbindung, Skripte.
    - Fertiger Einstieg: [llm-wiki von Goekce](https://github.com/mehmetgoekce/llm-wiki)
      mit Schema, Setup und `/wiki`-Befehlen.

    *Gewinn:* maximale Leistung, sehr grosse Wissensbasen pflegbar.
    *Aufwand:* am höchsten; Programmierkenntnisse hilfreich.

## Voraussetzungen

- Stufe 1: nur ein Chat-LLM und ein Texteditor (Obsidian empfohlen).
- Stufe 2: Claude Cowork.
- Stufe 3: ein Coding-Agent (z.B. Claude Code), Grundkenntnisse Terminal.

## Grenzen & Datenschutz

- Inhalte gehen durch ein LLM: bei Cloud-Modellen Datenschutz beachten,
  bei sensiblen Daten lokale Modelle erwägen.
- Risiko von Fehlern in den Notizen: regelmässig prüfen ("lint").

## Offizielle Links

- Karpathys Original-Idee:
  <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Goekce, fertige Umsetzung mit Claude Code (L1/L2-Architektur, Obsidian/Logseq):
  <https://github.com/mehmetgoekce/llm-wiki>
- Obsidian (Markdown-Editor): <https://obsidian.md>

## Weiterführend

- Gelebtes Beispiel: der [Forschungsstand dieser Website](../../wiki/index.md)
  ist ein solches Wiki (Quellnotizen + Synthesen, öffentlich einsehbar)
- Workflow: [Eigenes Forschungs-Wiki aufbauen](../../workflows/forschungs-wiki.md)
- Praxis-Repo: [llm-wiki von Mehmet Goekce](https://github.com/mehmetgoekce/llm-wiki)
  mit Schema, Setup-Skript und Befehlen `/wiki ingest`, `/wiki query`, `/wiki lint`

---

Was es sonst noch gibt, von Research Rabbit bis scite.ai:
[Weitere Tools im Überblick](../weitere-tools.md).
