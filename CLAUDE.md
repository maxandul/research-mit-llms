# Spielregeln für dieses Repository

Dieses Dokument ist das **Schema** des Forschungsstand-Wikis (im Sinn von
`docs/workflows/forschungs-wiki.md`): Es sagt einem LLM-Agenten, wie das
Wiki funktioniert und wie neue Quellen eingepflegt werden. Es ist zugleich
Teil des Fallbeispiels — Besucher der Website können hier nachlesen, wie
die Belege entstehen.

## Das Projekt

MkDocs-Material-Website "Forschen mit LLMs" (deutsch, Schweizer
Rechtschreibung, CC BY 4.0). Inhalte unter `docs/`, Navigation in
`mkdocs.yml`, Deploy automatisch via GitHub Actions bei Push auf `main`.

## Schreibregeln

- Kein Eszett (ß), immer Doppel-S. Umlaute (ä/ö/ü) normal verwenden.
- Auf Gedankenstriche möglichst verzichten; stattdessen Kommas,
  Doppelpunkte, Klammern oder kurze Sätze verwenden.
- Niederschwelliger, praktischer Ton; keine unnötigen Anglizismen.
- Interne Verweise als relative Markdown-Links (keine Wikilinks).

## Das Wiki: vier Schichten

```text
rohdaten/               PDFs/Volltexte, nur Durchgang — gitignored, NIE committen (Urheberrecht)
docs/wiki/quellen/      eine Notiz pro Quelle (Provenienz + Verifikation)
docs/wiki/konzepte/     atomare Themen, quellenübergreifend (das Netz)
docs/wiki/synthese/     Forschungsstand pro Website-Thema
```

Der Wissensgraph wird beim Build automatisch aus den Markdown-Links
erzeugt (`tools/wiki_graph.py`, eingebunden als Hook in `mkdocs.yml`) und
auf `docs/wiki/index.md` gerendert. Er braucht keine manuelle Pflege —
saubere Verlinkung genügt.

**Die Evidenz führt, nicht die Website:** Synthesen entsprechen in der
Regel den Website-Themen, müssen aber nicht entlang der bestehenden
Website wachsen. Drängt sich aus den Konzepten eine Synthese auf, die den
Aufbau der Website verändern würde (neue Seite, andere Gliederung,
zusammengelegte oder gestrichene Inhalte), ist das erlaubt und erwünscht.
Solche Strukturänderungen dem Menschen vorschlagen, nach Entscheid
umsetzen und im Changelog begründen.

## ingest: eine neue Quelle einpflegen (zwei Phasen)

**Phase 1 — Sichten** (Abstract-Ebene, LLM-tauglich):

1. Kandidaten suchen (Semantic Scholar / OpenAlex), DOI/URL auflösen,
   Abstracts lesen, Relevanz einordnen. Keine Quelle aus dem Gedächtnis
   zitieren — LLMs erfinden Referenzen. Bewusst sein und transparent
   machen: Durchsucht wird nur öffentlich Zugängliches; die Recherche in
   lizenzierten Fachdatenbanken liegt beim Menschen.
2. Kandidatenliste mit Kurzeinordnung dem Menschen vorlegen: Was
   verspricht die Quelle, warum ist sie relevant?

**Phase 2 — Vertiefen** (Volltext-Ebene, Pflicht vor der Quellnotiz):

3. **Volltext beschaffen** (Open Access, arXiv, Verlagsseite; sonst durch
   den Menschen) und in `rohdaten/` ablegen — nie committen. Der Mensch
   liest mit und/oder stellt dem LLM den Volltext zur Verfügung. Zugleich
   die Quelle in die Zotero-Sammlung `research-mit-llms` einpflegen (siehe
   Abschnitt "Zotero-Anbindung").
4. **Quellnotiz erst auf Volltext-Basis** in `docs/wiki/quellen/` anlegen
   (Vorlage unten) und im dortigen `index.md` eintragen. Ist ausnahmsweise
   kein Volltext beschaffbar, im Feld "Geprüft" explizit **"nur Abstract"**
   vermerken — solche Notizen gelten als vorläufig.
5. **Evidenzstufe bestimmen:** Peer-reviewed / Preprint / Policy / Doku /
   Praxis (Definitionen in `docs/wiki/index.md`).
6. **Konzeptnotizen** anlegen oder erweitern: Welche atomaren Aussagen
   stützt die Quelle? Bestehende Konzepte zuerst prüfen (`docs/wiki/konzepte/index.md`),
   nur bei echtem neuem Sachverhalt ein neues Konzept anlegen.
   Verwandte Konzepte gegenseitig verlinken.
7. **Synthese** des betroffenen Themas aktualisieren.

## Grundsatz: Modell und Einsatzart mitlesen

LLM-Fähigkeiten entwickeln sich so schnell und die Einsatzarten sind so
vielfältig, dass empirische Befunde ohne Methodenkontext wertlos oder
irreführend sind. Deshalb bei **jeder** empirischen Quelle zu LLMs:

- Im Methodenteil prüfen und in der Quellnotiz festhalten: Welche Modelle
  (exakte Version), wie eingesetzt (Prompting, Parameter, API/Web/lokal,
  Reasoning-Modus), wann durchgeführt (nicht nur wann publiziert)?
- Schlussfolgerungen entsprechend datieren und begrenzen: Negative Befunde
  mit schwachen oder falsch konfigurierten Modellen widerlegen die
  Machbarkeit nicht; positive Befunde gelten für die getestete
  Konfiguration, nicht für "LLMs" allgemein. Studien von 2024/2025 sind
  bei Modellfragen oft schon überholt; ihre Werte als untere Schranke lesen.
- In Konzeptnotizen und Synthesen Modellgeneration und Einsatzart der
  Belege sichtbar machen, bevor daraus Website-Empfehlungen werden.
- **Vorsichtig formulieren.** Die Studienlage zu LLM-Fähigkeiten ist jung
  (breite Nutzung erst seit Ende 2022), unvollständig und veraltet
  schnell. Deshalb keine Gewissheits- oder Superlativ-Rhetorik: nicht
  "gut belegt", "gut untersucht", "gut gestützt", "bisher grösster",
  "selbst die besten Modelle". Stattdessen datierte Momentaufnahmen und
  Vergangenheitsform für Testergebnisse: "in bisherigen Studien", "in
  einem Benchmark mit 46 Modellen (2026)", "Stand Juli 2026", "zeigten
  in Tests". Beobachtete Schwächen nie als dauerhafte Eigenschaften
  beschreiben; sie können mit der nächsten Modellgeneration behoben
  sein. Stabiler formulieren darf man nur, was nicht an der
  Modellgeneration hängt (z.B. Policy-Konsense, epistemologische
  Argumente).

Ankerpunkt im Wiki: `docs/wiki/konzepte/modell-und-einsatzart.md`.

## Zotero-Anbindung

Parallel zu den Quellnotizen werden alle eingepflegten Quellen in einer
dedizierten Zotero-Sammlung `research-mit-llms` gesammelt (bibliografische
Referenz plus PDF-Anhang). Das LLM greift über einen lokal eingerichteten
Zotero-MCP-Server (Web-API) darauf zu und schreibt ausschliesslich in diese
Sammlung, nie sonst in die Bibliothek. Der API-Key liegt nur in der lokalen
Claude-Desktop-Konfiguration (`%APPDATA%\Claude\claude_desktop_config.json`),
nie im Repo.

**Einpflegen nach Quelltyp (Hybrid):** Die Metadaten sollen zitierfähig
sein, darum führt die Referenz, nicht die lokale Datei:

- arXiv-Preprint: über die arXiv-URL anlegen (`zotero_add_by_url`). Liefert
  Titel, Autoren, Abstract, arXiv-ID und PDF.
- Veröffentlichter Artikel: über die DOI anlegen (`zotero_add_by_doi`).
  Liefert CrossRef-Metadaten und, wo verfügbar, ein Open-Access-PDF
  (Unpaywall).
- Nur wenn weder DOI noch arXiv greifen und kein OA-PDF auffindbar ist: das
  lokale `rohdaten`-PDF über `zotero_add_from_file` anhängen und die
  Metadaten anschliessend von Hand nachtragen (`zotero_update_item`). Der
  reine Datei-Import erzeugt sonst nur ein leeres "document" ohne
  brauchbare Metadaten.

Vor Schreiboperationen immer erst lesend prüfen (`zotero_get_collections`),
und neue Einträge dem Menschen zur Kontrolle in Zotero melden.

**`rohdaten/` ist nur ein Durchgangsordner, Zotero die dauerhafte Ablage:**
Sobald eine Quelle kontrolliert in Zotero liegt (zitierfähige Metadaten
und PDF-Anhang vorhanden), das lokale PDF aus `rohdaten/` löschen. Erst
nach dieser Kontrolle löschen, nie davor; hängt in Zotero kein PDF am
Eintrag, bleibt die Datei lokal liegen. Vorsicht bei `zotero_add_from_file`
mit `if_exists='file'`: schlägt die DOI-Extraktion aus dem PDF fehl,
entsteht statt des Anhangs ein leeres "document"-Duplikat. Dann Metadaten
ins Duplikat nachtragen (`zotero_update_item`) und den PDF-losen
Doppelgänger löschen, so bleibt das PDF am zitierfähigen Eintrag.

## Nach einem Sprint (Thema abgeschlossen)

1. Betroffene Website-Seite anpassen: Quellen-Sektion (Muster:
   `docs/haltung/ki-deklarieren.md`), Vermerk "Evidenz zuletzt geprüft",
   inhaltliche Korrekturen, wenn die Evidenz Empfehlungen widerspricht.
2. **Changelog-Eintrag** in `docs/ressourcen/changelog.md`: geschrieben für
   Besucher der Website, die sich über LLMs in der Forschung informieren,
   nicht als internes Arbeitslog. Festhalten, was sich inhaltlich geändert
   hat und was Leser davon haben (neue Belege und Erkenntnisse, neue oder
   korrigierte Empfehlungen, neue Seiten oder Methoden). Rein interne
   Vorgänge (Schema-Anpassungen, Umbauten am Ablauf, Werkzeug-Setup) gehören
   nicht in den Changelog, sondern in die Commit-Historie bzw. dieses Schema;
   nur wenn sie für Leser sichtbar etwas ändern, kurz und besucherorientiert
   erwähnen. Datiert und menschenlesbar.
3. Neue Synthese in `mkdocs.yml` unter `nav:` → Forschungsstand eintragen.
4. Build testen: `mkdocs build --strict`.

## lint: regelmässige Prüfung

- Widersprüche zwischen Konzepten markieren, nicht stillschweigend glätten.
- Veraltete Policies kennzeichnen (Policies ändern sich laufend; das
  Prüfdatum steht in jeder Quellnotiz).
- **Quellnotizen mit Vermerk "nur Abstract" melden** — sie sind vorläufig
  und sollen mit dem Volltext nachgerüstet werden.
- Verwaiste Notizen (ohne eingehende Links) und tote Links melden.

## Vorlage: Quellnotiz

```markdown
# Kurztitel der Quelle

**Evidenzstufe:** ... ·
**Geprüft:** TT.MM.JJJJ, was genau geprüft wurde (Original gelesen? DOI aufgelöst?)

> Vollständige bibliografische Angabe mit Link/DOI.

## Kernaussagen
## Einordnung        (Methodik, Grenzen, Bias — weglassen wenn trivial)
## Relevanz für die Website
## Querverweise
```

## Vorlage: Konzeptnotiz

```markdown
# Name des Konzepts

**Konzeptnotiz** · Stand: Monat JJJJ

Kernaussage in 1-2 Absätzen, quellenübergreifend formuliert.

## Belege             (Links auf Quellnotizen, je mit Evidenzstufe)
## Verwandte Konzepte (Links, mit einem Halbsatz zur Beziehung)
## Fliesst ein in     (Synthese- und Website-Seiten)
```

## Geplante Sprint-Reihenfolge

1. ~~ki-deklarieren~~ (Juli 2026 abgeschlossen)
2. qualitativ-codieren (LLM als zweiter Codierer, Intercoder-Übereinstimmung,
   methodologische Kritik)
3. transkription (Whisper-Benchmarks Deutsch/Schweizerdeutsch, Diarisierung,
   Wirkung von Transkriptionsfehlern auf die Analyse)
4. wie-llms-arbeiten (erweitert um Kontextfenster und Halluzinationen:
   lost in the middle, Tokenisierung/Rechnen, Prompt-Sensitivität)
5. anonymisieren-datenschutz (Re-Identifikation, Grenzen der Anonymisierung
   qualitativer Daten, Einwilligung; hohe Fallhöhe)
6. ki-literaturrecherche (Evaluationen der Recherche-Werkzeuge, Recall und
   Abdeckung, erfundene Referenzen vertieft)
7. schreiben-mit-llms (Copy-Editing vs. Inhaltserzeugung, Chancen für
   Nicht-Muttersprachler, KI-Detektoren, kognitive Auslagerung/De-Skilling)
8. quantitativ-auswerten (Korrektheit LLM-generierten Analysecodes,
   Reproduzierbarkeit)

**Beobachtungsliste** (noch ohne Sprint, könnten neue Seiten erzwingen):
Bias/WEIRD-Verzerrungen in Forschungsergebnissen, LLMs im Peer Review,
Lernen mit LLMs als eigene Haltung-Seite (fällt vorerst unter Sprint 7).
