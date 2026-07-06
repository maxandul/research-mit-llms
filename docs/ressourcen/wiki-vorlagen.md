# Wiki-Vorlagen

Kopierfertige Vorlagen für ein eigenes Forschungs-Wiki, wie es
[Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md)
beschreibt. Es sind dieselben Vorlagen, mit denen der
[Forschungsstand dieser Website](../wiki/index.md) gepflegt wird — du
siehst dort also, wie ausgefüllte Exemplare aussehen.

## Quellnotiz

Eine Notiz pro Quelle. Sie trägt die Provenienz: wer sagt was, wie wurde
es geprüft, wie belastbar ist es.

```markdown
# Kurztitel der Quelle

**Evidenzstufe:** Peer-reviewed | Preprint | Policy | Doku | Praxis ·
**Geprüft:** TT.MM.JJJJ, was genau geprüft wurde (Original gelesen? DOI aufgelöst?)

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
# Forschungsstand: Thema

**Evidenz zuletzt geprüft:** Monat JJJJ

## Was gut belegt ist

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
```

Das vollständige, produktive Schema dieser Website:
[CLAUDE.md im Repository](https://github.com/maxandul/research-mit-llms/blob/main/CLAUDE.md).

!!! tip "Verifikation ist der wichtigste Schritt"
    LLMs erfinden Referenzen. Die Regel "verifizieren, bevor irgendetwas
    geschrieben wird" ist der Teil des Schemas, den du am wenigsten
    weglassen solltest — siehe
    [LLMs verstehen](../grundlagen/llms-verstehen.md).
