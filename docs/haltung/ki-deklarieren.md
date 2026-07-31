# KI-Nutzung deklarieren

Die [Rollenteilung](../grundlagen/llms-verstehen.md) endet bei einem Wort:
**Verantworten**. Wer LLMs nutzt und die Verantwortung für den Text trägt,
für den ist Transparenz keine lästige Pflicht, sondern die logische
Konsequenz. Deklariert wird nicht, weil man erwischt werden könnte, sondern
weil Offenlegen zur wissenschaftlichen Redlichkeit gehört, genau wie das
Zitieren von Quellen.

!!! quote "Die Haltung dahinter"
    Wer seine Werkzeuge sauber einsetzt, hat nichts zu verstecken. Eine
    Deklaration ist kein Schuldeingeständnis, sondern ein Qualitätsmerkmal:
    Sie zeigt, dass du deinen Prozess im Griff hast und ihn überprüfbar machst.

## Was deklarieren?

Als Faustregel: alles, was das Ergebnis inhaltlich mitgeprägt hat.

**Deklarationswürdig ist typischerweise:**

- Textentwürfe oder Überarbeitungen durch ein LLM (auch Teilkapitel)
- LLM-gestützte [Codierung qualitativer Daten](../analysieren/qualitativ-codieren.md)
  (gehört zusätzlich ins Methodenkapitel: Modell, Codebuch, Prüfschritte)
- LLM-gestützte [Datenauswertung](../analysieren/quantitativ-auswerten.md)
  (Code als Analyseprotokoll aufheben)
- Literaturrecherche über LLM-Werkzeuge, wenn sie die Quellenauswahl
  geprägt hat
- [Transkription](../erheben/transkription.md) mit KI-Werkzeugen

**Meist nicht deklarationspflichtig** (Vorgaben der Institution prüfen):
Rechtschreib-, Grammatik- und Stilkorrektur an selbst verfasstem Text.
Springer Nature nennt das "AI assisted copy editing" und nimmt es explizit
von der Deklarationspflicht aus; Elsevier und die UZH ziehen die Grenze
analog zwischen generativen und nicht-generativen Hilfsmitteln. Aber: Sobald
die KI Textteile **substanziell umstrukturiert oder neu erzeugt**, ist die
Grenze überschritten und es gilt Deklarationspflicht.

## Wie deklarieren?

Zwei Orte, je nach Rolle der KI:

1. **Eigenständigkeitserklärung / Verzeichnis der Hilfsmittel:** kompakte
   Übersicht, welche Werkzeuge wofür eingesetzt wurden.
2. **Methodenkapitel:** wenn die KI Teil der Methode war (Codieren,
   Auswerten, Transkribieren), gehört sie dorthin, so präzise beschrieben,
   dass jemand das Vorgehen nachvollziehen könnte.

Beispielformulierung für die Erklärung:

```text
Beim Erstellen dieser Arbeit habe ich folgende KI-Werkzeuge eingesetzt:

- Claude (Anthropic): Überarbeitung eigener Textentwürfe in den Kapiteln 2
  und 5 (Verständlichkeit, Struktur); Vorschläge wurden geprüft und
  selektiv übernommen.
- ChatGPT (OpenAI): deskriptive Auswertung der Fragebogendaten (Kap. 4);
  der ausgeführte Analysecode liegt im Anhang B.
- TranscriboZH (lokal): Transkription der Interviews; alle Transkripte
  wurden gegengehört und korrigiert.

Die inhaltliche Verantwortung für alle Aussagen, Auswertungen und
Schlussfolgerungen liegt bei mir.
```

!!! tip "Faustregel für den Detailgrad"
    Deklariere so, dass bei einer Nachfrage im Kolloquium nichts zum
    Vorschein kommt, was überrascht. Wenn du zögerst, ob etwas erwähnt
    werden muss: erwähnen.

## Warum Deklarieren trotzdem manchmal schwerfällt

Ehrlicherweise: Deklaration ist nicht gratis. Eine Serie von 13 Experimenten
zeigt, dass Personen, die ihre KI-Nutzung offenlegen, zunächst *weniger*
vertraut wird als solchen, die schweigen — das sogenannte Transparenz-Dilemma
(Schilke & Reimann 2025). Das erklärt, warum viele zögern. **An der Sache
ändert es nichts:** Redlichkeit ist keine Abwägung. Wer KI verwendet,
deklariert sie — alles andere ist mit dem Transparenzgedanken
wissenschaftlichen Arbeitens nicht vereinbar, unabhängig davon, wie die
Offenlegung ankommt.

Wer es dennoch als Rechnung sehen will, kommt zum selben Schluss: Dieselbe
Forschung zeigt, dass aufgedeckte *verschwiegene* Nutzung dem Vertrauen
mehr schadet als freiwillige Offenlegung. Und sie wird aufgedeckt: Die
Academ-AI-Fallsammlung dokumentiert Hunderte publizierter Arbeiten mit
stehengebliebenen Chatbot-Phrasen, bis in Journals renommierter Verlage
(Glynn 2024) — bei inzwischen alltäglicher LLM-Nutzung (je nach Fachgebiet
trugen 2024 bis gegen 22% der Papers LLM-Spuren; Liang et al. 2025). Die
ICMJE-Empfehlungen stufen Nichtdeklaration ausdrücklich als möglichen Fall
von **wissenschaftlichem Fehlverhalten** ein.

## Vorgaben prüfen

Die Haltung kommt zuerst, aber die Formalien setzt deine Institution:

- **Hochschule / Fakultät:** Viele haben inzwischen Richtlinien oder
  Merkblätter zu generativer KI, teils mit vorgegebenen
  Deklarationsformularen. Vor der Abgabe prüfen, im Zweifel die
  Betreuungsperson fragen.
- **Journals / Verlage:** ICMJE, COPE und alle grossen Verlage verlangen
  eine Offenlegung im Manuskript (im Methodenteil bzw. einer eigenen
  Deklarationssektion) und schliessen LLMs einhellig als Co-Autoren aus,
  weil sie keine Verantwortung übernehmen können. Elsevier stellt dafür
  einen Mustertext bereit, Details in den Quellen unten.
- **Ethikkommissionen:** Bei Datenauswertung mit Cloud-Diensten kann die
  KI-Nutzung Teil des Ethikantrags sein, siehe
  [Daten anonymisieren](../erheben/anonymisieren.md).

## Was die Deklaration nicht ersetzt

Deklarieren macht den Einsatz transparent, nicht automatisch gut. Die
Grundregeln gelten weiterhin: alles Belegrelevante selbst prüfen, Urteil
und Interpretation nicht delegieren, Datenschutz einhalten. Die Deklaration
ist der letzte Schritt eines sauberen Prozesses, nicht sein Ersatz.

!!! evidenz "Evidenz zuletzt geprüft: Juli 2026"
    Die Belege zu dieser Seite sind im
    [Forschungsstand: KI-Nutzung deklarieren](../wiki/synthese/ki-deklarieren.md)
    zusammengefasst; dort steht auch, worin die Quellen übereinstimmen und
    was offen ist.

## Quellen

**Policies (Original massgeblich, ändern sich laufend):**

- ICMJE, *Use of AI by Authors* (Empfehlungen, Abschnitt V.A):
  <https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html>
  · [Notiz](../wiki/quellen/icmje-ki-nutzung-autoren.md)
- COPE, *Authorship and AI tools* (Positionspapier):
  <https://doi.org/10.24318/cCVRZBms>
  · [Notiz](../wiki/quellen/cope-autorschaft-ki.md)
- Elsevier, *Generative AI policies for journals* (inkl. Mustertext, Stand Juni 2026):
  <https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals>
  · [Notiz](../wiki/quellen/elsevier-genai-policy.md)
- Springer Nature, *Artificial Intelligence (AI)* (inkl. Copy-Editing-Ausnahme):
  <https://www.nature.com/nature-portfolio/editorial-policies/ai>
  · [Notiz](../wiki/quellen/springer-nature-ki-policy.md)
- Universität Zürich, *Empfehlungen zum Umgang mit generativer KI* (inkl.
  Mustertext für die Eigenständigkeitserklärung):
  <https://www.uzh.ch/de/explore/basics/ai/recommendations.html>
  · [Notiz](../wiki/quellen/uzh-empfehlungen-genki.md)

**Studien:**

- Schilke & Reimann (2025), *The transparency dilemma*, Organizational
  Behavior and Human Decision Processes — peer-reviewed:
  <https://doi.org/10.1016/j.obhdp.2025.104405>
  · [Notiz](../wiki/quellen/schilke-reimann-2025-transparenz-dilemma.md)
- Liang et al. (2025), *Quantifying large language model usage in scientific
  papers*, Nature Human Behaviour — peer-reviewed:
  <https://www.nature.com/articles/s41562-025-02273-8>
  · [Notiz](../wiki/quellen/liang-2025-llm-praevalenz.md)
- Glynn (2024, rev. 2025), *Academ-AI* — Preprint:
  <https://arxiv.org/abs/2411.15218>
  · [Notiz](../wiki/quellen/glynn-2024-academ-ai.md)

**Überblick Schweiz (Praxis):**

- Scribbr, *Die ChatGPT-Richtlinien der 23 Schweizer Hochschulen*:
  <https://www.scribbr.ch/ki-tools-nutzen-ch/chatgpt-richtlinien-hochschulen-schweiz/>
  · [Notiz](../wiki/quellen/scribbr-2024-ch-hochschulen.md)

---

Damit ist der Rundgang durch den Forschungsprozess komplett. Wie diese
Seite selbst zu ihren Belegen kommt, zeigt der
[Forschungsstand](../wiki/index.md); kopierfertige Prompts für alle Phasen
sammelt die [Prompt-Bibliothek](../ressourcen/prompt-bibliothek.md).
