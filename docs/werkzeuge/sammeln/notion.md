---
werkzeug:
  schwierigkeit: Einsteiger
  kosten: Freemium
  verarbeitung: Cloud
  wofuer: Notizen und Datenbanken als Ablage, an ein LLM anbindbar
  phase: [verwalten]
  stand: August 2026
---

# Notion

Notion verbindet Notizen mit Datenbanken: Jede Seite kann Felder haben,
und über die Felder lassen sich Seiten filtern, sortieren und
gruppieren. Für die Forschung heisst das, Lesenotizen, Projektwissen und
Aufgaben in einer Struktur zu führen, die man später auswerten kann,
statt in einer Sammlung loser Dokumente.

Interessant wird es durch die Anbindung an ein LLM: Ein Modell kann
Funde direkt als Einträge anlegen, statt dass du sie abtippst.

## Wofür es taugt

- **Lesenotizen nach festem Schema ablegen**, mit denselben Feldern für
  jede Quelle, damit sich später über die Sammlung hinweg vergleichen
  lässt.
- **Als Ziel für automatisch erzeugte Zusammenfassungen dienen**, etwa
  aus dem Workflow
  [Vom Thema zur Literaturübersicht](../../workflows/thema-zu-uebersicht.md).
- **Projektwissen an einem Ort halten**, das nicht in die
  Literaturverwaltung gehört: Entscheidungen, offene Fragen, Notizen aus
  Besprechungen.

## An ein LLM anbinden

Notion betreibt seit 2026 einen eigenen **MCP-Server** (siehe
[Wie du ein LLM einspannst](../../grundlagen/llm-einspannen.md)). Die
Verbindung läuft über OAuth, für gängige Chat-Programme gibt es eine
Ein-Klick-Einrichtung. Das ist der einfachere Weg und ersetzt für die
meisten Zwecke die früher nötige Handarbeit mit selbst angelegten
Integrationen und Token.

Der ältere Weg über eine eigene Integration mit Zugriffs-Token besteht
weiter und ist dann sinnvoll, wenn ein Programm kein MCP spricht oder du
den Zugriff selbst programmieren willst.

## Grenzen

- **Der Zugriff ist breit.** Ein angebundenes Modell kann in deinem
  Arbeitsbereich lesen und schreiben wie du selbst. Die Berechtigungen
  von Notion gelten weiterhin, aber innerhalb davon gibt es keine
  Feinsteuerung pro Seite. Für Forschungsdaten heisst das: einen
  eigenen Arbeitsbereich oder eine eigene Seite für die Anbindung
  verwenden, nicht den ganzen Bestand freigeben.
- **Alles liegt in der Notion-Cloud.** Für die Einordnung siehe die
  [Grundregel zum Datenschutz](../../grundlagen/datenschutz.md).
- **Kein Literaturverwaltungsprogramm.** Notion kennt keine
  Zitierstile, erzeugt keine Bibliografien und schreibt nicht in Word.
  Dafür ist [Zotero](zotero.md) zuständig.
- **Bindung an einen Anbieter.** Die Inhalte lassen sich exportieren,
  aber Datenbanken und Verknüpfungen überstehen den Umzug nicht
  unverändert.

## Wann etwas anderes passt

Für Referenzen und Zitate ist [Zotero](zotero.md) das richtige Werkzeug,
Notion ergänzt es höchstens. Wenn das Wissen nicht nur abgelegt, sondern
vom Modell laufend verdichtet und verknüpft werden soll, ist das
[LLM-Wiki](llm-wiki.md) der passendere Ansatz, und es kommt ohne
Anbieterbindung aus, weil es aus Markdown-Dateien besteht.

Offizielle Seite: <https://www.notion.com> ·
MCP-Anbindung: <https://www.notion.com/help/notion-mcp> ·
API-Doku: <https://developers.notion.com>

---

Wenn das Wissen nicht nur abgelegt, sondern vom LLM gepflegt werden soll:
[LLM-Wiki nach Karpathy](llm-wiki.md).
