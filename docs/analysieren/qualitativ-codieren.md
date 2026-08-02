# Qualitative Daten codieren

Ein LLM kann beim Codieren qualitativer Daten (Interviews, offene
Fragebogen-Antworten, Feldnotizen) viel Arbeit abnehmen, wenn du es als
**zweiten Codierer** behandelst: Es macht Vorschläge nach deinem Codebuch,
du prüfst und entscheidest.

Erste Studien zu diesem Vorgehen liegen vor, mit einer wichtigen
Einschränkung: Die Forschung ist jung, lückenhaft, und die Modelle ändern
sich schneller, als Studien erscheinen. Als Momentaufnahme (Stand Juli
2026): Beim **deduktiven Codieren mit klarem Codebuch** erreichten
aktuelle Modelle in einzelnen Untersuchungen die Zuverlässigkeit
erfahrener menschlicher Codierer, abhängig von Modellwahl und
Arbeitsweise (Quellen unten). Genau davon hängt viel ab; die berichteten
Übereinstimmungen reichen von 36 bis 99 Prozent, je nach Modell, Prompt
und Prüfstrenge. Umso wichtiger, dass du deine eigene Konfiguration
prüfst, statt dich auf publizierte Werte zu verlassen.

## Voraussetzungen

- Daten sind [anonymisiert bzw. pseudonymisiert](../erheben/anonymisieren.md),
  bevor irgendetwas in einen Cloud-Dienst geht.
- Ein Chat-Werkzeug wie Claude oder ChatGPT, möglichst mit einem
  **aktuellen Modell mit aktiviertem Reasoning** ("Nachdenken"): In einem
  Benchmark mit 46 Modellen (2026) machte genau das den Unterschied
  zwischen zuverlässigem und unzuverlässigem Codieren aus.
- Die Daten als Tabelle (Excel/CSV): eine Zeile pro Aussage oder Segment.

## Der Workflow

### 1. Codebuch definieren

Pro Code: Name, Definition, ein Ankerbeispiel und die Abgrenzung zu
ähnlichen Codes. Wo die Abgrenzung unscharf bleibt, weichen Mensch und
Modell später genau dort voneinander ab.

```text
Code: BELASTUNG_ZEIT
Definition: Aussagen über zeitlichen Druck oder Überlastung im Arbeitsalltag.
Ankerbeispiel: "Ich komme kaum dazu, eine Pause zu machen."
Abgrenzung: Nicht für emotionale Belastung ohne Zeitbezug (dann BELASTUNG_EMO).
```

Arbeitest du **induktiv** (Codes aus dem Material entwickeln), kann das LLM
helfen: Gib ihm einen Teil des Materials und lass dir Kategorienvorschläge
machen, die du dann selbst zum Codebuch verdichtest. Die Entscheidung, was
eine Kategorie ist, bleibt deine.

### 2. Daten als Tabelle mit ID- und Frage-Spalte vorbereiten

Jede Zeile bekommt eine eindeutige ID (1, 2, 3, ...). Die ID ist deine
Versicherung: Nur so erkennst du später, ob Zeilen übersprungen wurden, und
kannst die Codes fehlerfrei in deine Excel-Tabelle zurückführen.

Genauso wichtig: **Die Frage gehört mit in die Tabelle.** Kurze Antworten
wie "Ja, auf jeden Fall" oder "Eher selten" sind ohne die zugehörige Frage
nicht interpretierbar; das LLM würde raten. Also pro Zeile eine Spalte mit
der gestellten Frage (oder dem Interview-Impuls) mitführen:

| ID | Frage | Antwort |
|----|-------|---------|
| 1 | Wie erleben Sie den Zeitdruck im Alltag? | Es geht eigentlich. |
| 2 | Würden Sie den Beruf wieder wählen? | Ja, auf jeden Fall. |

Bei Interviews mit Gesprächsverlauf gilt dasselbe sinngemäss: dem Segment
so viel Kontext mitgeben (vorangehende Frage, ggf. der vorherige Turn),
dass die Bedeutung ohne Raten erschliessbar ist.

### 3. Codieren lassen, in Häppchen

Gib dem Modell das Codebuch und **20 bis 30 Zeilen pro Durchgang**, nicht
die ganze Tabelle auf einmal. Verlange pro Zeile Code, Begründung und
Ankerzitat. Eine kopierfertige Vorlage steht in der
[Prompt-Bibliothek](../ressourcen/prompt-bibliothek.md).

Zwei dieser Prinzipien zeigten in bisherigen Studien übereinstimmend
einen positiven Effekt: Nach einer **Begründung pro Entscheid** fragen
verbesserte die Codierqualität, und **kleinere Aufgabenpakete schlugen
den grossen Wurf**. Bei
schwierigen oder unscharfen Codes lohnt sich die konsequenteste Variante
davon: einen Code pro Durchgang codieren lassen statt das ganze Codebuch
auf einmal. Die konkrete Häppchengrösse von 20 bis 30 Zeilen ist dagegen
Praxiserfahrung, kein Forschungsergebnis; experimentiere, was bei deinem
Material funktioniert.

!!! warnung "Stolperstein: das LLM schätzt über den Daumen"
    LLMs sind Muster-Vervollständiger, keine Schleifen (siehe
    [Wie ein LLM arbeitet](../grundlagen/wie-llms-arbeiten.md)). Bei langen
    Tabellen neigen sie dazu, nach ein paar dutzend Zeilen das Muster zu
    "erkennen" und den Rest pauschal oder lückenhaft zu codieren, statt jede
    Zeile einzeln zu bearbeiten. Dagegen hilft:

    1. Explizit anweisen: jede Zeile einzeln, keine Zusammenfassungen,
       keine Auslassungen.
    2. Ausgabe muss exakt so viele Zeilen haben wie die Eingabe, mit den
       IDs aus der Eingabe.
    3. In Häppchen von 20 bis 30 Zeilen arbeiten.
    4. Nachzählen: Stimmen Zeilenzahl und IDs? Das ist der billigste und
       wichtigste Qualitätscheck.

### 4. Prüfen wie bei einem zweiten Codierer

- **Vollständigkeit:** Zeilen und IDs abgleichen (Schritt 3).
- **Stichprobe:** Einen Teil selbst codieren und mit dem LLM vergleichen,
  wie bei einem Intercoder-Vergleich. Wo ihr auseinanderliegt, ist oft das
  Codebuch unscharf, nicht das Modell "dumm".
- **Differenzen nutzen:** Abweichungen mit dem LLM diskutieren ("Warum hast
  du hier BELASTUNG_EMO vergeben?"). Die Begründungen zeigen, wo
  Definitionen nachgeschärft werden müssen. Danach ggf. einen zweiten
  Durchgang mit dem verbesserten Codebuch fahren.
- **Nach Fallhöhe staffeln:** Gute Gesamtwerte können systematische
  Schwächen bei einzelnen Codes verdecken; in Benchmarks trifft es
  ausgerechnet heikle, indirekt geäusserte Themen. Codes, bei denen
  Fehlcodierung am meisten schadet (etwa Belastung, Sicherheit,
  Diskriminierung), gezielt und vollständiger prüfen als den Rest, nicht
  nur per Zufallsstichprobe.

### 5. Ergebnisse zurückführen und dokumentieren

Codes in die Excel-Tabelle übernehmen (per ID zuordnen) und das Vorgehen
fürs Methodenkapitel festhalten: Codebuch-Version, **exakte Modellversion**
(nicht nur "ChatGPT", sondern z.B. Modellname und Datum), Einsatzform
(Web-Chat, API, lokal) und relevante Einstellungen, die verwendeten
Prompts sowie alle Prüfschritte. Das entspricht dem Stand der
Reporting-Diskussion (Stichwort COREQ + LLM): In der publizierten
Forschung fehlen diese Angaben bisher meistens, was die Studien
unvergleichbar macht; deine Arbeit macht es besser. Das gehört auch in
die [Deklaration der KI-Nutzung](../haltung/ki-deklarieren.md).

### Lohnt sich das bei einer kleinen Interviewstudie?

Ehrliche Einordnung aus der Forschung: Der Aufbau eines sauber
geprüften LLM-Workflows (Codebuch schärfen, Vergleichscodierung,
Differenzen klären) kostet bei wenigen Interviews ähnlich viel Zeit
wie das Selbst-Codieren, das zudem Nähe zum Material stiftet. Das
LLM spielt seine Stärke bei grossen Materialmengen aus. Bei kleinen
Studien ist es vor allem als **Zweitmeinung und Sparringpartner**
wertvoll (Differenzen zeigen unscharfe Definitionen), weniger als
Zeitersparnis.

## Profi-Variante: der Agent arbeitet die Schleife ab

Wer die Vollständigkeit nicht der Disziplin des Modells überlassen will,
lässt einen Coding-Agenten (Claude Code, Cursor) die Tabelle
**programmatisch** Zeile für Zeile durchlaufen: Ein Skript iteriert über
die Zeilen, das LLM codiert nur den Inhalt der jeweils aktuellen Zeile.
Die Schleife garantiert, dass keine Zeile fehlt. Bei hunderten Zeilen ist
das der verlässlichere Weg.

## Alternative: QDA-Software mit KI-Funktionen

Für grosse Projekte oder wenn die Methodik im Zentrum steht, lohnt sich
ein Blick auf etablierte QDA-Software, die inzwischen eigene
KI-Funktionen mitbringt: [MAXQDA](../werkzeuge/analysieren/maxqda.md)
und [ATLAS.ti](../werkzeuge/analysieren/atlasti.md).

Der Vorteil gegenüber dem Chat-Workflow: Codesystem, Fundstellen und
Dokumente bleiben in einer dafür gebauten Umgebung, statt dass du
Ergebnisse aus einem Chatfenster zurückkopierst. Der Nachteil: weniger
Kontrolle über die Prompts, und die KI-Funktionen laufen ebenfalls über
die Cloud, es gilt also dieselbe
[Anonymisierungs-Regel](../erheben/anonymisieren.md). Beides sind
kostenpflichtige Programme; viele Hochschulen haben Campuslizenzen,
vorher nachfragen.

## Werkzeuge für die Auswertung

{{ werkzeuge:analysieren }}

## Grenzen

- Das LLM codiert am zuverlässigsten, was explizit dasteht. Bei
  **implizit Geäussertem, Randfällen und feinen Bedeutungen** (Ironie,
  Kontextabhängiges) zeigten in bisherigen Tests auch die
  leistungsstärksten Modelle Schwächen. Ob das so bleibt, ist offen;
  bis auf Weiteres prüft hier der Mensch (siehe "Nach Fallhöhe
  staffeln" oben).
- Interpretation, Theoriebezug und die Synthese der Befunde bleiben bei dir
  (siehe [Rollenteilung](../grundlagen/llms-verstehen.md)). Ein Teil der
  qualitativen Community hält schon das maschinelle Codieren für
  unvereinbar mit reflexiver qualitativer Forschung; diese Debatte ist
  offen. Prüfe, wo deine Methodentradition (und deine Betreuungsperson)
  steht.
- Eine rote Linie, die nicht an der Modellgeneration hängt:
  **LLMs simulieren keine Teilnehmenden.**
  Synthetische "Interviewdaten" aus LLM-Personas wirken plausibel, haben
  aber keine gelebte Erfahrung hinter sich und unterlaufen Einwilligung
  und Handlungsmacht echter Communities. LLMs helfen beim Verarbeiten
  erhobener Daten, nicht beim Erzeugen.
- Methodisch sauber ist der Einsatz dann, wenn er dokumentiert, geprüft und
  im Methodenteil offengelegt ist.

!!! evidenz "Evidenz zuletzt geprüft: Juli 2026"
    Die Belege zu dieser Seite sind im
    [Forschungsstand: Qualitative Daten codieren](../wiki/synthese/qualitativ-codieren.md)
    zusammengefasst. Wichtig beim Lesen: Die Studienlage ist jung und
    unvollständig, Modell, Version und Einsatzart bestimmen die
    Ergebnisse. Alle Befunde sind Momentaufnahmen; beobachtete Schwächen
    können mit der nächsten Modellgeneration verschwunden sein.

## Quellen

- Kempny et al. (2026), *The use and methodological reporting of large
  language models in qualitative research: a scoping review*, BMC Medical
  Research Methodology — peer-reviewed:
  <https://doi.org/10.1186/s12874-026-02913-1>
  · [Notiz](../wiki/quellen/kempny-2026-llm-qualitativ-scoping-review.md)
- Dunivin (2025), *Scaling hermeneutics: a guide to qualitative coding
  with LLMs for reflexive content analysis*, EPJ Data Science —
  peer-reviewed: <https://doi.org/10.1140/epjds/s13688-025-00548-8>
  · [Notiz](../wiki/quellen/dunivin-2025-scaling-hermeneutics.md)
- Misra et al. (2026), *Large Language Models in Qualitative Analysis*,
  International Journal of Qualitative Methods — peer-reviewed:
  <https://doi.org/10.1177/16094069261426100>
  · [Notiz](../wiki/quellen/misra-2026-open-source-llms-codieren.md)
- Kapania et al. (2025), *Simulacrum of Stories*, CHI '25 — peer-reviewed:
  <https://doi.org/10.1145/3706598.3713220>
  · [Notiz](../wiki/quellen/kapania-2025-simulacrum-of-stories.md)
- Marston et al. (2026), *Can Large Language Models Reliably Code
  Qualitative Humanitarian Data?* — Preprint:
  <https://arxiv.org/abs/2606.26541>
  · [Notiz](../wiki/quellen/marston-2026-humanitaere-daten-benchmark.md)

---

Für Zahlen statt Texte gilt ein anderes Prinzip (Code ausführen statt
schätzen): [Quantitativ auswerten](quantitativ-auswerten.md).
