# Qualitative Daten codieren

!!! info "Auf einen Blick"
    **Schwierigkeit:** Einsteiger · **Kosten:** gratis bis Abo ·
    **Wofür:** Interviews und offene Antworten mit einem LLM als zweitem Codierer auswerten

Ein LLM kann beim Codieren qualitativer Daten (Interviews, offene
Fragebogen-Antworten, Feldnotizen) enorm viel Arbeit abnehmen. Der Schlüssel
liegt darin, es als **zweiten Codierer** zu behandeln, nicht als Orakel: Es
macht Vorschläge nach deinem Codebuch, du prüfst und entscheidest.

## Voraussetzungen

- Daten sind [anonymisiert bzw. pseudonymisiert](../erheben/anonymisieren.md),
  bevor irgendetwas in einen Cloud-Dienst geht.
- Ein Chat-Werkzeug wie Claude oder ChatGPT.
- Die Daten als Tabelle (Excel/CSV): eine Zeile pro Aussage oder Segment.

## Der Workflow

### 1. Codebuch definieren

Das Codebuch ist das Herzstück. Pro Code: Name, Definition, ein
Ankerbeispiel und die Abgrenzung zu ähnlichen Codes.

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

!!! warning "Stolperstein: das LLM schätzt über den Daumen"
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

### 5. Ergebnisse zurückführen und dokumentieren

Codes in die Excel-Tabelle übernehmen (per ID zuordnen) und das Vorgehen
fürs Methodenkapitel festhalten: Codebuch-Version, Modell, Prompt,
Prüfschritte. Das gehört auch in die
[Deklaration der KI-Nutzung](../haltung/ki-deklarieren.md).

## Profi-Variante: der Agent arbeitet die Schleife ab

Wer die Vollständigkeit nicht der Disziplin des Modells überlassen will,
lässt einen Coding-Agenten (Claude Code, Cursor) die Tabelle
**programmatisch** Zeile für Zeile durchlaufen: Ein Skript iteriert über
die Zeilen, das LLM codiert nur den Inhalt der jeweils aktuellen Zeile.
Die Schleife garantiert, dass keine Zeile fehlt. Bei hunderten Zeilen ist
das der verlässlichere Weg.

## Alternative: QDA-Software mit KI-Funktionen

Für grosse Projekte oder wenn die Methodik im Zentrum steht, lohnt sich ein
Blick auf etablierte QDA-Software, die inzwischen eigene KI-Funktionen
mitbringt:

- **MAXQDA** (mit "AI Assist"): Zusammenfassungen, Codevorschläge und
  Chat mit den eigenen Dokumenten, eingebettet in die volle
  QDA-Umgebung (Codesystem, Memos, Visualisierungen).
  <https://www.maxqda.com>
- **ATLAS.ti** (mit "AI Coding"): automatische Codierungsvorschläge über
  ganze Dokumente. <https://atlasti.com>

Beides sind kostenpflichtige Programme (viele Hochschulen haben
Campuslizenzen, vorher nachfragen). Der Vorteil gegenüber dem
Chat-Workflow: Codesystem, Fundstellen und Dokumente bleiben in einer
dafür gebauten Umgebung verwaltet. Der Nachteil: weniger Kontrolle über
die Prompts, und die KI-Funktionen laufen ebenfalls über die Cloud, es
gilt also dieselbe [Anonymisierungs-Regel](../erheben/anonymisieren.md).

## Grenzen

- Das LLM codiert nach sprachlicher Ähnlichkeit. Feine Bedeutungen, Ironie
  und kontextabhängige Aussagen prüft besser ein Mensch.
- Interpretation, Theoriebezug und die Synthese der Befunde bleiben bei dir
  (siehe [Rollenteilung](../grundlagen/llms-verstehen.md)).
- Methodisch sauber ist der Einsatz dann, wenn er dokumentiert, geprüft und
  im Methodenteil offengelegt ist.
