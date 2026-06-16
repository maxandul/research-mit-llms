# RAG vs. LLM-Wiki

Ein zentraler Denkansatz, der erklaert, warum eine wachsende Wissensbasis
oft besser ist als das uebliche "Dokumente hochladen und fragen".

## Der uebliche Weg: RAG

Bei **RAG** (Retrieval-Augmented Generation) laedst du Dokumente hoch, und
das Modell sucht bei *jeder* Frage erneut die passenden Stellen heraus und
formuliert eine Antwort. So arbeiten die meisten "Chatte mit deinen PDFs"-
Werkzeuge.

- Funktioniert gut fuer Einzelfragen.
- Aber: Es baut sich nichts auf. Bei jeder Frage faengt das Modell von vorn
  an. Eine Erkenntnis, die fuenf Quellen verbindet, muss jedes Mal neu
  zusammengesetzt werden.

## Der andere Weg: das LLM-Wiki

Die Idee stammt von Andrej Karpathy: Statt nur abzurufen, pflegt das LLM
eine **bestehende, verlinkte Wissensbasis** aus Markdown-Dateien. Kommt eine
neue Quelle dazu, liest das Modell sie, traegt das Wichtige in vorhandene
Seiten ein, aktualisiert Querverweise und notiert Widersprueche.

- Das Wissen wird *einmal* verdichtet und dann *aktuell gehalten* — nicht
  bei jeder Frage neu hergeleitet.
- Die Wissensbasis wird mit jeder Quelle reicher.

!!! quote "Kernunterschied"
    RAG ruft ab und vergisst. Ein Wiki sammelt an und verdichtet.

## Wann was?

| Situation | Besser geeignet |
|-----------|-----------------|
| Schnelle Einzelfrage an ein paar PDFs | RAG / Chat mit Dokumenten |
| Laufendes Projekt ueber Wochen/Monate | LLM-Wiki |
| Kleine Materialmenge (grob unter ~150 Seiten) | Wiki/Kontext reicht oft ohne RAG |
| Sehr grosse Materialmengen | RAG noetig |

Mehr zur praktischen Umsetzung: [LLM-Wiki nach Karpathy](../werkzeuge/sammeln/llm-wiki.md).

## Quelle

- Andrej Karpathy, *llm-wiki* (Original-Idee als GitHub Gist):
  <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
