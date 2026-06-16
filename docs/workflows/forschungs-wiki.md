# Eigenes Forschungs-Wiki aufbauen

Ueber ein laengeres Projekt eine wachsende, verlinkte Wissensbasis aufbauen,
statt Wissen bei jeder Frage neu zusammenzusuchen. Hintergrund:
[RAG vs. LLM-Wiki](../grundlagen/rag-vs-wiki.md).

!!! abstract "Der Kreislauf"
    ```
    Quelle finden  ->  ingest (einpflegen)  ->  query (fragen)  ->  lint (pruefen)
                            ^                                          |
                            +------------------------------------------+
    ```

## Ziel

Eine persistente Markdown-Wissensbasis, die mit jeder Quelle reicher wird und
deren Pflege das LLM uebernimmt.

## Beteiligte Werkzeuge

- [LLM-Wiki nach Karpathy](../werkzeuge/sammeln/llm-wiki.md) als Methode
  (waehle deine Stufe: haendisch, Claude Cowork oder Coding-Agent)
- eine Recherchequelle aus [Finden & Erkunden](../werkzeuge/finden/semantic-scholar.md)
- optional [Obsidian](https://obsidian.md) zum Lesen und zur Graph-Ansicht

## Schritte

1. **Stufe waehlen.** Klein anfangen ist voellig in Ordnung — die haendische
   Stufe reicht zum Start und laesst sich spaeter automatisieren.
2. **Struktur anlegen.** Ein Ordner mit ein paar Startdateien genuegt (siehe
   Vorschlag unten).
3. **Schema festlegen.** In einer Anleitungsdatei beschreiben, wie das Wiki
   aufgebaut ist und wie neue Quellen eingepflegt werden (siehe Beispiel).
4. **ingest — einpflegen.** Eine Quelle nach der anderen: lesen lassen,
   zusammenfassen, in vorhandene Seiten einarbeiten, Querverweise setzen,
   eine Zeile ins Log schreiben.
5. **query — fragen.** Fragen an das Wiki stellen. Gute Antworten als neue
   Seite zurueckschreiben, damit sich Erkenntnisse anhaeufen.
6. **lint — pruefen.** Regelmaessig auf Widersprueche, veraltete Stellen,
   verwaiste Seiten und Luecken pruefen lassen.

## Vorschlag: Ordnerstruktur

```text
mein-wiki/
├── CLAUDE.md          # das Schema (Spielregeln fuers LLM)
├── index.md           # Inhaltsverzeichnis, eine Zeile pro Seite
├── log.md             # chronologisches Protokoll der Aenderungen
├── raw/               # Originalquellen (unveraendert)
└── wiki/              # die gepflegten Markdown-Seiten
    ├── themen/
    └── konzepte/
```

## Vorschlag: Schema-Datei (Auszug fuer `CLAUDE.md`)

```markdown
# Spielregeln fuer dieses Wiki

## Aufbau
- Originalquellen liegen unveraendert in raw/ und werden nie geaendert.
- Gepflegte Seiten liegen in wiki/. Querverweise als [[Seitenname]].

## Beim Einpflegen einer Quelle (ingest)
1. Quelle lesen, Kernpunkte mit mir besprechen.
2. Eine Zusammenfassungsseite in wiki/ anlegen.
3. Betroffene Themen- und Konzeptseiten aktualisieren.
4. index.md ergaenzen, eine Zeile ans log.md anhaengen.

## Beim Pruefen (lint)
- Widersprueche zwischen Seiten markieren, nicht stillschweigend glaetten.
- Veraltete Aussagen kennzeichnen, verwaiste Seiten melden.

## Log-Format
- Jede Zeile beginnt mit: ## [JJJJ-MM-TT] ingest | Titel
```

!!! tip "Erst klein, dann automatisieren"
    Starte von Hand mit fuenf Quellen. Wenn der Nutzen sichtbar ist und die
    Handarbeit nervt, wechsle auf [Claude Cowork oder einen
    Coding-Agenten](../werkzeuge/sammeln/llm-wiki.md).

!!! note "Noch zu ergaenzen"
    Dein angepasstes Schema und ein Beispiel aus deinem eigenen Wiki.
