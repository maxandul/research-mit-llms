---
title: Coding-Agenten (Claude Code, Cursor)
werkzeug:
  schwierigkeit: Profi
  schwierigkeit_zusatz: Terminal und Dateiablage, keine Programmierkenntnisse zwingend
  kosten: kostenpflichtig
  kosten_zusatz: über ein Abo des jeweiligen Anbieters
  verarbeitung: Cloud
  verarbeitung_zusatz: Dateien liegen lokal, die Verarbeitung läuft beim Anbieter
  wofuer: Ein Modell arbeitet direkt auf deinen Dateien, mit sichtbaren Änderungen
  phase: [analysieren, schreiben, verwalten]
  stand: August 2026
---

# Coding-Agenten (Claude Code, Cursor)

Ein Coding-Agent ist ein Modell, das nicht in einem Chatfenster
antwortet, sondern auf deinen Dateien arbeitet: liest, ändert, legt
neue an, führt Skripte aus. Der Name führt in die Irre, denn für die
Forschung ist der interessante Teil selten das Programmieren, sondern
dass Arbeit über viele Dateien hinweg zuverlässig abgearbeitet wird.

Die bekanntesten sind **Claude Code** (Anthropic) und **Cursor**. Beide
brauchen ein Abo, beide zeigen jede Änderung als Unterschied an, bevor
oder nachdem sie passiert.

## Wofür es taugt

- **Vollständigkeit erzwingen.** Statt darauf zu hoffen, dass ein
  Modell alle 200 Tabellenzeilen bearbeitet, lässt ein Agent ein Skript
  darüber laufen, das jede Zeile einzeln vorlegt. Das ist der
  verlässliche Weg beim
  [qualitativen Codieren](../../analysieren/qualitativ-codieren.md).
- **Feedback über viele Dateien einarbeiten**, mit sichtbarem
  Unterschied pro Änderung, siehe
  [Mit Word-Feedback umgehen](../../schreiben/word-feedback.md).
- **Ein Wiki pflegen.** Die dritte Stufe des
  [LLM-Wikis](../sammeln/llm-wiki.md) beruht darauf: Der Agent liest
  neue Quellen, trägt sie ein und prüft die Struktur nach Regeln, die
  in einer Anleitungsdatei stehen.
- **Werkzeugketten einrichten.** Fehlermeldungen bei Pandoc, CUDA oder
  einem MCP-Server sind eine Aufgabe, bei der ein Agent schneller ans
  Ziel kommt als eine Websuche.

## Grenzen

- **Der Agent sieht deine Dateien.** Was im Arbeitsverzeichnis liegt,
  kann gelesen und an den Anbieter übertragen werden. Für Verzeichnisse
  mit Interviewmaterial gilt die
  [Grundregel zum Datenschutz](../../grundlagen/datenschutz.md)
  besonders deutlich, weil der Zugriff nicht dateiweise erfolgt.
- **Er ändert Dinge.** Ohne Versionsverwaltung ist eine falsche
  Änderung schwer rückgängig zu machen. Git ist hier keine Kür.
- **Kostenpflichtig**, und die Kosten hängen an der Nutzung.
- **Die Einstiegshürde liegt beim Terminal**, nicht beim Programmieren.
  Wer nie eine Kommandozeile geöffnet hat, braucht einen Nachmittag.
- **Die Prüfpflicht wächst mit dem Tempo.** Ein Agent, der zwanzig
  Dateien ändert, produziert zwanzig Änderungen zum Nachsehen.

## Wann etwas anderes passt

Für einzelne Texte und Fragen ist ein normales Chat-Werkzeug einfacher
und billiger. Für Literaturarbeit sind die Werkzeuge unter
[Literatur finden](../finden/semantic-scholar.md) und
[befragen](../dialog/scholarai.md) näher an der Aufgabe. Ein
Coding-Agent lohnt sich, sobald dieselbe Operation auf vielen Dateien
wiederholt werden muss.

Claude Code: <https://claude.com/product/claude-code> ·
Cursor: <https://cursor.com>

!!! randnotiz "Interessenlage"
    Diese Website wird selbst mit Cursor und einer agentischen
    Anwendung von Anthropic gepflegt, siehe
    [Über diese Website](../../ueber.md). Die Einschätzung hier stammt
    also aus der eigenen Nutzung und nicht aus einem Vergleich mehrerer
    Werkzeuge.

---

Wie sich das in einen durchgängigen Ablauf fügt, zeigt
[Eigenes Forschungs-Wiki aufbauen](../../workflows/forschungs-wiki.md).
