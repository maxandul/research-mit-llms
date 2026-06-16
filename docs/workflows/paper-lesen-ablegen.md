# Paper lesen & strukturiert ablegen

Ein einzelnes Paper gruendlich verstehen und die Lesenotiz so ablegen, dass
du sie spaeter wiederfindest und wiederverwenden kannst.

!!! abstract "Das Rezept in einem Bild"
    ```
    PDF / DOI  ->  Befragen (Deep Read)  ->  Lesenotiz nach Schema  ->  Ablage
                   ScholarAI / NotebookLM                              Zotero / Notion
    ```

## Ziel

Aus einem einzelnen Paper eine strukturierte, immer gleich aufgebaute
Lesenotiz erzeugen — ohne das Paper jedes Mal neu durchackern zu muessen.

## Beteiligte Werkzeuge

- [ScholarAI](../werkzeuge/dialog/scholarai.md) (Baustein *Deep Read*) oder
  [NotebookLM](../werkzeuge/dialog/notebooklm.md) zum Befragen
- [Zotero](../werkzeuge/sammeln/zotero.md) und/oder
  [Notion](../werkzeuge/sammeln/notion.md) zur Ablage

## Schritte

1. **Paper bereitstellen.** PDF, DOI oder Link zur Hand haben. In ScholarAI
   reicht oft der Titel; in NotebookLM laedst du das PDF als Quelle hoch.
2. **Gruendlich befragen.** Nutze in ScholarAI den Baustein *Deep Read*
   (siehe [ScholarAI-Seite](../werkzeuge/dialog/scholarai.md)) oder stelle in
   NotebookLM gezielte Fragen zum hochgeladenen PDF.
3. **Lesenotiz nach festem Schema erzeugen.** Gib dem Modell das Schema unten
   vor, damit jede Notiz gleich aufgebaut ist.
4. **Pruefen.** Stimmen die Aussagen mit dem Originaltext? Sind Seiten- bzw.
   Abschnittsverweise plausibel? Nichts erfunden?
5. **Ablegen.** Notiz nach Notion (als Datenbankeintrag) oder als Anhang/Notiz
   zur Referenz in Zotero. Bei einem [LLM-Wiki](../werkzeuge/sammeln/llm-wiki.md)
   wird daraus eine eigene Markdown-Seite.

## Vorlage: Lesenotiz-Schema

Kopiere dieses Schema in deinen Prompt ("Fasse das Paper nach folgendem
Schema zusammen"). So sind alle Notizen vergleichbar.

```markdown
# {Kurztitel}

- **Quelle:** [{Autor et al., Jahr}]({URL/DOI})
- **Fragestellung:** {1 Satz}
- **Methode & Daten:** {Stichpunkte}
- **Kernbefunde:** {2-4 Stichpunkte}
- **Limitationen:** {Stichpunkte}
- **Relevanz fuer mich:** {1-2 Saetze, eigener Bezug}
- **Anschlussfragen / verwandte Arbeiten:** {Stichpunkte}
- **Schlagworte:** {tag1, tag2, ...}
```

!!! tip "Konsistenz zahlt sich aus"
    Ein einmal festgelegtes Schema ist Gold wert: Du kannst spaeter ueber
    viele Notizen hinweg vergleichen, filtern und synthetisieren — von Hand
    oder wieder mit einem LLM.

!!! note "Noch zu ergaenzen"
    Dein eigenes Notiz-Schema und ein reales Beispiel aus deiner Ablage.
