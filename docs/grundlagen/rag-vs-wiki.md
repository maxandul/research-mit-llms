# Datei in den Chat, RAG oder LLM-Wiki?

Es gibt drei verschiedene Arten, ein LLM mit eigenen Dokumenten arbeiten zu
lassen. Sie werden oft in einen Topf geworfen — vor allem "Datei hochladen"
ist *nicht* automatisch RAG. Der Unterschied entscheidet, was gut funktioniert
und was nicht.

## 1. Datei direkt in den Chat (Kontext)

Du laedst eine Datei in den Chat. Der gesamte Text wird ins **Kontextfenster**
des Modells gelegt — das Modell liest ihn komplett mit. Kein Embedding, keine
Datenbank, keine Zwischenstufe.

- **Vorteile:** Am einfachsten (Drag & Drop). Das Modell sieht den *ganzen*
  Text — nichts geht durch Zerstueckeln verloren. Ideal fuer "fasse das ganze
  Dokument zusammen" oder Fragen, die das gesamte Dokument betreffen.
- **Nachteile:** Begrenzt durch die Groesse des Kontextfensters — viele oder
  sehr grosse Dokumente passen nicht hinein. Bei jeder neuen Unterhaltung muss
  man die Datei neu laden; es baut sich nichts auf. Bei sehr viel Kontext kann
  das Modell Details "in der Mitte" uebersehen (mehr dazu: [Das Kontextfenster](kontextfenster.md)).

## 2. RAG (Embedding + Retrieval)

Die Dokumente werden in Haeppchen (Chunks) zerlegt, jedes wird in einen Vektor
umgewandelt (**Embedding**) und in einer Vektordatenbank gespeichert. Bei einer
Frage wird die Frage ebenfalls in einen Vektor umgewandelt, die aehnlichsten
Haeppchen werden gesucht und *nur diese* in den Kontext gegeben.

- **Vorteile:** Skaliert auf sehr grosse Mengen (Tausende Dokumente), die nie
  ins Kontextfenster passen wuerden. Es wird nur das Relevante geladen.
- **Nachteile:** Mehr Technik noetig (Embedding-Pipeline, Vektordatenbank). Das
  Modell sieht immer nur Ausschnitte, nie das ganze Dokument — Fragen, die viele
  verstreute Stellen verbinden, oder "vergleiche ueber alles hinweg" sind
  schwierig. Das Zerstueckeln kann Zusammenhaenge zerschneiden, und die Suche
  kann relevante Stellen verfehlen. Es baut sich nichts auf: jede Frage ist ein
  neuer Abruf.

## 3. LLM-Wiki

Statt bei jeder Frage abzurufen, pflegt das LLM eine **bestehende, verlinkte
Wissensbasis** aus Markdown-Dateien. Kommt eine neue Quelle dazu, liest das
Modell sie, traegt das Wichtige in vorhandene Seiten ein, aktualisiert
Querverweise und notiert Widersprueche. Die Idee stammt von Andrej Karpathy.

- **Vorteile:** Das Wissen wird *einmal* verdichtet und dann aktuell gehalten,
  nicht bei jeder Frage neu hergeleitet. Querverweise und Widersprueche sind
  schon eingearbeitet. Die Wissensbasis wird mit jeder Quelle reicher.
- **Nachteile:** Etwas mehr Pflege; je nach Variante etwas Technik noetig
  (siehe [LLM-Wiki nach Karpathy](../werkzeuge/sammeln/llm-wiki.md)). Fehler in
  den Notizen muessen regelmaessig geprueft werden.

!!! quote "Der Kernunterschied"
    Kontext und RAG geben dem Modell Dokumente zum *Abrufen*. Das Wiki
    *verdichtet* sie zu bleibendem Wissen. RAG ruft ab und vergisst — ein Wiki
    sammelt an.

## Was steckt hinter "Datei hochladen"?

Das haengt vom Tool ab — und ist oft nicht sichtbar. Kleine Dateien werden in
vielen Chat-Oberflaechen einfach in den Kontext geladen (Ansatz 1). Bei grossen
oder vielen Dokumenten schaltet sich im Hintergrund RAG dazu (Ansatz 2).
Werkzeuge wie [NotebookLM](../werkzeuge/dialog/notebooklm.md) arbeiten
typischerweise mit Retrieval. Im Zweifel: nachschauen, wie das jeweilige Tool
mit den Quellen umgeht.

## Wann was?

| Situation | Geeignet |
|-----------|----------|
| Ein einzelnes Dokument schnell befragen oder zusammenfassen | Datei in den Chat (Kontext) |
| Kleine Materialmenge (grob bis ~100-200 Seiten) | Kontext reicht meist, zuverlaessiger als RAG |
| Sehr grosse Materialmengen (Tausende Dokumente) | RAG |
| Laufendes Projekt ueber Wochen/Monate, Wissen soll sich anhaeufen | LLM-Wiki |

!!! tip "Faustregel zur Groessenordnung"
    Solange dein Material bequem ins Kontextfenster passt, ist der direkte Weg
    (Ansatz 1) meist einfacher *und* zuverlaessiger als RAG. RAG lohnt sich erst,
    wenn schlicht zu viel Material fuer den Kontext da ist. Fuers Anhaeufen ueber
    Zeit ist das Wiki gedacht.

## Quelle

- Andrej Karpathy, *llm-wiki* (Original-Idee als GitHub Gist):
  <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
