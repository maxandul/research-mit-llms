---
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: je nach Variante bis Fortgeschritten
  kosten: gratis
  wofuer: persistente, wachsende Wissensbasis
---

# LLM-Wiki (nach Karpathy)

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

## Ein Standard zeichnet sich ab: das Open Knowledge Format

Bisher hat jedes LLM-Wiki seine eigenen Konventionen erfunden. Im Juni 2026
hat Google Cloud dazu eine offene Spezifikation veröffentlicht, das
**Open Knowledge Format (OKF)**, im Juli 2026 gefolgt von Version 0.2. Sie
beschreibt genau das Muster, das Karpathy skizziert hat, in verbindlicher
Form: ein Verzeichnis von Markdown-Dateien, jede mit einem kleinen
YAML-Block am Anfang (Frontmatter), Querverweise als normale
Markdown-Links.

Pflicht ist dabei erstaunlich wenig: genau ein Feld, `type`. Alles Weitere
ist freiwillig, eigene Zusatzfelder sind ausdrücklich erlaubt, und Programme,
die OKF lesen, müssen unbekannte Felder und kaputte Links tolerieren. Ein
bestehendes Markdown-Wiki wird damit meist mit wenig Aufwand kompatibel,
ohne dass man seine Struktur aufgeben muss.

Interessanter als die Interoperabilität sind für Forschungszwecke die
Felder, die Version 0.2 ergänzt hat. Sie beantworten Fragen, die sich bei
LLM-gepflegten Notizen ohnehin stellen:

| Feld | Frage |
|------|-------|
| `sources` | Worauf stützt sich diese Notiz? |
| `generated` / `verified` | Wer hat das geschrieben, wer hat es geprüft? |
| `stale_after` | Ab wann ist die Notiz nachzuprüfen? |
| `status` | Ist sie vorläufig, aktuell oder überholt? |

Aus `verified` ergibt sich eine Vertrauensstufe: keine Angabe heisst
ungeprüft, eine Bestätigung durch eine Maschine heisst maschinell bestätigt,
eine Bestätigung durch einen Menschen heisst menschlich geprüft. Wer will,
kann sein Wiki so filtern, dass nur menschlich geprüfte Notizen in eine
Arbeit einfliessen.

!!! note "Wie neu das ist"
    OKF ist als Entwurf gekennzeichnet und wenige Wochen alt; zwischen v0.1
    und v0.2 wurden bereits zwei Felder umbenannt. Es ist ein Vorschlag mit
    Gewicht, kein etablierter Standard. Wer heute ein Wiki aufbaut, kann die
    Felder trotzdem übernehmen: Sie sind auch dann nützlich, wenn sich OKF
    nicht durchsetzt, weil sie die eigene Qualitätskontrolle maschinell
    prüfbar machen.

    Das [Forschungsstand-Wiki dieser Website](../../wiki/index.md) ist im
    Juli 2026 auf diese Felder umgestellt worden, ohne die Notizen selbst
    umzuschreiben. Wie das konkret aussieht, steht in
    [CLAUDE.md im Repository](https://github.com/maxandul/research-mit-llms/blob/main/CLAUDE.md).

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
- Open Knowledge Format, Spezifikation und Beispiel-Sammlungen:
  <https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf>
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
