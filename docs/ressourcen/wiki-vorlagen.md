# Wiki-Vorlagen

Kopierfertige Vorlagen für ein eigenes Forschungs-Wiki, wie es
[Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md)
beschreibt. Es sind dieselben Vorlagen, mit denen der
[Forschungsstand dieser Website](../wiki/index.md) gepflegt wird — du
siehst dort also, wie ausgefüllte Exemplare aussehen.

Jede Vorlage beginnt mit einem YAML-Block (Frontmatter) nach dem
[Open Knowledge Format](../werkzeuge/sammeln/llm-wiki.md#ein-standard-zeichnet-sich-ab-das-open-knowledge-format).
Er ist optional: Ohne ihn funktionieren die Vorlagen genauso. Mit ihm wird
maschinell prüfbar, was sonst nur im Text steht, und Werkzeuge wie
Obsidian oder MkDocs können danach filtern. Pflicht ist im Format allein
das Feld `type`; ergänze also ruhig nur so viel, wie du auch pflegen magst.

!!! randnotiz "Warum im Frontmatter und nicht im Text?"
    Evidenzstufe und Prüfvermerk standen auf dieser Website früher zusätzlich
    als Fliesstext im Kopf jeder Notiz. Das musste doppelt gepflegt werden und
    lief mit der Zeit auseinander. Seit Juli 2026 stehen sie nur noch im
    Frontmatter; den sichtbaren Kopf einer Notiz erzeugt die Website daraus
    automatisch. Wer die Vorlagen ohne solche Automatik nutzt, schreibt die
    Angaben natürlich weiterhin in den Text.

## Quellnotiz

Eine Notiz pro Quelle. Sie trägt die Provenienz: wer sagt was, wie wurde
es geprüft, wie belastbar ist es.

```markdown
---
type: Quellnotiz
title: "Kurztitel"
description: >-
  Ein Satz, was die Quelle zeigt.
resource: https://doi.org/…
tags: [thema, art]

generated: { by: "llm-assistiert, redigiert von human:name", at: JJJJ-MM-TT }
verified:
  - { by: "human:name", at: JJJJ-MM-TT, umfang: Volltext }
stale_after: JJJJ-MM-TT
# status: draft        nur bei vorläufigen Notizen (nur Abstract geprüft)

evidenzstufe: Peer-reviewed        # Peer-reviewed | Preprint | Policy | Doku | Praxis
evidenzstufe_zusatz: "Doku eines Verlags"   # optional, präzisiert die Stufe
pruefnotiz: >-
  Was genau geprüft wurde: Original gelesen? DOI aufgelöst? Besonderheiten?
---

# Kurztitel der Quelle

> Vollständige bibliografische Angabe mit Link/DOI.

## Kernaussagen

- Die 3-6 wichtigsten Aussagen der Quelle, in eigenen Worten.

## Einordnung

Methodik, Grenzen, mögliche Verzerrungen. Weglassen, wenn trivial.

## Relevanz für das eigene Projekt

Wofür brauchst du diese Quelle? Welche deiner Aussagen stützt sie?

## Querverweise

- Links auf verwandte Quell- und Konzeptnotizen.
```

## Konzeptnotiz

Ein atomares Thema, quellenübergreifend. Hier entsteht das Netz: Konzepte
verlinken Quellen und einander.

```markdown
---
type: Konzeptnotiz
title: "Name des Konzepts"
description: >-
  Ein Satz, was das Konzept behauptet.
tags: [thema, art]

generated: { by: "llm-assistiert, redigiert von human:name", at: JJJJ-MM-TT }
---

# Name des Konzepts

**Konzeptnotiz** · Stand: Monat JJJJ

Kernaussage in 1-2 Absätzen, quellenübergreifend formuliert. Was weiss
man über diesen einen Sachverhalt, wenn man alle Quellen zusammennimmt?

## Belege

- Links auf Quellnotizen, je mit Evidenzstufe.

## Verwandte Konzepte

- Links, je mit einem Halbsatz zur Beziehung ("die Kehrseite von ...",
  "erklärt möglicherweise ...").

## Fliesst ein in

- Synthese- oder Ergebnisseiten, die dieses Konzept verwenden.
```

## Synthese

Der verdichtete Stand zu einem Thema, zusammengesetzt aus Konzepten.

```markdown
---
type: Synthese
title: "Forschungsstand: Thema"
description: >-
  Ein Satz, was die Synthese zusammenfasst.
tags: [thema]

generated: { by: "llm-assistiert, redigiert von human:name", at: JJJJ-MM-TT }
---

# Forschungsstand: Thema

**Evidenz zuletzt geprüft:** Monat JJJJ

## Worin die Quellen übereinstimmen

Pro Absatz ein Konzept, mit Link. Konsens benennen.

## Was die Evidenz kompliziert macht

Widersprüche, Dilemmata, schwache Übertragbarkeit — nicht glätten.

## Offene Punkte

Wozu fehlt belastbare Forschung? Was veraltet schnell?

## Konsequenzen

Was folgt daraus für dein Projekt / deine Arbeit?
```

## Schema (Spielregeln für den LLM-Agenten)

Die Anleitungsdatei (z.B. `CLAUDE.md`) im Wurzelverzeichnis sagt dem
Agenten, wie das Wiki funktioniert. Gerüst:

```markdown
# Spielregeln für dieses Wiki

## Aufbau
- rohdaten/   Originalquellen — nie verändern, nie veröffentlichen
- quellen/    eine Notiz pro Quelle
- konzepte/   atomare Themen, quellenübergreifend
- synthese/   verdichteter Stand pro Thema

## ingest: neue Quelle einpflegen (zwei Phasen)
Phase 1 — Sichten:
1. Kandidaten suchen, DOI/URL auflösen, Abstracts lesen, priorisieren.
2. Kandidatenliste mit Kurzeinordnung vorlegen.
Phase 2 — Vertiefen (Pflicht vor der Notiz):
3. Volltext beschaffen und in rohdaten/ ablegen; Mensch liest mit
   und/oder gibt dem LLM den Volltext.
4. Quellnotiz erst auf Volltext-Basis anlegen; sonst "nur Abstract"
   vermerken (Notiz gilt dann als vorläufig).
5. Evidenzstufe bestimmen.
6. Konzeptnotizen anlegen oder erweitern; verwandte Konzepte verlinken.
7. Betroffene Synthese aktualisieren.

## lint: regelmässige Prüfung
- Widersprüche markieren, nicht stillschweigend glätten.
- Veraltete Aussagen kennzeichnen, verwaiste Notizen und tote Links melden.
- Was im Frontmatter steht, per Skript prüfen statt von Hand.
```

Das vollständige, produktive Schema dieser Website:
[CLAUDE.md im Repository](https://github.com/maxandul/research-mit-llms/blob/main/CLAUDE.md).

!!! warnung "Verifikation ist der wichtigste Schritt"
    LLMs erfinden Referenzen. Die Regel "verifizieren, bevor irgendetwas
    geschrieben wird" ist der Teil des Schemas, den du am wenigsten
    weglassen solltest — siehe
    [LLMs verstehen](../grundlagen/llms-verstehen.md).
