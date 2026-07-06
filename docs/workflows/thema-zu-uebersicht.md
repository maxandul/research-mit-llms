# Vom Thema zur Literaturübersicht

Ein durchgängiges Beispiel, das mehrere Werkzeuge verkettet: die
Blaupause für eigene Workflows.

!!! abstract "Das Rezept in einem Bild"
    ```
    Semantic Scholar  ->  Custom GPT (verarbeitet nach Template)  ->  Ablage
       (Recherche)         ScholarAI-Action                          Zotero / Notion / Markdown
    ```

## Ziel

Aus einem Stichwort eine belegte Literaturübersicht erzeugen und die Funde
sofort ablagefertig im gewünschten Format erhalten.

## Beteiligte Werkzeuge

- [ScholarAI Custom GPT](../werkzeuge/dialog/scholarai.md) als Steuerzentrale
- [Semantic Scholar](../werkzeuge/finden/semantic-scholar.md) als Datenquelle
- [Zotero](../werkzeuge/sammeln/zotero.md) und/oder
  [Notion](../werkzeuge/sammeln/notion.md) als Ablage
- optional ein [LLM-Wiki](../werkzeuge/sammeln/llm-wiki.md) als Markdown-Ziel

## Schritte

1. **Recherche anstossen.** Im Custom GPT den Baustein
   *Gezielte Literatursuche* nutzen. Der GPT sucht über die angebundene
   Datenbasis und liefert verlinkte Treffer.
2. **Verdichten nach Template.** Der GPT formatiert jeden Treffer nach einem
   hinterlegten Template (als RAG im GPT abgelegt), z.B. als Markdown-Block
   fürs Wiki oder als Struktur, die direkt nach Notion/Zotero passt.
3. **Ablegen.** Über die angebundenen Actions schreibt der GPT die Einträge
   nach Zotero (als Referenzen) und/oder Notion (als Notizen), bzw. gibt
   Markdown für das Wiki aus.
4. **Prüfen.** Stichprobe: Stimmen Zitate und Links? Keine erfundenen Quellen?

!!! tip "Warum das Template der Trick ist"
    Indem das Ausgabeformat vorgegeben ist, sind die Funde ohne Nacharbeit
    ablagefertig. Genau das macht aus Einzeltools eine durchgängige Kette.

!!! warning "Was dieser Workflow nicht ersetzt"
    LLM-Werkzeuge durchsuchen nur **öffentlich zugängliche** Korpora
    (Metadaten, Abstracts, Open-Access-Volltexte). Eine systematische
    Recherche in den lizenzierten **Fachdatenbanken** deines Fachs (z.B.
    über die Hochschulbibliothek) ersetzen sie nicht — je nach Disziplin
    fehlt dort Wesentliches. Und: Die Treffer sind Kandidaten, keine
    Belege. Was du zitieren willst, **liest du selbst im Volltext** —
    Abstracts genügen nicht.

## Vorlagen: Ausgabe-Templates

Lege diese Vorlagen im GPT ab (in der Instruktion oder als hochgeladenes
Wissensdokument) und lass den GPT je nach Ablageziel das passende Format
wählen. Passe sie an dein eigenes Schema an.

!!! warning "Eine Regel für alle Templates"
    Keine erfundenen Angaben. Felder, die die Quelle nicht hergibt, bleiben
    leer. Lieber eine Lücke als ein falscher Wert.

### Router (steuert die Formatwahl)

```text
Wenn ich ein Ablageziel nenne, formatiere die Ausgabe nach dem passenden
Template:
- "fürs Wiki"  -> Template Wiki (Markdown mit Frontmatter und [[Links]])
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

**Bezug zu meinem Projekt:** {1-2 Sätze}

**Verwandt:** [[{andere Wiki-Seite}]], [[{...}]]
```

Das Frontmatter (YAML oben) macht die Seite für Obsidian-Dataview
auswertbar; die `[[Links]]` erzeugen die Querverweise im Wiki.

### Template Notion (Datenbankeintrag)

Der GPT befüllt die Properties deiner Notion-Datenbank. Die Property-Namen
müssen **exakt** denen in deiner Datenbank entsprechen:

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

Zuerst die Referenz über DOI/Metadaten anlegen, dann eine kompakte
Kindnotiz anhängen:

```text
Zusammenfassung: {2-3 Sätze}
Kernbefunde: {Stichpunkte}
Limitationen: {Stichpunkte}
Eigener Bezug: {1-2 Sätze}
```

Schlagworte zusätzlich als echte Zotero-Tags setzen (nicht nur im Notiztext),
damit sie filterbar sind.

!!! note "Vor dem Produktiveinsatz prüfen"
    Die Property-Namen (Notion) und Feldzuordnungen (Zotero) gegen deine
    aktuelle Datenbank bzw. die aktuelle API abgleichen; diese ändern sich
    eher als die Markdown-Vorlage.

## Variante: Connected Papers zwischenschalten

Statt direkt abzulegen, die Treffer zuerst in
[Connected Papers](../werkzeuge/finden/connected-papers.md) visuell prüfen
und erst die relevanten Arbeiten übernehmen.

## Variante: Claude Cowork als Steuerzentrale

Dasselbe Rezept funktioniert mit einem agentischen Desktop-Werkzeug wie
[Claude Cowork](../werkzeuge/sammeln/llm-wiki.md) statt eines Custom GPT —
mit zwei praktischen Vorteilen:

- **Direkter Dateizugriff:** Der Agent fragt die
  [Semantic-Scholar-API](../werkzeuge/finden/semantic-scholar.md) direkt ab
  (geht ohne API-Key), wendet deine Templates aus einer lokalen Datei an
  und schreibt die Ergebnisse als Markdown-Dateien direkt in deinen
  Wiki-Ordner — ohne Kopieren aus dem Chat.
- **Volltext-tauglich:** Legst du Paper-PDFs in einen lokalen Ordner, kann
  der Agent sie vollständig lesen. Wichtig, denn Abstracts allein reichen
  für belastbare Notizen nicht — erst sichten, dann den Volltext besorgen
  und auf dieser Basis exzerpieren.

Statt der GPT-Instruktion übernimmt eine Schema-Datei im Arbeitsordner die
Steuerung (siehe [Wiki-Vorlagen](../ressourcen/wiki-vorlagen.md)). OpenAI
geht mit seiner Desktop-App einen ähnlichen Weg; massgeblich ist die
jeweilige Original-Doku.
