# LLMs verstehen & verantwortungsvoll nutzen

Bevor es um einzelne Werkzeuge geht: ein kurzer Blick darauf, *was* ein LLM
eigentlich tut, wo seine Stärken und Grenzen liegen — und welche Verantwortung
beim Forschen unteilbar bei dir bleibt.

## Wie ein LLM grob funktioniert

Vereinfacht setzt ein LLM (großes Sprachmodell) Text fort: Es sagt, Schritt
für Schritt, das wahrscheinlich nächste Wort voraus — gelernt aus sehr großen
Textmengen. Einen geprüften Faktenspeicher, den es gezielt abfragt, gibt es
dabei nicht.

"Wahrscheinlichkeit" ist hier aber nicht trivial. Um gut vorherzusagen, hat das
Modell im Training enorm viel verdichtet: sprachliche Regeln, Sachzusammenhänge,
Argumentationsmuster. Es plappert also nicht einzelne Phrasen nach, sondern
verarbeitet komplexe Zusammenhänge — in diesem Sinn steckt in den "Mustern" eine
Menge impliziten Wissens.

Ob das schon "Verstehen" ist, ist umstritten. Für die einen ist ein LLM eine
blosse Autovervollständigung, die Zeichen an Zeichen reiht, ohne etwas zu meinen.
Andere — etwa der Philosoph Markus Gabriel — halten das für zu kurz gegriffen: In
den Mustern der Sprache stecke unser Denken, Werten und Fühlen, das ein Modell
teils erfasse, ohne je verstehen zu müssen, *warum*. Vielleicht ist "nur
Autovervollständigung oder echtes Verstehen" also schon die falsche Frage.

Für die Praxis muss man diese Debatte gar nicht entscheiden. Denn wie man das
Erfassen der Muster auch nennt: Ein LLM lernt aus *Regelmässigkeiten der
Sprache*, nicht durch einen Abgleich mit der Welt. Daraus ergeben sich für den
Einsatz in der Forschung folgende Stärken und Schwächen:

## Wo LLMs stark sind

Stark ist ein LLM dort, wo es um *Sprache* selbst geht — ums Verarbeiten und
Umformen, wo also gut passende Formulierung schon das Ziel ist. Konkret etwa:
explorieren, strukturieren,
verdichten, umformulieren, spiegeln, zuspitzen, variieren, explizieren (siehe die
Rollenteilung unten).

## Wo LLMs schwächeln

Schwach ist es dort, wo es auf den Abgleich mit der Wirklichkeit ankommt — wo
gut klingen und stimmen auseinanderfallen:

- **Fakten, Zahlen, Daten:** können schlicht falsch sein — und klingen trotzdem
  überzeugend.
- **Quellen:** werden mitunter frei erfunden (Titel, Autor:innen, sogar DOIs).
- **Aktualität:** das Wissen hat einen Stichtag; Neueres fehlt, außer das Tool
  sucht aktiv im Web.
- **Urteil:** es hat kein echtes Verständnis und trägt keine Verantwortung —
  es wirkt nur so.
- **Verzerrungen:** es spiegelt Schieflagen und Lücken seiner Trainingsdaten.

!!! quote "Der gemeinsame Nenner"
    Weil das Modell Muster fortsetzt, statt zu wissen, klingt Falsches oft
    genauso flüssig und überzeugend wie Richtiges. Die Form ist kein Beleg
    für den Gehalt.

## Grundregel: selbst prüfen

!!! warning "Nicht delegierbar"
    Alles Belegrelevante — Fakten, Zahlen, Zitate, Quellen — selbst
    gegenprüfen. Ein LLM liefert Entwürfe und Zuarbeit, keine verlässlichen
    Belege. Was du übernimmst, verantwortest du.

## Partner, nicht Abkürzung

KI kann dir beim Durchgehen helfen — strukturieren, spiegeln, verdichten,
Anschlussfragen formulieren. Sie kann dir **nicht** das eigene Denken und
Urteilen abnehmen. Wer nur die fertige Antwort abholt, verliert genau den
Gewinn des Forschens: den Weg der Erkenntnis selbst zu gehen.

## Rollenteilung: was sich delegieren lässt — und was nicht

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

Die linke Spalte ist Zuarbeit und lässt sich delegieren. Die rechte Spalte
bleibt bei den Forschenden — sie ist der Kern wissenschaftlicher Verantwortung
und nicht delegierbar.

!!! note "Keine feste Zuordnung"
    Die Zeilen sind keine Paare: "Explorieren" gehört nicht exklusiv zu
    "Entscheiden". Es sind zwei gegenübergestellte Verantwortungsbereiche,
    nicht acht 1:1-Beziehungen.

---

Wie du ein LLM konkret einbindest — im Chat, mit Werkzeugen oder als
Wissensbasis — zeigt die nächste Seite:
[Drei Arten, LLMs zu nutzen](llm-research.md).