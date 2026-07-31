---
werkzeug:
  schwierigkeit: Einsteiger
  kosten: Freemium
  wofuer: Notizen und Datenbanken als Wissensbasis
---

# Notion

## Was ist es?

Ein flexibles Notiz- und Datenbank-Werkzeug. Per API lässt sich Notion an
einen LLM-Workflow anbinden, etwa damit ein Custom GPT Zusammenfassungen
direkt als Einträge in einer Notion-Datenbank ablegt.

## Was bringt es für Research?

- Strukturierte Ablage von Notizen, Lesenotizen, Projektwissen.
- Als Ziel für automatisch generierte Zusammenfassungen.

## Voraussetzungen

- Notion-Konto. Für die Anbindung: eine eigene "Integration" mit Token.

## Einrichtung / Nutzung (High-Level)

1. Konto und gewünschte Datenbank/Seiten anlegen.
2. Unter den Entwickler-Einstellungen eine Integration erstellen, Token kopieren.
3. Die Ziel-Datenbank für die Integration freigeben.
4. Token im anbindenden Werkzeug hinterlegen.

## Grenzen & Datenschutz

- Inhalte liegen in der Notion-Cloud. Sensible Daten entsprechend behandeln.

## Offizielle Links

- Produkt/Entwickler: <https://www.notion.com/product/dev>
- API-Doku: <https://developers.notion.com>

---

Wenn das Wissen nicht nur abgelegt, sondern vom LLM gepflegt werden soll:
[LLM-Wiki nach Karpathy](llm-wiki.md).
