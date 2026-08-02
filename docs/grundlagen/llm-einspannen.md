# Wie du ein LLM einspannst

Ein Modell kann von sich aus nur, was in seinen Trainingsdaten steckte.
Alles andere musst du ihm zugänglich machen. Dafür gibt es fünf Wege, mit
steigendem Aufwand und steigendem Nutzen bei grösseren Projekten.

Die Begriffe werden oft in einen Topf geworfen. Vor allem "Datei
hochladen" ist *nicht* automatisch RAG, und der Unterschied entscheidet,
welche Fragen gut beantwortet werden.

## 1. Reiner Chat

Du stellst einem Modell (ChatGPT, Claude, Gemini) eine Frage und bekommst
eine Antwort aus dem Trainingswissen. Kein eigenes Material im Spiel.

- **Vorteile:** Sofort verfügbar. Gut zum Brainstormen, Erklären und
  Formulieren.
- **Nachteile:** Das Wissen hat einen Stichtag, das Modell kennt deine
  Dokumente nicht und kann Quellen erfinden.

## 2. Datei direkt in den Chat (Kontext)

Du lädst eine Datei hoch. Der gesamte Text wird ins
[Kontextfenster](kontextfenster.md) gelegt und das Modell liest ihn
komplett mit. Kein Embedding, keine Datenbank, keine Zwischenstufe.

- **Vorteile:** Am einfachsten. Das Modell sieht den *ganzen* Text,
  nichts geht durch Zerstückeln verloren. Passt für "fasse das Dokument
  zusammen" und für Fragen, die das ganze Dokument betreffen.
- **Nachteile:** Begrenzt durch die Grösse des Kontextfensters. Viele
  oder sehr grosse Dokumente passen nicht hinein. Bei jeder neuen
  Unterhaltung musst du die Datei neu laden. Bei sehr viel Material
  übersieht das Modell eher Details in der Mitte.

## 3. Angebundene Werkzeuge (MCP)

Das Modell ruft während des Gesprächs externe Dienste auf: eine
Literaturdatenbank durchsuchen, ein PDF lesen, in deine
Zotero-Bibliothek schreiben. So arbeitet etwa ein
[Custom GPT mit ScholarAI](../werkzeuge/dialog/scholarai.md). Auch die
Code-Ausführung beim
[quantitativen Auswerten](../analysieren/quantitativ-auswerten.md) gehört
hierher: Das Modell ruft eine Programmier-Umgebung auf, statt selbst zu
"rechnen".

Damit nicht jeder Anbieter eigene Anbindungen erfindet, gibt es dafür
einen offenen Standard, **MCP** (Model Context Protocol). Ein MCP-Server
stellt die Funktionen eines Dienstes als Werkzeuge bereit, die jedes
MCP-fähige Chat-Programm nutzen kann. Wie das eingerichtet wird, zeigt
die Seite [Zotero](../werkzeuge/sammeln/zotero.md), wo das LLM Referenzen
und PDFs direkt in der Literaturverwaltung ablegt.

- **Vorteile:** Aktuelle, belegbare Antworten mit echten Quellen. Zugriff
  auf deine eigenen Daten, und verlässliches Rechnen über ausgeführten
  Code.
- **Nachteile:** Einrichtung nötig. Die Qualität hängt an den
  angebundenen Quellen.

## 4. RAG (Embedding und Retrieval)

Die Dokumente werden in Häppchen (Chunks) zerlegt, jedes wird in einen
Vektor umgewandelt (**Embedding**) und in einer Vektordatenbank
gespeichert. Bei einer Frage wird auch die Frage in einen Vektor
umgewandelt, die ähnlichsten Häppchen werden gesucht und *nur diese* in
den Kontext gegeben.

- **Vorteile:** Skaliert auf Mengen, die nie ins Kontextfenster passen
  würden. Es wird nur das Relevante geladen.
- **Nachteile:** Mehr Technik nötig. Das Modell sieht immer nur
  Ausschnitte, nie das ganze Dokument. Fragen, die viele verstreute
  Stellen verbinden, oder Vergleiche über den ganzen Bestand sind
  schwierig. Das Zerstückeln kann Zusammenhänge zerschneiden, und die
  Suche kann relevante Stellen verfehlen.

## 5. LLM-Wiki

Statt bei jeder Frage abzurufen, pflegt das LLM eine bestehende,
verlinkte Wissensbasis aus Markdown-Dateien. Kommt eine neue Quelle
dazu, liest das Modell sie, trägt das Wichtige in vorhandene Seiten ein,
aktualisiert Querverweise und notiert Widersprüche. Die Idee stammt von
Andrej Karpathy; eine fertige Umsetzung mit Schema, Befehlen und Setup
gibt es im
[llm-wiki-Repo von Mehmet Goekce](https://github.com/mehmetgoekce/llm-wiki).

Der Unterschied zu den Wegen 2 und 4 liegt nicht in der Technik, sondern
darin, was am Ende bleibt: Kontext und RAG geben dem Modell Dokumente
zum Abrufen und vergessen sie danach. Ein Wiki verdichtet sie zu Wissen,
das beim nächsten Mal schon da ist.

- **Vorteile:** Das Wissen wird einmal verdichtet und dann aktuell
  gehalten. Querverweise und Widersprüche sind schon eingearbeitet. Die
  Wissensbasis wird mit jeder Quelle reicher.
- **Nachteile:** Mehr Pflege, je nach Variante etwas Technik (siehe
  [LLM-Wiki nach Karpathy](../werkzeuge/sammeln/llm-wiki.md)). Fehler in
  den Notizen müssen regelmässig geprüft werden.

## Was steckt hinter "Datei hochladen"?

Das hängt vom Werkzeug ab und ist oft nicht sichtbar. Kleine Dateien
werden in vielen Chat-Oberflächen einfach in den Kontext geladen (Weg 2).
Bei grossen oder vielen Dokumenten schaltet sich im Hintergrund RAG dazu
(Weg 4). Werkzeuge wie
[Gemini Notebook](../werkzeuge/dialog/gemini-notebook.md) arbeiten typischerweise
mit Retrieval. Im Zweifel nachschauen, wie das jeweilige Werkzeug mit den
Quellen umgeht.

## Wann was?

| Situation | Weg |
|-----------|-----|
| Frage aus Allgemeinwissen, kein eigenes Material | 1. Reiner Chat |
| Ein einzelnes Dokument befragen oder zusammenfassen | 2. Datei in den Chat |
| Kleine Materialmenge, grob bis 100 bis 200 Seiten | 2. Kontext, zuverlässiger als RAG |
| Das Modell soll suchen, rechnen oder in deine Ablage schreiben | 3. Angebundene Werkzeuge |
| Sehr grosse Materialmengen, viele Dokumente oder tausende Seiten | 4. RAG |
| Laufendes Projekt über Wochen, Wissen soll sich anhäufen | 5. LLM-Wiki |

## Quellen

- Andrej Karpathy, *llm-wiki* (Original-Idee als GitHub Gist):
  <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Mehmet Goekce, *llm-wiki* (Umsetzung mit Claude Code; L1/L2-Architektur,
  Befehle `/wiki ingest`, `/wiki query`, `/wiki lint`; Obsidian oder Logseq):
  <https://github.com/mehmetgoekce/llm-wiki>

---

Alle fünf Wege laufen durch dasselbe Nadelöhr:
[Das Kontextfenster](kontextfenster.md) erklärt, warum mehr Material
nicht automatisch bessere Antworten bedeutet.
