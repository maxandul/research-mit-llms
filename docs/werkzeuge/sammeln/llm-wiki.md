# LLM-Wiki (nach Karpathy)

!!! info "Auf einen Blick"
    **Schwierigkeit:** Einsteiger bis Fortgeschritten (je nach Variante) · **Kosten:** gratis · **Wofuer:** persistente, wachsende Wissensbasis

## Was ist es?

Eine Arbeitsweise (kein einzelnes Programm): Statt bei jeder Frage neu zu
suchen, pflegt ein LLM eine wachsende Sammlung verlinkter Markdown-Notizen.
Hintergrund: [RAG vs. LLM-Wiki](../../grundlagen/rag-vs-wiki.md).

Die Architektur hat drei Schichten:

- **Raw / Quellen** — deine unveraenderten Originaldokumente.
- **Wiki** — die vom LLM gepflegten, verlinkten Markdown-Seiten.
- **Schema** — eine Anleitungsdatei (z.B. `CLAUDE.md`), die festlegt, wie
  das Wiki strukturiert ist und wie neue Quellen eingepflegt werden.

## Drei Umsetzungsvarianten

Du kannst klein und ganz ohne Technik starten und spaeter automatisieren.

=== "Stufe 1 — Haendisch (Einsteiger)"

    Keine API, kein Spezial-Tool noetig.

    - Lege einen Ordner mit Markdown-Dateien an (z.B. in Obsidian oder
      direkt im GitHub-Repo).
    - Kopiere Quelltexte in ein normales Chat-LLM und lass dir
      Zusammenfassungen und Querverweise erzeugen.
    - Fuege die Ergebnisse selbst als `.md`-Seiten ein und verlinke sie.

    *Gewinn:* du verstehst das Prinzip und hast sofort Ergebnisse.
    *Aufwand:* das Einpflegen machst du von Hand.

=== "Stufe 2 — Claude Cowork (Mittel)"

    Eine agentische Anwendung fuer Wissensarbeit, gedacht auch fuer
    Nicht-Entwickler:innen.

    - Der Agent uebernimmt das Lesen, Zusammenfassen und Einpflegen
      halb-automatisch.
    - Du kuratierst Quellen und stellst Fragen; die Pflege laeuft mit.

    *Gewinn:* deutlich weniger Handarbeit als Stufe 1.
    *Aufwand:* etwas Einrichtung, kein Programmieren noetig.

=== "Stufe 3 — Claude Code / eigener Aufbau (Fortgeschritten)"

    Volle Automatisierung mit einem Coding-Agenten.

    - Der ganze Kreislauf *ingest -> query -> lint* laeuft automatisiert.
    - Optional eigene Such-Tools, MCP-Anbindung, Skripte.

    *Gewinn:* maximale Leistung, sehr grosse Wissensbasen pflegbar.
    *Aufwand:* am hoechsten; Programmierkenntnisse hilfreich.

## Voraussetzungen

- Stufe 1: nur ein Chat-LLM und ein Texteditor (Obsidian empfohlen).
- Stufe 2: Claude Cowork.
- Stufe 3: ein Coding-Agent (z.B. Claude Code), Grundkenntnisse Terminal.

## Grenzen & Datenschutz

- Inhalte gehen durch ein LLM — bei Cloud-Modellen Datenschutz beachten,
  bei sensiblen Daten lokale Modelle erwaegen.
- Risiko von Fehlern in den Notizen: regelmaessig pruefen ("lint").

## Offizielle Links

- Karpathys Original-Idee:
  <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Obsidian (Markdown-Editor): <https://obsidian.md>

!!! note "Noch zu ergaenzen"
    Verweis auf den Workflow
    [Eigenes Forschungs-Wiki aufbauen](../../workflows/forschungs-wiki.md)
    sowie ein eigenes Beispiel.
