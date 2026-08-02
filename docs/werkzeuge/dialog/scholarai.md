---
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: "eigener GPT: Fortgeschritten"
  kosten: Freemium
  kosten_zusatz: eigener GPT braucht ein ChatGPT-Abo
  verarbeitung: Cloud
  wofuer: Literatur im Chat suchen und Volltexte gezielt befragen
  phase: [finden, befragen]
  stand: August 2026
---

# ScholarAI

ScholarAI gibt einem Chat Zugriff auf wissenschaftliche Datenbanken: Es
sucht Arbeiten, holt Volltexte und beantwortet Fragen zu einzelnen
Papers. Damit fällt der häufigste Fehler weg, den ein reiner Chat bei
Literatur macht, nämlich Quellen zu erfinden. Was hier auftaucht, hat
eine URL.

Es gibt zwei Wege dorthin. Der **fertige ScholarAI-GPT** ist ohne
Einrichtung nutzbar, du öffnest ihn und legst los. Ein **eigener Custom
GPT** kostet Einrichtungszeit, lässt sich dafür mit eigenen Instruktionen
auf deine Arbeitsweise zuschneiden und mit weiteren Anbindungen
kombinieren.

## Wofür es taugt

- **Im Chat nach Literatur suchen**, mit verlinkten Treffern statt
  erfundener Referenzen.
- **Volltexte gezielt befragen**: Methode, Datengrundlage, Limitationen,
  statt das ganze PDF zu lesen.
- **Ein Feld über Zitationen erschliessen**, über die Funktion
  `literature_map`.
- **Funde direkt ablegen.** Die Schnittstelle kann Zitate nach
  [Zotero](../sammeln/zotero.md) schreiben.
- **Mehrere Arbeiten in einem Durchgang befragen**, über die
  Projekt-Funktion.

## Einen eigenen GPT einrichten

1. API-Schlüssel unter <https://app.scholarai.io/profile/api> erzeugen
   und kopieren.
2. In ChatGPT einen neuen GPT anlegen, im Reiter `Configure` unten
   "Create a New Action" wählen.
3. Authentifizierung: `API Key`, den Schlüssel einsetzen, Auth Type
   `Custom`, Header-Name `X-ScholarAI-API-Key`.
4. Schema importieren von `https://api.scholarai.io/openapi.yaml`.
5. Instruktion einsetzen, siehe die Bausteine unten.

Die verbindliche, stets aktuelle Anleitung mit Bildschirmfotos:
<https://docs.scholarai.io/make-a-gpt>

## System-Prompt-Bausteine je Einsatzzweck

Setze den passenden Baustein als Instruktion ein oder nutze ihn als
Eröffnungs-Prompt. Alle Bausteine teilen eine Grundregel: **keine Aussage
ohne verlinkte Quelle, keine erfundenen Zitate.**

### 1. Explorativer Überblick

```text
Rolle: Du kartierst ein mir neues Forschungsfeld.
Aufgabe: Finde via search_abstracts die wichtigsten Arbeiten und
Review-Artikel zum Thema. Gib mir eine Landkarte des Feldes.
Ausgabe:
- 3-5 zentrale Arbeiten / Reviews, je mit [Autor et al., Jahr](URL)
- die wichtigsten Teilthemen / Strömungen in Stichworten
- 3 offene Fragen, die ich als nächstes verfolgen könnte
Regel: Keine Aussage ohne verlinkte Quelle.
```

### 2. Gezielte Literatursuche

```text
Rolle: Du bist ein präziser Literatur-Rechercheassistent.
Aufgabe: Beantworte meine Frage ausschliesslich auf Basis von Quellen,
die du via search_abstracts findest. Bei Unsicherheit nutze getFullText
oder question am Paper selbst, statt zu raten.
Ausgabe:
- 5-8 relevante Arbeiten, je mit [Autor et al., Jahr](URL)
- 1 Satz, warum die Arbeit relevant ist
- am Ende: 2-3 offene Anschlussfragen
Regel: Keine Aussage ohne verlinkte Quelle. Keine erfundenen Zitate.
```

### 3. Deep Read (ein Paper tief befragen)

```text
Rolle: Du analysierst eine einzelne Arbeit gründlich.
Aufgabe: Nutze getFullText für das PDF und question für Detailfragen.
Beantworte zu diesem Paper:
- Fragestellung und Kernbeitrag
- Methode und Datengrundlage
- zentrale Ergebnisse
- Limitationen und offene Punkte
Ausgabe: kompakte Stichpunkte, mit Verweis auf Abschnitt/Seite, wo möglich.
Regel: Wenn etwas im Text nicht steht, sag das ausdrücklich.
```

### 4. Synthese / Mini-Review

```text
Rolle: Du vergleichst mehrere Arbeiten und synthetisierst.
Aufgabe: Für die folgenden Papers (oder deine Suchtreffer):
- stelle die Befunde gegenüber
- markiere Übereinstimmungen und Widersprüche
- benenne Forschungslücken
Ausgabe:
- Vergleichstabelle (Arbeit | Befund | Methode | Einschränkung)
- 1 Absatz Synthese
- 3 Lücken / Anschlussfragen
Regel: Jede Zeile mit verlinkter Quelle. Widersprüche nicht glätten.
```

### 5. Zitations-Verfolgung

```text
Rolle: Du zeichnest die Entwicklung eines Feldes nach.
Aufgabe: Ausgehend von der genannten Arbeit, nutze literature_map /
verwandte Arbeiten, um frühere Grundlagen und spätere Weiterentwicklungen
zu finden.
Ausgabe:
- "Baut auf" (Prior Works), 3-5 Arbeiten mit Link
- "Wurde weiterentwickelt in" (Derivative Works), 3-5 Arbeiten mit Link
- 1 Satz, wie sich das Feld über die Zeit verschoben hat
Regel: Keine Aussage ohne verlinkte Quelle.
```

**Templates als Ausgabeformat.** Du kannst dem GPT zusätzlich ein festes
Ausgabeformat vorgeben, etwa Markdown für dein
[LLM-Wiki](../sammeln/llm-wiki.md) oder eine Struktur, die direkt nach
[Notion](../sammeln/notion.md) oder [Zotero](../sammeln/zotero.md) passt.
So sind Funde ohne Nacharbeit ablagefertig.

## Grenzen

- **An ChatGPT gebunden.** ScholarAI wird als Action eingebunden, nicht
  über den offenen [MCP-Standard](../../grundlagen/llm-einspannen.md).
  Wer mit einem anderen Chat-Programm arbeitet, kann es so nicht nutzen.
- **Ein eigener GPT braucht Pflege.** Der Anbieter aktualisiert das
  Schema; nach einem Funktionsupdate muss man es im eigenen GPT von Hand
  neu importieren, sonst fehlen neue Funktionen stillschweigend.
- **Die Schnittstelle ist als Alpha gekennzeichnet.** Verhalten und
  Umfang können sich ändern.
- **Verlinkt heisst nicht geprüft.** Die Quellen existieren, aber ob die
  Zusammenfassung sie richtig wiedergibt, siehst du erst im Original.
- **Cloud-Dienst über ChatGPT.** Für die Einordnung siehe die
  [Grundregel zum Datenschutz](../../grundlagen/datenschutz.md); zusätzlich
  lohnt ein Blick in die ChatGPT-Einstellungen zur Trainingsnutzung.

## Wann etwas anderes passt

Wenn du nicht im Chat, sondern in einer Oberfläche mit Tabellen arbeiten
willst, nimmt [Elicit](../finden/elicit.md) dir mehr ab. Geht es um deine
*eigenen* PDFs statt um den Korpus, ist
[Gemini Notebook](gemini-notebook.md) einfacher. Und für die blosse Suche
ohne Chat ist [Semantic Scholar](../finden/semantic-scholar.md) direkter.

Fertiger GPT: <https://chatgpt.com/g/g-L2HknCZTC-scholar-ai> ·
Anleitung: <https://docs.scholarai.io/make-a-gpt> ·
Anbieter: <https://scholarai.io>

---

Statt Quellen anzubinden, kannst du auch nur mit deinen eigenen
Dokumenten chatten: [Gemini Notebook](gemini-notebook.md).
