# Vom Thema zur Literaturuebersicht

Ein durchgaengiges Beispiel, das mehrere Werkzeuge verkettet — die
Blaupause fuer eigene Workflows.

!!! abstract "Das Rezept in einem Bild"
    ```
    Semantic Scholar  ->  Custom GPT (verarbeitet nach Template)  ->  Ablage
       (Recherche)         ScholarAI-Action                          Zotero / Notion / Markdown
    ```

## Ziel

Aus einem Stichwort eine belegte Literaturuebersicht erzeugen und die Funde
sofort ablagefertig im gewuenschten Format erhalten.

## Beteiligte Werkzeuge

- [ScholarAI Custom GPT](../werkzeuge/dialog/scholarai.md) als Steuerzentrale
- [Semantic Scholar](../werkzeuge/finden/semantic-scholar.md) als Datenquelle
- [Zotero](../werkzeuge/sammeln/zotero.md) und/oder
  [Notion](../werkzeuge/sammeln/notion.md) als Ablage
- optional ein [LLM-Wiki](../werkzeuge/sammeln/llm-wiki.md) als Markdown-Ziel

## Schritte

1. **Recherche anstossen.** Im Custom GPT den Baustein
   *Gezielte Literatursuche* nutzen. Der GPT sucht ueber die angebundene
   Datenbasis und liefert verlinkte Treffer.
2. **Verdichten nach Template.** Der GPT formatiert jeden Treffer nach einem
   hinterlegten Template (als RAG im GPT abgelegt) — z.B. als Markdown-Block
   fuers Wiki oder als Struktur, die direkt nach Notion/Zotero passt.
3. **Ablegen.** Ueber die angebundenen Actions schreibt der GPT die Eintraege
   nach Zotero (als Referenzen) und/oder Notion (als Notizen), bzw. gibt
   Markdown fuer das Wiki aus.
4. **Pruefen.** Stichprobe: Stimmen Zitate und Links? Keine erfundenen Quellen?

!!! tip "Warum das Template der Trick ist"
    Indem das Ausgabeformat vorgegeben ist, sind die Funde ohne Nacharbeit
    ablagefertig. Genau das macht aus Einzeltools eine durchgaengige Kette.

## Vorlagen: Ausgabe-Templates

Lege diese Vorlagen im GPT ab (in der Instruktion oder als hochgeladenes
Wissensdokument) und lass den GPT je nach Ablageziel das passende Format
waehlen. Passe sie an dein eigenes Schema an.

!!! warning "Eine Regel fuer alle Templates"
    Keine erfundenen Angaben. Felder, die die Quelle nicht hergibt, bleiben
    leer — lieber eine Luecke als ein falscher Wert.

### Router (steuert die Formatwahl)

```text
Wenn ich ein Ablageziel nenne, formatiere die Ausgabe nach dem passenden
Template:
- "fuers Wiki"  -> Template Wiki (Markdown mit Frontmatter und [[Links]])
- "nach Notion" -> Template Notion (Properties exakt nach meinem DB-Schema)
- "nach Zotero" -> Template Zotero (Referenz + kompakte Notiz)
Ohne Angabe: Template Wiki.
```

### Template Wiki (Markdown, Obsidian/Karpathy-Stil)

```markdown
---
title: "{Kurztitel}"
authors: "{Autor et al.}"
year: {Jahr}
source: "{DOI oder URL}"
tags: [{tag1}, {tag2}]
added: {JJJJ-MM-TT}
---

# {Kurztitel}

**Fragestellung:** {1 Satz}

**Kernbefunde:**
- {Stichpunkt}
- {Stichpunkt}

**Methode & Daten:** {Stichpunkte}

**Limitationen:** {Stichpunkte}

**Bezug zu meinem Projekt:** {1-2 Saetze}

**Verwandt:** [[{andere Wiki-Seite}]], [[{...}]]
```

Das Frontmatter (YAML oben) macht die Seite fuer Obsidian-Dataview
auswertbar; die `[[Links]]` erzeugen die Querverweise im Wiki.

### Template Notion (Datenbankeintrag)

Der GPT befuellt die Properties deiner Notion-Datenbank. Die Property-Namen
muessen **exakt** denen in deiner Datenbank entsprechen:

```text
Properties:
- Titel        (title)        : {Kurztitel}
- Autor:innen  (text)         : {Autor et al.}
- Jahr         (number)       : {Jahr}
- Quelle       (url)          : {DOI oder URL}
- Status       (select)       : ungelesen | gelesen | zitiert
- Tags         (multi-select) : {tag1, tag2}

Seiteninhalt (Body):
- Fragestellung, Kernbefunde, Methode & Daten, Limitationen,
  Bezug zu meinem Projekt  (gleiche Gliederung wie Template Wiki)
```

### Template Zotero (Referenz + Notiz)

Zuerst die Referenz ueber DOI/Metadaten anlegen, dann eine kompakte
Kindnotiz anhaengen:

```text
Zusammenfassung: {2-3 Saetze}
Kernbefunde: {Stichpunkte}
Limitationen: {Stichpunkte}
Eigener Bezug: {1-2 Saetze}
```

Schlagworte zusaetzlich als echte Zotero-Tags setzen (nicht nur im Notiztext),
damit sie filterbar sind.

!!! note "Vor dem Produktiveinsatz pruefen"
    Die Property-Namen (Notion) und Feldzuordnungen (Zotero) gegen deine
    aktuelle Datenbank bzw. die aktuelle API abgleichen — diese aendern sich
    eher als die Markdown-Vorlage.

## Variante

Statt direkt abzulegen, die Treffer zuerst in
[Connected Papers](../werkzeuge/finden/connected-papers.md) visuell pruefen
und erst die relevanten Arbeiten uebernehmen.
