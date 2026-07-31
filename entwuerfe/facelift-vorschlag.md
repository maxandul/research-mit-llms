# Facelift-Vorschlag: Struktur, Design und Komponenten

**Stand:** 31.07.2026 · Arbeitsdokument, nicht Teil der Website
(liegt unter `entwuerfe/`, ausserhalb von `docs/`, also nicht Teil des Builds)

Entscheidungen aus dem Vorgespräch: Umfang **inklusive Inhaltsumbau**,
Charakter **warm-niederschwellig**, Navigation **Reiter nach
Forschungsphase**.

---

## 1. Befund

Ich habe `mkdocs.yml`, alle 71 Markdown-Dateien, die beiden Hooks und die
Live-Seite in hellem und dunklem Modus angeschaut. Sechs Befunde, sortiert
nach Wirkung.

### 1.1 Es gibt kein Design, nur Voreinstellungen

Kein `extra_css`, keine `overrides/`, keine Schriftwahl, Palette auf
Material-Default `indigo`. Die Seite sieht aus wie jede zweite
MkDocs-Material-Seite. Das ist kein Schönheitsproblem: Ohne eigene
Design-Tokens gibt es keinen Ort, an dem eine Gestaltungsentscheidung
einmal getroffen und überall angewendet wird. Jede spätere Anpassung wird
zur Einzelmassnahme. Das ist der eigentliche Grund, warum "nachhaltig"
hier mit einer CSS-Datei anfängt und nicht mit einer Farbe.

### 1.2 Die wertvollsten Daten sind unsichtbar

Das ist der grösste ungenutzte Hebel. Die Wiki-Notizen tragen bereits
OKF-Frontmatter mit `evidenzstufe`, `verified`, `stale_after`, `studie`
(Modelle, Einsatzart, Durchführungszeitpunkt) und `tags`. Auf der Website
erscheint davon: nichts. Statt dessen steht dieselbe Information ein
zweites Mal als Fliesstext im Notizkopf, von Hand gepflegt.

Zwei Kosten: Doppelpflege (und damit Divergenz zwischen Frontmatter und
Prosa), und Leserinnen sehen die Belastbarkeit einer Notiz nicht auf einen
Blick, obwohl das Wiki genau davon lebt.

Dasselbe auf den Werkzeugseiten: `!!! info "Auf einen Blick"` mit
**Schwierigkeit** / **Kosten** / **Wofür** als Fliesstext. Diese Angaben
sind strukturiert gedacht, aber unstrukturiert abgelegt, also weder
filterbar noch prüfbar noch einheitlich dargestellt.

### 1.3 Die Navigation zeigt neun Bereiche gleichzeitig

Die Seitenleiste listet alle neun Top-Level-Bereiche mit allen
Untereinträgen. Auf einer Wiki-Seite muss man scrollen, um überhaupt zu
sehen, wo man ist. Die Gliederung nach Forschungsphase, eigentlich die
beste Idee der Seite, ist visuell nicht erkennbar, weil alles gleich
aussieht.

Dazu fehlen: Breadcrumbs, Bereichs-Startseiten (`navigation.indexes`),
Icons als Wiedererkennung.

### 1.4 Die Startseite ist eine Textwüste

`docs/index.md` vermischt vier Dinge: Willkommen, Wegweiser ("Wo stehst du
in deiner Arbeit?"), Aufbauerklärung und Lese-Legende ("So liest du die
Hinweis-Boxen", inklusive Beispiel-Admonitions). Der Einstieg, der
eigentlich in zehn Sekunden funktionieren soll, ist eine Bullet-Liste mit
sieben Punkten in Fliesstext.

### 1.5 Acht Admonition-Typen ohne Konvention

Gezählt: 19× `info`, 12× `note`, 11× `tip`, 10× `warning`, 6× `quote`, 3×
`abstract`, 2× `danger`, 1× `example`. Was `info` von `note` unterscheidet,
ist nicht erkennbar; die Farbe trägt keine Bedeutung. Wo jede Box gleich
wichtig aussieht, liest man keine.

### 1.6 Der Wissensgraph ist ein Knäuel

Aktuell rund 45 Knoten, alle Beschriftungen dauerhaft eingeblendet und
überlappend, keine Filter, keine Hervorhebung der Nachbarschaft, feste
Höhe 480px, Farben fest verdrahtet (im dunklen Modus zu grell), kein
Fallback ohne JavaScript. Er ist ein hübsches Argument, aber kein
brauchbares Werkzeug, und er skaliert nicht: Bei 100 Notizen wird er
unlesbar.

**Nebenbefund:** Die Website-Seiten (37 von 71) haben gar kein
Frontmatter. Für Social Cards, Tags und Werkzeug-Badges brauchen sie eins.

---

## 2. Gestaltungskonzept

### 2.1 Farbwelt: warm, gedeckt, mit semantischen Ausnahmen

Kein Standard-Indigo. Basis ist eine warme neutrale Palette (Sand statt
Kaltgrau), damit lange Textstrecken freundlich wirken.

| Rolle | Hell | Dunkel | Wofür |
|---|---|---|---|
| Primär | `#B4532A` Terrakotta | `#E08A5F` | Kopfzeile, Reiter, Marke |
| Akzent | `#0F6E6E` Petrol | `#5DCAA5` | Links, interaktive Elemente |
| Seitenfläche | `#FBF8F4` | `#1C1917` | Hintergrund |
| Karten | `#FFFFFF` | `#262220` | Karten, Boxen |
| Linien | `#E7DFD4` | `#3A332F` | Rahmen, Trenner |

Das Terrakotta trägt die Wärme, das Petrol hält die Links ruhig und
seriös. Zwei Farben, klar getrennte Aufgaben.

Für Bedeutung kommen fünf **Evidenzfarben** dazu, jeweils als Chip mit
Text (nie Farbe allein, sonst nicht barrierefrei):

| Evidenzstufe | Farbe |
|---|---|
| Peer-reviewed | Grün `#1F6F4A` |
| Preprint | Blau `#1B5E8A` |
| Policy | Violett `#6B4E9E` |
| Doku | Schiefer `#4A5568` |
| Praxis | Amber `#9A6708` |

Alle Werte liegen als CSS-Variablen in **einer** Datei
(`docs/assets/stylesheets/tokens.css`). Farbe ändern heisst: eine Zeile
ändern.

### 2.2 Typografie: grösser, weicher, offline

- **Fliesstext:** Atkinson Hyperlegible. Eigens auf Lesbarkeit hin
  entworfen (Braille Institute), freundliche Formen, sehr gut
  unterscheidbare Zeichen. Passt inhaltlich exakt zum niederschwelligen
  Anspruch.
- **Überschriften:** Fraunces (weiche Serife, variabel) mit reduzierter
  "Wonk"-Achse. Gibt Charakter, ohne verspielt zu wirken.
- **Code und Prompts:** JetBrains Mono.
- Basisgrad von 16px auf 17px, Zeilenhöhe 1.7, Textspalte auf etwa 68
  Zeichen begrenzt.

**Wichtig:** Schriften werden nicht von Google geladen, sondern über das
eingebaute `privacy`-Plugin beim Build heruntergeladen und selbst
gehostet. Eine Website, die Datenschutz erklärt, sollte keine IP-Adressen
an Google weiterreichen. Das ist zugleich schneller.

### 2.3 Navigation: Reiter nach Forschungsphase

Aus neun Bereichen werden sechs Reiter in der Kopfzeile:

```
Grundlagen · Literatur · Daten · Schreiben & Haltung · Forschungsstand · Ressourcen
```

Jeder Reiter bekommt eine **Bereichs-Startseite** mit Karten statt einer
blossen Aufklapp-Liste. Die Seitenleiste zeigt nur noch den aktiven
Bereich und wird damit kurz genug, um sie zu überblicken.

Dazu Breadcrumbs (`navigation.path`), Icons pro Bereich,
`navigation.prune` und `navigation.tabs.sticky`.

### 2.4 Komponenten statt Fliesstext

Vier wiederkehrende Bausteine, jeweils **aus dem Frontmatter erzeugt**,
nicht von Hand geschrieben:

**a) Notizkopf für Quellnotizen.** Ersetzt die heutige Zeile
"**Evidenzstufe:** … · **Geprüft:** …". Zeigt Evidenz-Chip,
Prüfvermerk mit Umfang, Ampel aus `stale_after` (grün / gelb ab drei
Monaten vor Fälligkeit / rot danach) und die `studie:`-Angaben (Modelle,
Einsatzart, Durchführung) als eigenen, sichtbaren Block. Genau die
Angaben, die euer Grundsatz "Modell und Einsatzart mitlesen" verlangt,
werden damit erstmals gelesen.

**b) Werkzeug-Steckbrief.** Frontmatter
`werkzeug: {schwierigkeit, kosten, wofuer, stand}` statt
`!!! info "Auf einen Blick"`. Ergibt Badges (Schwierigkeit als ein bis
drei Punkte, nicht nur Farbe) und macht eine filterbare
Werkzeug-Übersicht möglich.

**c) Automatische Indizes.** `docs/wiki/quellen/index.md` und
`konzepte/index.md` werden aus dem Frontmatter generiert: Karten mit
Titel, Evidenzstufe, Prüfdatum, Tags, gruppiert nach Thema. Heute
handgepflegte Bullet-Listen, die bei jedem Sprint mitgeführt werden
müssen und irgendwann veralten.

**d) Prompt-Block.** Eigener Admonition-Typ für kopierfertige Prompts
(Monospace, Kopier-Knopf, Terminal-Icon). Ihr habt eine
Prompt-Bibliothek; sie verdient ein eigenes Element.

### 2.5 Admonition-Konvention: acht Typen werden sechs Rollen

| Typ | Rolle | Ersetzt |
|---|---|---|
| `tip` | Praxistipp, Abkürzung | `tip` |
| `warning` | Fallstrick, Vorsicht | `warning` |
| `datenschutz` (neu) | Rechtliches und Vertraulichkeit | `danger` |
| `evidenz` (neu) | "Was die Forschung sagt", verlinkt in den Forschungsstand | Teile von `info`, `abstract` |
| `quote` | Wörtliches aus Policy oder Quelle | `quote` |
| `beispiel` | Konkreter Fall, ausklappbar | `example`, `note` |

`info` und `note` verschwinden: Sie sind das Symptom fehlender Konvention.
Der neue Typ `evidenz` ist der interessante: Er verbindet die
inhaltlichen Seiten sichtbar mit dem Wiki und macht die
Belegarbeit im Fliesstext auffindbar.

### 2.6 Wissensgraph: vom Poster zum Werkzeug

- Beschriftungen nur bei Hover oder ab einer Zoomstufe; Knotengrösse nach
  Anzahl Verbindungen.
- Hover hebt die Nachbarschaft hervor und dämpft den Rest.
- Filter-Chips nach Schicht **und** nach Thema (aus den vorhandenen
  `tags`), plus Suchfeld.
- Farben aus den CSS-Variablen, also im dunklen Modus stimmig.
- Unter dem Graphen dieselbe Information als aufklappbare Liste:
  barrierefrei und funktioniert ohne JavaScript.
- Zusätzlich ein **Mini-Graph pro Notiz** ("Was hängt hier dran?"). Der
  Nutzen eines Wissensgraphen entsteht beim Lesen einer Notiz, nicht auf
  einer Übersichtsseite.

### 2.7 Startseite: vom Fliesstext zum Einstieg

- Kurzer Hero: Titel, ein Satz, zwei Knöpfe (*Wo anfangen?* /
  *Forschungsstand*).
- Sechs Karten nach Forschungsphase, mit Icon und einem Satz.
- "Wo stehst du in deiner Arbeit?" als kompakte Karten statt Bullet-Liste.
- "Zuletzt geändert": die drei jüngsten Changelog-Einträge, automatisch.
- Die Lese-Legende ("So liest du die Hinweis-Boxen", Schwierigkeitsstufen,
  Kosten) zieht auf eine eigene Seite *Wegweiser* um. Sie ist nützlich,
  aber kein Startseiteninhalt.
- Der Hinweis "Diese Seite ist im Aufbau" wandert in eine
  `announce`-Leiste am Seitenkopf: einmal für die ganze Website statt als
  Warnbox auf mehreren Seiten.

### 2.8 Kleinere Gewinne, die sich lohnen

- **Tags-Plugin** aktivieren: Die Tags stehen schon im Frontmatter, es
  fehlt nur die Indexseite. Sofortiger Gewinn für null Inhaltsarbeit.
- **Social Cards** (`social`-Plugin): eigenes Vorschaubild pro Seite beim
  Teilen. Braucht Pillow und CairoSVG in `requirements.txt`.
- **Glossar-Tooltips**: `docs/ressourcen/glossar.md` speist eine
  `includes/abkuerzungen.md`; Begriffe wie "Token" oder "RAG" bekommen
  überall auf der Website einen Tooltip (`content.tooltips` plus
  `abbr`/`snippets`).
- Eigene 404-Seite, Footer mit Lizenz und Repo-Link, `search.share`.

---

## 3. Etappen

Jede Etappe ist für sich lauffähig und deploybar. Nach jeder kannst du
abbrechen, ohne dass etwas halbfertig aussieht.

| # | Etappe | Inhalt | Berührt Inhalte? |
|---|---|---|---|
| 1 | **Fundament** | `tokens.css`, Farbwelt, Schriften, `privacy`-Plugin, Typografie-Feinschliff | nein |
| 2 | **Navigation** | Reiter, sechs Bereichs-Startseiten, Breadcrumbs, Icons, `mkdocs.yml`-Umbau | neue Seiten, alte unverändert |
| 3 | **Komponenten** | Hook für Notizkopf und Werkzeug-Steckbrief, Admonition-Typen, Prompt-Block | Frontmatter ergänzen, Prosa-Dubletten entfernen |
| 4 | **Startseite** | Hero, Karten, Wegweiser-Seite, `announce`-Leiste | ja, Startseite neu |
| 5 | **Wiki** | Automatische Indizes, Graph-Überarbeitung, Mini-Graphen, Tags-Index | Indizes werden generiert |
| 6 | **Feinschliff** | Social Cards, Glossar-Tooltips, 404, Footer, Designregeln in `CLAUDE.md` | nein |

**Etappe 3 ist die wichtigste.** Sie ist der Unterschied zwischen einem
Facelift und einem System: Danach ist das Frontmatter die einzige Quelle
der Wahrheit, und jede neue Quelle sieht automatisch richtig aus, ohne
dass jemand an Prosa denken muss.

## 4. Was danach in CLAUDE.md gehört

Damit der Umbau nicht in einem Jahr wieder auseinanderläuft, kommt ein
Abschnitt **Designregeln** dazu:

- Welche Admonition-Typen es gibt und wofür (die sechs Rollen).
- Dass Evidenzstufe, Prüfvermerk und `studie:` **nur** ins Frontmatter
  gehören und nicht mehr in die Prosa.
- Dass Werkzeugseiten einen `werkzeug:`-Block brauchen.
- Dass Farben und Abstände ausschliesslich aus `tokens.css` kommen.
- Dass Indizes generiert werden und nicht von Hand zu pflegen sind.

Dazu eine Erweiterung von `tools/wiki_lint.py`: fehlender
`werkzeug:`-Block, unbekannter Admonition-Typ, hart kodierte Farbe im
Markdown.

## 5. Entschieden am 31.07.2026

1. **Reiter-Zuschnitt:** sieben Reiter, **Haltung bleibt eigenständig**.
   Also: Grundlagen · Literatur · Daten · Schreiben · Haltung ·
   Forschungsstand · Ressourcen.
2. **Titelschrift: Source Serif 4** (nicht Fraunces). Fliesstext bleibt
   Atkinson Hyperlegible.
3. **Petrol ist Primärfarbe**, Terrakotta nur Akzent. Die Tabelle in
   Abschnitt 2.1 ist entsprechend zu lesen: Petrol trägt Kopfzeile,
   Reiter und Links, Terrakotta die Hervorhebungen und aktiven Zustände.
4. **Indizes hybrid:** generierte Karten aus dem Frontmatter plus ein
   handgeschriebener Vorspann pro Thema. Die redaktionelle Einordnung
   bleibt also erhalten, nur die Listenpflege entfällt.

## 6. Stand der Umsetzung

### Etappe 1: Fundament (erledigt)

| Datei | Was |
|---|---|
| `docs/assets/stylesheets/tokens.css` | neu: Farbrampen, Zweck-Tokens für hell und dunkel, Evidenzfarben, Ampelfarben, Masse |
| `docs/assets/stylesheets/extra.css` | neu: Abbildung der Tokens auf Material, Typografie, Navigation, Tabellen, Code, Hinweisboxen |
| `overrides/main.html` | neu: lädt Source Serif 4 nach |
| `mkdocs.yml` | Palette auf `custom`, Schriften, `extra_css`, `privacy`-Plugin, `custom_dir` |
| `requirements.txt` | Versionen nach oben begrenzt |

Geprüft: `mkdocs build --strict` läuft ohne Warnung durch (71 Seiten),
`tools/wiki_lint.py` meldet nur den vorbestehenden Befund zu
`liang-2025-llm-praevalenz.md`. Alle Farbpaare rechnerisch gegen WCAG
geprüft, hell und dunkel: Fliesstext ab 15:1, Links ab 5,7:1, alle
Evidenz-Chips ab 6,7:1. Damit liegt jede Kombination über AA, die
meisten über AAA.

**Noch nicht am echten Bild geprüft.** Die Sandbox kommt nicht an Google
Fonts, deshalb konnten die Schriften nicht geladen und die Seite nicht
im Browser angesehen werden. Beim ersten Push zu prüfen: Wirkt der
Grundgrad von 17px zu gross? Sitzt Source Serif 4 als Titelschrift
richtig? Atkinson Hyperlegible hat kein Schnittgewicht 300, das Material
sonst für Überschriften nutzt; die Überschriften laufen deshalb über
Source Serif 4 in 600.

**Nebengewinn des `privacy`-Plugins:** Es holt nicht nur die Schriften,
sondern auch das d3 aus dem Wissensgraphen vom CDN. Die Website macht
danach beim Besuch keine Anfrage mehr an Dritte. Für eine Seite, die
Datenschutz erklärt, ist das mehr als Kosmetik.

### Etappe 2: Navigation (erledigt)

Acht Reiter in der Kopfzeile, je mit Icon:

```
Start · Grundlagen · Literatur · Daten · Schreiben · Haltung · Forschungsstand · Ressourcen
```

Aus neun Top-Level-Bereichen wurden sieben inhaltliche: "Daten erheben &
schützen" und "Daten analysieren" sind zu **Daten** zusammengefasst (mit
den Untergruppen "Erheben & schützen" und "Analysieren"), "Über" ist
unter Ressourcen gewandert. Haltung bleibt wie entschieden eigenständig.

| Datei | Was |
|---|---|
| `docs/grundlagen/index.md` | neu, sieben Karten |
| `docs/literatur/index.md` | neu, vier Gruppenkarten (Finden, Dialog, Sammeln, Workflows) |
| `docs/daten/index.md` | neu, vier Karten in zwei Gruppen |
| `docs/schreiben/index.md` | neu, zwei Karten |
| `docs/haltung/index.md` | neu, eigener Text zu Verantwortung und Prüfpflicht plus zwei Karten |
| `docs/ressourcen/index.md` | neu, sechs Karten |
| `docs/wiki/index.md` | Frontmatter mit `icon` und `description` ergänzt |
| `docs/index.md` | Abschnitt "Wie diese Seite aufgebaut ist" auf die neue Gliederung gebracht, alle Bereiche verlinkt |
| `mkdocs.yml` | `navigation.tabs`, `.sticky`, `.indexes`, `.path`, `.prune`, `.tracking`, `search.share`, `pymdownx.emoji`, Navigationsbaum neu |
| `docs/assets/stylesheets/extra.css` | Abschnitte 4b (Reiter, Brotkrumen) und 4c (Kartenraster) ergänzt |

**Zwei Dinge, die unterwegs aufgefallen sind.**

`navigation.indexes` erkennt nur eine echte `index.md` als
Bereichs-Startseite. "Literatur" und "Daten" spannen über mehrere Ordner
(`werkzeuge/`, `workflows/` bzw. `erheben/`, `analysieren/`), eine flache
`literatur.md` wurde deshalb nicht als Startseite behandelt, sondern als
gewöhnliche erste Unterseite, ohne Icon und mit doppeltem Eintrag in der
Seitenleiste. Gelöst durch eigene Ordner `docs/literatur/` und
`docs/daten/`, die nur ihre `index.md` enthalten.

Die Ordnernamen passen jetzt teils nicht mehr zu den Reiternamen: Unter
"Literatur" liegen Seiten mit URLs wie `/werkzeuge/finden/elicit/`. Das
ist kosmetisch und nur in der Adresszeile sichtbar. Ein Umbenennen würde
alle bestehenden Links brechen und bräuchte `mkdocs-redirects`. Vorschlag:
liegen lassen, oder in Etappe 6 zusammen mit Weiterleitungen erledigen.

Geprüft: `mkdocs build --strict` grün (77 Seiten), `wiki_lint.py`
unverändert nur der bekannte Befund. Alle **543 internen Links** im
gebauten Site gegen den Dateibestand geprüft, **kein toter Link**. Alle
acht Reiter zeigen auf die richtige Startseite und tragen ihr Icon.
Brotkrumen erscheinen auf den Unterseiten, `navigation.prune` kürzt die
Seitenleiste wie erwartet.

**Keine bestehende URL hat sich geändert.** Es kamen nur Seiten dazu,
Lesezeichen und externe Verweise bleiben gültig.

**Noch nicht am echten Bild geprüft**, aus demselben Grund wie in Etappe 1.
Beim ersten Push anzusehen: Wirken acht Reiter in der Kopfzeile zu voll?
Sind die Karten mit `minmax(15rem, 1fr)` richtig dimensioniert? Ist der
Terrakotta-Unterstrich am aktiven Reiter deutlich genug?

### Etappen 3 bis 6

Offen, siehe Abschnitt 3.
