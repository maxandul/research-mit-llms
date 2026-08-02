# LLMs verstehen & verantwortungsvoll nutzen

Bevor es um einzelne Werkzeuge geht: ein kurzer Blick darauf, *was* ein LLM
eigentlich tut, wo seine Stärken und Grenzen liegen, und welche Verantwortung
beim Forschen bei dir bleibt.

## Wie ein LLM grob funktioniert

Vereinfacht setzt ein LLM (grosses Sprachmodell) Text fort: Es sagt, Schritt
für Schritt, das wahrscheinlich nächste Wort voraus, gelernt aus sehr grossen
Textmengen. Einen geprüften Faktenspeicher, den es gezielt abfragt, gibt es
dabei nicht.

"Wahrscheinlichkeit" ist hier aber nicht trivial. Um gut vorherzusagen, hat das
Modell im Training viel verdichtet: sprachliche Regeln, Sachzusammenhänge,
Argumentationsmuster. Es reiht also nicht einzelne Phrasen aneinander, sondern
verarbeitet komplexe Zusammenhänge. In diesem Sinn steckt in den "Mustern" eine
Menge impliziten Wissens.

Ob das schon "Verstehen" ist, ist umstritten. Für die einen ist ein LLM eine
blosse Autovervollständigung, die Zeichen an Zeichen reiht, ohne etwas zu meinen.
Andere, etwa der Philosoph Markus Gabriel, halten das für zu kurz gegriffen: In
den Mustern der Sprache stecke unser Denken, Werten und Fühlen, das ein Modell
teils erfasse, ohne je verstehen zu müssen, *warum*. Vielleicht ist "nur
Autovervollständigung oder echtes Verstehen" also schon die falsche Frage.

Für die Praxis muss man diese Debatte gar nicht entscheiden. Denn wie man das
Erfassen der Muster auch nennt: Ein LLM lernt aus *Regelmässigkeiten der
Sprache*, nicht durch einen Abgleich mit der Welt. Daraus ergeben sich für den
Einsatz in der Forschung folgende Stärken und Schwächen:

## Wo LLMs stark sind

Stark ist ein LLM dort, wo es um *Sprache* selbst geht, ums Verarbeiten und
Umformen, wo also eine gut passende Formulierung schon das Ziel ist. Konkret
etwa: explorieren, strukturieren, verdichten, umformulieren, spiegeln,
zuspitzen, variieren, explizieren (siehe die Rollenteilung unten).

## Wo LLMs schwächeln

Schwach ist es dort, wo es auf den Abgleich mit der Wirklichkeit ankommt, wo
gut klingen und stimmen auseinanderfallen:

- **Fakten, Zahlen, Daten:** können schlicht falsch sein und klingen trotzdem
  überzeugend.
- **Quellen:** werden mitunter frei erfunden (Titel, Autor:innen, sogar DOIs).
- **Aktualität:** das Wissen hat einen Stichtag; Neueres fehlt, ausser das Tool
  sucht aktiv im Web.
- **Urteil:** es hat kein echtes Verständnis und trägt keine Verantwortung,
  es wirkt nur so.
- **Verzerrungen:** es spiegelt Schieflagen und Lücken seiner Trainingsdaten.

!!! merksatz "Der gemeinsame Nenner"
    Weil das Modell Muster fortsetzt, statt zu wissen, klingt Falsches oft
    genauso flüssig und überzeugend wie Richtiges. Die Form ist kein Beleg
    für den Gehalt.

## Grundregel: selbst prüfen

Alles Belegrelevante, also Fakten, Zahlen, Zitate und Quellen, gehört
gegengeprüft, bevor du es übernimmst.

Wie nötig das ist, zeigen die bisher gesichteten Studien. In einem
Experiment mit ChatGPT-generierten Forschungsanträgen hatten 38 Prozent
der Referenzen falsche DOIs, 16 Prozent existierten gar nicht. In einem
Schreibexperiment reichten 68 Prozent der Teilnehmenden LLM-Output
unbearbeitet ein. Die Werte stammen aus einem Review über Studien von
2019 bis 2025, hängen also an älteren Modellgenerationen; aussagekräftig
ist die Grössenordnung, nicht die einzelne Zahl.

Eine Einschränkung, die nicht an der Modellgeneration hängt: Prüfen
findet die auffälligen Fehler, also erfundene Quellen und falsche Zahlen.
Verzerrte Auswahl und plausible Fehlinterpretationen findet es nicht
zuverlässig.

!!! warnung "Nicht delegierbar"
    Was du übernimmst, verantwortest du. Ein LLM liefert Entwürfe und
    Zuarbeit, keine Belege.

## Was das Auslagern kostet

Ein LLM kann strukturieren, spiegeln, verdichten und Anschlussfragen
formulieren. Das Urteil nimmt es nicht ab. Ob und wie stark sich das
Auslagern von Zwischenschritten auf das eigene Verstehen auswirkt, ist
bisher wenig untersucht; ein Recherche-Sprint dazu ist geplant.

## Rollenteilung: was sich delegieren lässt und was nicht

Wissenschaftliches Arbeiten lebt von einer klaren Trennung. Ein LLM kann die
Zuarbeit übernehmen; das Urteil bleibt bei den Forschenden.

| Die KI unterstützt beim … | Die Forschenden … |
|---------------------------|-------------------|
| Explorieren               | Entscheiden       |
| Strukturieren             | Bewerten          |
| Verdichten                | Prüfen            |
| Umformulieren             | Einordnen         |
| Spiegeln                  | Verknüpfen        |
| Zuspitzen                 | Interpretieren    |
| Variieren                 | Begründen         |
| Explizieren               | Verantworten      |

Die linke Spalte lässt sich delegieren, die rechte nicht. Aus dem letzten
Wort, dem Verantworten, folgt auch die Transparenz gegenüber anderen:
siehe [KI-Nutzung deklarieren](../haltung/ki-deklarieren.md).

!!! randnotiz "Keine feste Zuordnung"
    Die Zeilen sind keine Paare: "Explorieren" gehört nicht exklusiv zu
    "Entscheiden". Es sind zwei gegenübergestellte Verantwortungsbereiche,
    nicht acht 1:1-Beziehungen.

Die Rollenteilung ist keine Setzung dieser Website. Sie ist der
Konsenskern der bisherigen Debatte: Auch Positionen, die sich über den
Nutzen von LLMs in der Forschung heftig streiten, sind sich einig, dass
Verantwortung, Urteil und Verstehen beim Menschen bleiben.

!!! evidenz "Evidenz zuletzt geprüft: Juli 2026"
    Die Belege sind im
    [Forschungsstand: LLMs verstehen](../wiki/synthese/llms-verstehen.md)
    zusammengefasst; die mechanischen Einzelaussagen der Grundlagen folgen
    mit einem eigenen Recherche-Sprint.

## Quellen

- Binz et al. (2025), *How should the advancement of large language
  models affect the practice of science?*, PNAS — peer-reviewed:
  <https://doi.org/10.1073/pnas.2401227121>
  · [Notiz](../wiki/quellen/binz-2025-llms-praxis-wissenschaft.md)
- Mabirizi et al. (2025), *A systematic review of the impact of
  generative AI on postgraduate research* — peer-reviewed:
  <https://doi.org/10.1007/s44163-025-00495-3>
  · [Notiz](../wiki/quellen/mabirizi-2025-genai-postgrad-review.md)
- Eger et al. (2026), *Transforming Science with Large Language Models* —
  Preprint: <https://arxiv.org/abs/2502.05151>
  · [Notiz](../wiki/quellen/eger-2026-transforming-science-survey.md)

---

Zwei Anschlüsse: Die mechanischen Eigenheiten hinter diesen Stärken und
Schwächen erklärt [Wie ein LLM arbeitet](wie-llms-arbeiten.md). Die fünf
Wege, dem Modell eigenes Material zugänglich zu machen, zeigt
[Wie du ein LLM einspannst](llm-einspannen.md).
