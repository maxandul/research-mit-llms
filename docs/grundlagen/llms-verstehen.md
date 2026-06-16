# LLMs verstehen & verantwortungsvoll nutzen

Bevor es um einzelne Werkzeuge geht: ein kurzer Blick darauf, *was* ein LLM
eigentlich tut, wo seine Staerken und Grenzen liegen — und welche Verantwortung
beim Forschen unteilbar bei dir bleibt.

## Wie ein LLM grob funktioniert

Vereinfacht setzt ein LLM (grosses Sprachmodell) Text fort: Es sagt, Schritt
fuer Schritt, das wahrscheinlich naechste Wort voraus — gelernt aus sehr grossen
Textmengen. Einen geprueften Faktenspeicher, den es gezielt abfragt, gibt es
dabei nicht.

"Wahrscheinlichkeit" ist hier aber nicht trivial. Um gut vorherzusagen, hat das
Modell im Training enorm viel verdichtet: sprachliche Regeln, Sachzusammenhaenge,
Argumentationsmuster. Es plappert also nicht einzelne Phrasen nach, sondern
verarbeitet komplexe Zusammenhaenge — in diesem Sinn steckt in den "Mustern" eine
Menge impliziten Wissens. Wie weit das an echtes Verstehen heranreicht oder in Zukunft 
heranreichen wird, ist eine offene Debatte (der Philosoph Markus Gabriel zum Beispiel 
sieht darin heute schon deutlich mehr als blosse Autovervollstaendigung). 

Fuer die aktuelle Praxis folgen aber weiterhin gewisse Staerken und Grenzen daraus:

## Wo LLMs stark sind

Stark ist ein LLM dort, wo es um das Verarbeiten und Umformen von *Sprache*
geht — nicht um die Wahrheit einer Aussage, sondern um ihre Form. Konkret etwa:
explorieren, strukturieren, verdichten, umformulieren, spiegeln, zuspitzen,
variieren, explizieren (siehe die Rollenteilung unten).

## Wo LLMs schwaecheln

Schwach ist es genau dort, wo Sprache und Wahrheit auseinanderfallen:

- **Fakten, Zahlen, Daten:** koennen schlicht falsch sein — und klingen trotzdem
  ueberzeugend.
- **Quellen:** werden mitunter frei erfunden (Titel, Autor:innen, sogar DOIs).
- **Aktualitaet:** das Wissen hat einen Stichtag; Neueres fehlt, ausser das Tool
  sucht aktiv im Web.
- **Urteil:** es hat kein echtes Verstaendnis und traegt keine Verantwortung —
  es wirkt nur so.
- **Verzerrungen:** es spiegelt Schieflagen und Luecken seiner Trainingsdaten.

!!! quote "Der gemeinsame Nenner"
    Weil das Modell Muster fortsetzt, statt zu wissen, klingt Falsches oft
    genauso fluessig und ueberzeugend wie Richtiges. Die Form ist kein Beleg
    fuer den Gehalt.

## Grundregel: selbst pruefen

!!! warning "Nicht delegierbar"
    Alles Belegrelevante — Fakten, Zahlen, Zitate, Quellen — selbst
    gegenpruefen. Ein LLM liefert Entwuerfe und Zuarbeit, keine verlaesslichen
    Belege. Was du uebernimmst, verantwortest du.

## Rollenteilung: was sich delegieren laesst — und was nicht

Wissenschaftliches Arbeiten lebt von einer klaren Trennung. Ein LLM kann die
Zuarbeit uebernehmen; das Urteil bleibt bei den Forschenden.

| Die KI unterstuetzt beim … | Die Forschenden … |
|----------------------------|-------------------|
| Explorieren                | Entscheiden       |
| Strukturieren              | Bewerten          |
| Verdichten                 | Pruefen           |
| Umformulieren              | Einordnen         |
| Spiegeln                   | Verknuepfen       |
| Zuspitzen                  | Interpretieren    |
| Variieren                  | Begruenden        |
| Explizieren                | Verantworten      |

Die linke Spalte ist Zuarbeit und laesst sich delegieren. Die rechte Spalte
bleibt bei den Forschenden — sie ist der Kern wissenschaftlicher Verantwortung
und nicht delegierbar.

!!! note "Keine feste Zuordnung"
    Die Zeilen sind keine Paare: "Explorieren" gehoert nicht exklusiv zu
    "Entscheiden". Es sind zwei gegenuebergestellte Verantwortungsbereiche,
    nicht acht 1:1-Beziehungen.

---

Wie du ein LLM konkret einbindest — im Chat, mit Werkzeugen oder als
Wissensbasis — zeigt die naechste Seite:
[Drei Arten, LLMs zu nutzen](llm-research.md).
