# Eigenes Forschungs-Wiki aufbauen

Über ein längeres Projekt eine wachsende, verlinkte Wissensbasis aufbauen,
statt Wissen bei jeder Frage neu zusammenzusuchen. Hintergrund:
[Wie du ein LLM einspannst](../grundlagen/llm-einspannen.md).

### Gelebtes Beispiel auf dieser Website

Der [Forschungsstand](../wiki/index.md) dieser Website ist ein solches
Wiki: Quellnotizen, Konzeptnotizen, Synthesen und ein automatisch
erzeugter Wissensgraph, sprintweise aufgebaut. Das zugehörige Schema
ist die [CLAUDE.md im Repository](https://github.com/maxandul/research-mit-llms/blob/main/CLAUDE.md);
kopierfertige Vorlagen stehen unter
[Wiki-Vorlagen](../ressourcen/wiki-vorlagen.md).

### Der Kreislauf

```
Quelle finden  ->  ingest (einpflegen)  ->  query (fragen)  ->  lint (prüfen)
                        ^                                          |
                        +------------------------------------------+
```

## Ziel

Eine persistente Markdown-Wissensbasis, die mit jeder Quelle reicher wird und
deren Pflege das LLM übernimmt.

## Beteiligte Werkzeuge

- [LLM-Wiki nach Karpathy](../werkzeuge/sammeln/llm-wiki.md) als Methode
  (wähle deine Stufe: händisch, Claude Cowork oder Coding-Agent)
- [llm-wiki](https://github.com/mehmetgoekce/llm-wiki) als fertiges Repo:
  Schema, Setup-Skript und `/wiki`-Befehle für Claude Code mit Obsidian oder Logseq
- eine Recherchequelle aus [Finden & Erkunden](../werkzeuge/finden/semantic-scholar.md)
- optional [Zotero](../werkzeuge/sammeln/zotero.md) als Referenzverwaltung,
  per MCP ans LLM angebunden: Referenzen und PDFs zitierfähig ablegen lassen
- optional [Obsidian](https://obsidian.md) zum Lesen und zur Graph-Ansicht

## Schritte

1. **Stufe wählen.** Klein anfangen ist völlig in Ordnung; die händische
   Stufe reicht zum Start und lässt sich später automatisieren.
2. **Struktur anlegen.** Ein Ordner mit ein paar Startdateien genügt (siehe
   Vorschlag unten).
3. **Schema festlegen.** In einer Anleitungsdatei beschreiben, wie das Wiki
   aufgebaut ist und wie neue Quellen eingepflegt werden (siehe Beispiel).
4. **ingest (einpflegen).** Eine Quelle nach der anderen: lesen lassen,
   zusammenfassen, in vorhandene Seiten einarbeiten, Querverweise setzen,
   die Referenz ablegen (optional per [Zotero-MCP](../werkzeuge/sammeln/zotero.md),
   damit Zitat und Literaturverzeichnis später automatisch entstehen), eine
   Zeile ins Log schreiben.
5. **query (fragen).** Fragen an das Wiki stellen. Gute Antworten als neue
   Seite zurückschreiben, damit sich Erkenntnisse anhäufen.
6. **lint (prüfen).** Regelmässig auf Widersprüche, veraltete Stellen,
   verwaiste Seiten und Lücken prüfen lassen.

## Vorschlag: Ordnerstruktur

```text
mein-wiki/
├── CLAUDE.md          # das Schema (Spielregeln fürs LLM)
├── index.md           # Inhaltsverzeichnis, eine Zeile pro Seite
├── log.md             # chronologisches Protokoll der Änderungen
├── raw/               # Originalquellen (unverändert)
└── wiki/              # die gepflegten Markdown-Seiten
    ├── themen/
    └── konzepte/
```

## Vorschlag: Schema-Datei (Auszug für `CLAUDE.md`)

```markdown
# Spielregeln für dieses Wiki

## Aufbau
- Originalquellen liegen unverändert in raw/ und werden nie geändert.
- Gepflegte Seiten liegen in wiki/. Querverweise als [[Seitenname]].

## Beim Einpflegen einer Quelle (ingest)
1. Quelle lesen, Kernpunkte mit mir besprechen.
2. Eine Zusammenfassungsseite in wiki/ anlegen.
3. Betroffene Themen- und Konzeptseiten aktualisieren.
4. index.md ergänzen, eine Zeile ans log.md anhängen.

## Beim Prüfen (lint)
- Widersprüche zwischen Seiten markieren, nicht stillschweigend glätten.
- Veraltete Aussagen kennzeichnen, verwaiste Seiten melden.

## Log-Format
- Jede Zeile beginnt mit: ## [JJJJ-MM-TT] ingest | Titel
```

**Erst klein, dann automatisieren.** Starte von Hand mit fünf Quellen. Wenn der Nutzen sichtbar ist und die
Handarbeit nervt, wechsle auf [Claude Cowork oder einen
Coding-Agenten](../werkzeuge/sammeln/llm-wiki.md), oder nutze direkt das
[llm-wiki-Repo](https://github.com/mehmetgoekce/llm-wiki) mit vorgefertigtem
Schema und ingest/query/lint-Befehlen.

---

Damit ist die Literatur versorgt. Weiter im Forschungsprozess: eigene
Daten erheben, beginnend mit
[Interviews transkribieren](../erheben/transkription.md).
