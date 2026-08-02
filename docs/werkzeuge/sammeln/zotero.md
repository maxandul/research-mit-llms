---
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: LLM-Anbindung bis Profi
  kosten: gratis
  kosten_zusatz: Speicher-Abo nur für die Synchronisierung von PDFs
  verarbeitung: beides
  verarbeitung_zusatz: lokal nutzbar, Synchronisierung optional
  wofuer: Referenzen und PDFs verwalten, Zitate und Bibliografien erzeugen
  phase: [verwalten, schreiben]
  stand: August 2026
---

# Zotero

Zotero sammelt Referenzen und PDFs, erzeugt daraus Zitate und
Bibliografien und schreibt sie in Word, LibreOffice oder Google Docs.
Es ist quelloffen und ein Projekt der Non-Profit-Organisation Digital
Scholar, also nicht von einem Anbieter abhängig, der es abschalten
könnte.

Für diese Website ist Zotero doppelt relevant: als Ablage der Literatur
und als Datenquelle beim
[Schreiben in Markdown](../../schreiben/arbeit-in-markdown.md), wo
Zitierschlüssel und Literaturverzeichnis automatisch aus der Bibliothek
kommen.

## Wofür es taugt

- **Quellen mit einem Klick erfassen.** Die Browser-Erweiterung liest
  Metadaten und PDF direkt von der Verlagsseite.
- **Zitieren im Textverarbeitungsprogramm.** Die Plugins für Word,
  LibreOffice und Google Docs sind mitgeliefert, Zitierstil umstellbar.
- **Die Bibliografie für den Markdown-Weg liefern.** Mit dem Plugin
  Better BibTeX entsteht eine `.bib`-Datei, die Pandoc beim Word-Export
  auswertet.
- **Von einem LLM befüllen lassen**, siehe unten. So entsteht der
  [Forschungsstand](../../wiki/index.md) dieser Website.

## An ein LLM anbinden (MCP)

Über einen MCP-Server lässt sich die Zotero-Bibliothek direkt an ein LLM
anbinden: Das Modell liest Sammlungen und legt neue Einträge samt PDF
selbst ab.

**Custom GPT Action oder MCP-Server?** Beide nutzen im Kern die Zotero
Web API, unterscheiden sich aber in drei Punkten:

- **Einrichtung und Pflege.** Für eine Action muss die API-Beschreibung
  von Hand im Custom GPT hinterlegt und aktuell gehalten werden. Ein
  MCP-Server meldet seine Funktionen dem Chat-Programm selbst.
- **Funktionsumfang.** Eine Action kann, was die Web API direkt
  anbietet. Ein MCP-Server ist ein Programm mit eigener Logik:
  zotero-mcp kombiniert mehrere API-Aufrufe zu einem Schritt, liest PDFs
  und bietet semantische Suche über die Bibliothek.
- **Ort und Reichweite.** Eine Action läuft in der Cloud des Anbieters
  (der Schlüssel liegt dort) und ist an ChatGPT gebunden. Ein lokaler
  MCP-Server läuft auf dem eigenen Rechner, der Schlüssel bleibt lokal,
  und derselbe Server funktioniert mit jedem MCP-fähigen Chat-Programm.

Ein bewährter Weg (Claude Desktop unter Windows): den Server
[zotero-mcp](https://github.com/54yyyu/zotero-mcp) installieren und mit
einem Web-API-Schlüssel einrichten. Das Modell bekommt Lese- und
Schreibzugriff auf eine dedizierte Sammlung, nie auf die ganze
Bibliothek.

**Sauber einpflegen (Hybrid nach Quelltyp):** Damit die Einträge
zitierfähig sind, führt die Referenz, nicht die lokale Datei.

- arXiv-Preprint über die arXiv-URL anlegen: liefert Titel, Autoren,
  Abstract, arXiv-ID und PDF.
- Veröffentlichten Artikel über die DOI anlegen: liefert CrossRef-Metadaten
  und, wo verfügbar, ein Open-Access-PDF über Unpaywall.
- Nur wenn weder DOI noch arXiv greifen: das lokale PDF importieren und
  die Metadaten von Hand nachtragen. Ein reiner Datei-Import erzeugt
  sonst einen leeren Eintrag ohne brauchbare Angaben.

!!! warnung "Schlüssel und Plugins"
    Der Zotero-API-Schlüssel gehört in die lokale Konfiguration des
    anbindenden Werkzeugs, nie in ein öffentliches Repository, und die
    Schreibrechte werden bewusst auf eine eigene Sammlung beschränkt.
    Für Plugins gilt der Hinweis des Anbieters: Sie haben vollen Zugriff
    auf deine Bibliothek und deinen Rechner. Nur installieren, was du
    kennst.

## Grenzen

- **Synchronisierte Bibliotheken liegen bei Zotero.** Die Software
  selbst läuft lokal und funktioniert auch ohne Konto; sobald du
  synchronisierst, liegen Metadaten und je nach Einstellung auch PDFs
  auf fremden Servern. Bei vertraulichen Volltexten die
  Datei-Synchronisierung bewusst abschalten.
- **Der Gratis-Speicher ist begrenzt.** Die Software kostet nichts, für
  die Synchronisierung grösserer PDF-Bestände braucht es ein
  Speicher-Abo oder einen eigenen Speicherort.
- **Metadaten aus dem Netz sind nicht immer korrekt.** Was die
  Browser-Erweiterung holt, sollte man bei zitierrelevanten Angaben
  prüfen, besonders bei Sammelbänden und grauer Literatur.

## Wann etwas anderes passt

Für Projektwissen, das keine Referenz ist, eignet sich
[Notion](notion.md) besser. Und wenn nicht die Quelle, sondern das
daraus verdichtete Wissen bleiben soll, ist das
[LLM-Wiki](llm-wiki.md) der andere Ansatz; die beiden schliessen
einander nicht aus, diese Website nutzt Zotero für die Belege und ein
Wiki für die Verdichtung.

Offizielle Seite: <https://www.zotero.org> ·
Web API: <https://www.zotero.org/support/dev/web_api/v3/start>

---

Für Notizen und strukturierte Wissensdatenbanken neben den reinen
Referenzen: [Notion](notion.md).
