# Zotero

!!! info "Auf einen Blick"
    **Schwierigkeit:** Einsteiger · **Kosten:** gratis (Speicher-Abo optional) · **Wofür:** Literaturverwaltung

## Was ist es?

Ein kostenloses, offenes Literaturverwaltungsprogramm. Sammelt Referenzen
und PDFs, erstellt Zitate und Bibliografien. Über die Web API lässt sich
die eigene Bibliothek auch von anderen Werkzeugen (z.B. einem Custom GPT)
auslesen und befüllen.

## Was bringt es für Research?

- Zentrale, durchsuchbare Ablage aller Quellen.
- Per MCP an ein LLM anbindbar: Funde automatisch und zitierfähig ablegen
  lassen (siehe [An ein LLM anbinden (MCP)](#an-ein-llm-anbinden-mcp) unten).
- Liefert (mit dem Plugin Better BibTeX) die Literaturdatenbank für den
  Schreib-Workflow
  [Die Arbeit in Markdown aufbauen](../../schreiben/arbeit-in-markdown.md):
  Zitate und Literaturverzeichnis entstehen dann automatisch beim
  Word-Export.

## Voraussetzungen

- Zotero-Konto (gratis). Für die API: ein API-Schlüssel aus den
  Kontoeinstellungen.

## Einrichtung / Nutzung (High-Level)

1. Zotero installieren, Konto anlegen.
2. Für die Anbindung: in den Einstellungen einen API-Key erzeugen und die
   eigene User- bzw. Group-ID notieren.
3. Den Key im anbindenden Werkzeug hinterlegen.

## An ein LLM anbinden (MCP)

Über einen MCP-Server lässt sich die Zotero-Bibliothek direkt an ein LLM
anbinden: Das Modell liest dann Sammlungen und legt neue Einträge samt PDF
selbst ab. Auf dieser Website ist das gelebte Praxis, der
[Forschungsstand](../../wiki/index.md) verwaltet seine Quellen so.

Ein bewährter Weg (Claude Desktop unter Windows): den Server
[zotero-mcp](https://github.com/54yyyu/zotero-mcp) installieren und mit dem
Web-API-Key einrichten. Das Modell erhält so Lese- und Schreibzugriff auf
eine dedizierte Sammlung, in die es einpflegt, nie sonst in die Bibliothek.

**Sauber einpflegen (Hybrid nach Quelltyp):** Damit die Einträge
zitierfähig sind, führt die Referenz, nicht die lokale Datei.

- arXiv-Preprint über die arXiv-URL anlegen: liefert Titel, Autoren,
  Abstract, arXiv-ID und PDF.
- Veröffentlichten Artikel über die DOI anlegen: liefert saubere
  CrossRef-Metadaten und, wo verfügbar, ein Open-Access-PDF (via Unpaywall).
- Nur wenn weder DOI noch arXiv greifen: das lokale PDF importieren und die
  Metadaten von Hand nachtragen. Ein reiner Datei-Import erzeugt sonst nur
  einen leeren Eintrag ohne brauchbare Angaben.

!!! warning "API-Key lokal halten"
    Der Zotero-API-Key gehört in die lokale Konfiguration des anbindenden
    Werkzeugs, nie in ein öffentliches Repository. Die Schreibrechte bewusst
    auf eine eigene Sammlung beschränken.

## Grenzen & Datenschutz

- Bibliotheksdaten liegen bei Zotero (sofern synchronisiert). PDFs mit
  vertraulichem Inhalt bewusst handhaben.

## Offizielle Links

- Website: <https://www.zotero.org>
- Web API v3: <https://www.zotero.org/support/dev/web_api/v3/start>

---

Für Notizen und strukturierte Wissensdatenbanken neben den reinen
Referenzen: [Notion](notion.md).
