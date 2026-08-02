---
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: je nach Variante bis Profi
  kosten: gratis
  kosten_zusatz: je nach Modell fallen Abo- oder API-Kosten an
  verarbeitung: beides
  verarbeitung_zusatz: hängt am gewählten Modell, mit lokalem Modell komplett offline
  wofuer: Eine vom LLM gepflegte, wachsende Wissensbasis aus Markdown-Dateien
  phase: [verwalten]
  stand: August 2026
---

# LLM-Wiki (nach Karpathy)

Ein LLM-Wiki ist kein Programm, sondern eine Arbeitsweise: Statt bei
jeder Frage neu zu suchen, pflegt ein Modell eine wachsende Sammlung
verlinkter Markdown-Notizen. Kommt eine Quelle dazu, wird sie nicht
abgelegt, sondern eingearbeitet. Der Unterschied zu allen anderen Wegen,
einem Modell Material zu geben, steht unter
[Wie du ein LLM einspannst](../../grundlagen/llm-einspannen.md).

Die Architektur hat drei Schichten:

- **Raw / Quellen**: deine unveränderten Originaldokumente.
- **Wiki**: die vom LLM gepflegten, verlinkten Markdown-Seiten.
- **Schema**: eine Anleitungsdatei (etwa `CLAUDE.md`), die festlegt, wie
  das Wiki strukturiert ist und wie neue Quellen eingepflegt werden.

## Drei Umsetzungsvarianten

Du kannst klein und ganz ohne Technik starten und später automatisieren.

=== "Stufe 1: Händisch (Einsteiger)"

    Nötig sind nur ein Chat-LLM und ein Texteditor.

    - Lege einen Ordner mit Markdown-Dateien an, etwa in Obsidian oder
      direkt in einem Repository.
    - Kopiere Quelltexte in ein Chat-LLM und lass dir Zusammenfassungen
      und Querverweise erzeugen.
    - Füge die Ergebnisse selbst als `.md`-Seiten ein und verlinke sie.

    *Gewinn:* Du verstehst das Prinzip und hast sofort Ergebnisse.
    *Aufwand:* Das Einpflegen machst du von Hand.

=== "Stufe 2: Agentische Anwendung (Fortgeschritten)"

    Nötig ist eine Anwendung, die Dateien lesen und schreiben kann, etwa
    Claude Cowork.

    - Der Agent übernimmt Lesen, Zusammenfassen und Einpflegen
      halb-automatisch.
    - Du kuratierst die Quellen und stellst Fragen, die Pflege läuft mit.

    *Gewinn:* deutlich weniger Handarbeit als Stufe 1.
    *Aufwand:* etwas Einrichtung, kein Programmieren nötig.

=== "Stufe 3: Coding-Agent (Profi)"

    Nötig sind ein Coding-Agent wie Claude Code und Grundkenntnisse im
    Terminal.

    - Der Kreislauf *ingest, query, lint* läuft automatisiert.
    - Optional eigene Such-Werkzeuge, MCP-Anbindung, Prüfskripte.
    - Fertiger Einstieg:
      [llm-wiki von Goekce](https://github.com/mehmetgoekce/llm-wiki) mit
      Schema, Setup und `/wiki`-Befehlen.

    *Gewinn:* auch grosse Wissensbasen bleiben pflegbar.
    *Aufwand:* am höchsten.

## Ein Standard zeichnet sich ab: das Open Knowledge Format

Bisher hat jedes LLM-Wiki seine eigenen Konventionen erfunden. Im Juni
2026 hat Google Cloud dazu eine offene Spezifikation veröffentlicht, das
**Open Knowledge Format (OKF)**, im Juli 2026 gefolgt von Version 0.2.
Sie beschreibt in verbindlicher Form, was Karpathy skizziert hat: ein
Verzeichnis von Markdown-Dateien, jede mit einem kleinen YAML-Block am
Anfang, Querverweise als normale Markdown-Links.

Pflicht ist dabei genau ein Feld, `type`. Alles Weitere ist freiwillig,
eigene Zusatzfelder sind ausdrücklich erlaubt, und Programme, die OKF
lesen, müssen unbekannte Felder und kaputte Links tolerieren. Ein
bestehendes Markdown-Wiki wird damit meist mit wenig Aufwand kompatibel,
ohne seine Struktur aufzugeben.

Interessanter als die Interoperabilität sind für Forschungszwecke die
Felder aus Version 0.2. Sie beantworten Fragen, die sich bei
LLM-gepflegten Notizen ohnehin stellen:

| Feld | Frage |
|------|-------|
| `sources` | Worauf stützt sich diese Notiz? |
| `generated` / `verified` | Wer hat das geschrieben, wer hat es geprüft? |
| `stale_after` | Ab wann ist die Notiz nachzuprüfen? |
| `status` | Ist sie vorläufig, aktuell oder überholt? |

Aus `verified` ergibt sich eine Vertrauensstufe: keine Angabe heisst
ungeprüft, eine Bestätigung durch eine Maschine heisst maschinell
bestätigt, eine durch einen Menschen heisst menschlich geprüft. Wer will,
kann sein Wiki so filtern, dass nur menschlich geprüfte Notizen in eine
Arbeit einfliessen.

!!! randnotiz "Wie neu das ist"
    OKF ist als Entwurf gekennzeichnet und wenige Wochen alt; zwischen
    v0.1 und v0.2 wurden bereits zwei Felder umbenannt. Es ist ein
    Vorschlag mit Gewicht, kein etablierter Standard. Wer heute ein Wiki
    aufbaut, kann die Felder trotzdem übernehmen: Sie sind auch dann
    nützlich, wenn sich OKF nicht durchsetzt, weil sie die eigene
    Qualitätskontrolle maschinell prüfbar machen.

    Das [Forschungsstand-Wiki dieser Website](../../wiki/index.md) ist im
    Juli 2026 auf diese Felder umgestellt worden, ohne die Notizen selbst
    umzuschreiben. Wie das aussieht, steht in
    [CLAUDE.md im Repository](https://github.com/maxandul/research-mit-llms/blob/main/CLAUDE.md).

## Grenzen

- **Fehler pflanzen sich fort.** Was einmal falsch in einer Notiz steht,
  wird beim nächsten Einpflegen als Grundlage genommen. Ein
  regelmässiger Prüflauf ist deshalb Teil der Methode, nicht Kür.
- **Die Verdichtung ist eine Interpretation.** Was in der Notiz landet,
  hat ein Modell aus der Quelle gezogen. Für alles Zitierrelevante gilt
  weiterhin der Abgleich mit dem Original.
- **Es braucht Disziplin statt Technik.** Die Methode scheitert nicht an
  der Werkzeugwahl, sondern daran, dass das Schema nicht eingehalten
  wird und die Struktur nach ein paar Wochen auseinanderläuft.
- **Deine Quellen gehen durch ein Modell.** Bei Cloud-Modellen gilt die
  [Grundregel zum Datenschutz](../../grundlagen/datenschutz.md); für
  sensibles Material kommen lokale Modelle in Frage, dann bleibt alles
  auf dem eigenen Rechner.

## Wann etwas anderes passt

Für einzelne Projekte, bei denen das Wissen nachher nicht gebraucht
wird, ist der Aufwand zu hoch; da genügt eine Datei im Chat oder
[Gemini Notebook](../dialog/gemini-notebook.md). Für reine Referenzen
und Zitate bleibt [Zotero](zotero.md) zuständig, ein Wiki ersetzt es
nicht, sondern liegt darüber.

Karpathys Idee:
<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f> ·
Umsetzung von Goekce: <https://github.com/mehmetgoekce/llm-wiki> ·
OKF-Spezifikation:
<https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf>

Wie so ein Wiki Schritt für Schritt entsteht, zeigt der Workflow
[Eigenes Forschungs-Wiki aufbauen](../../workflows/forschungs-wiki.md);
ein laufendes Beispiel ist der
[Forschungsstand dieser Website](../../wiki/index.md).

---

Was es sonst noch gibt, von Research Rabbit bis scite.ai:
[Weitere Tools im Überblick](../weitere-tools.md).
