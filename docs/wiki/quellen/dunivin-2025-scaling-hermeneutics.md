---
type: Quellnotiz
title: "Dunivin (2025): Scaling hermeneutics"
description: >-
  Praxisleitfaden und Fallstudie zum LLM-Codieren als reflexive Praxis, mit
  vorbildlich dokumentierter Methodik und klaren Befunden zur Einsatzart.
resource: https://doi.org/10.1140/epjds/s13688-025-00548-8
tags: [qualitativ-codieren, empirie, intercoder-reliabilitaet, prompting]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-07 }
verified:
  - { by: "human:andreas", at: 2026-07-07, umfang: Volltext }
stale_after: 2028-07-07

evidenzstufe: Peer-reviewed
studie:
  modelle: [gpt-4-1106-preview, GPT-3.5]
  einsatzart: >-
    API, Temperature 0, top_p 1, Zero-Shot, Codebuch-Definition als
    System-Prompt; verglichen wurden ein Code pro Prompt gegen das gesamte
    Codebuch sowie mit und ohne Begruendungsschritt.
  durchgefuehrt: 2024-01
  sprache: Englisch
---

# Dunivin (2025): Scaling hermeneutics — LLM-Codieren als reflexive Praxis

**Evidenzstufe:** Peer-reviewed ·
**Geprüft:** 07.07.2026, Volltext gelesen (Open-Access-PDF, aus
`rohdaten/`), DOI im Original enthalten.

> Dunivin, Z. O. (2025): *Scaling hermeneutics: a guide to qualitative
> coding with LLMs for reflexive content analysis.* EPJ Data Science, 14:28.
> <https://doi.org/10.1140/epjds/s13688-025-00548-8>

## Kernaussagen

- Praxisleitfaden plus Fallstudie: Ein human entwickeltes Codebuch (9 Codes
  zur Charakterisierung von W.E.B. Du Bois in Zeitungstexten) wird iterativ
  für Maschinenverständlichkeit umgeschrieben, dann codiert das LLM;
  Vergleich gegen einen menschlichen Goldstandard (111 Passagen, mittlere
  Human-Übereinstimmung κ = 0,78).
- **Methodik (vorbildlich dokumentiert):** gpt-4-1106-preview via API,
  Januar 2024, Temperature 0, top_p 1, Zero-Shot, Codebuch-Definition als
  System-Prompt. Vergleichsbedingungen: GPT-3.5, mit/ohne
  Begründungsschritt (Chain-of-Thought), ein Code pro Prompt ("Per Code")
  vs. ganzes Codebuch auf einmal.
- Drei robuste Befunde zur Einsatzart: **GPT-4 weit vor GPT-3.5**
  (mittleres κ 0,68 vs. 0,34; drei Codes erreichen menschliches Niveau,
  κ 0,79 bis 1,00). **Ein Code pro Prompt schlägt das Gesamt-Codebuch**
  (0,68 vs. 0,60). **Nach Begründung fragen verbessert die Codierung**
  durchgehend (Per Code: 0,59 → 0,68).
- Modellversion ist nicht egal: In Folgearbeiten scheiterte gpt-4o-mini an
  Aufgaben, die GPT-4o zuverlässig löste (inkl. Missachtung expliziter
  Formatanweisungen). Modellnamen bezeichnen Familien, nicht feste
  Artefakte; jede neue Aufgabe und jede neue Version braucht erneute
  Validierung.
- Einordnung ins Qualitative: Automatisierung lohnt sich für grosse
  Korpora; **für kleine Datensätze wie Interviewstudien rät der Autor
  explizit ab**, da Handcodierung dort ähnlich effizient ist und
  Datennähe stiftet. Die Adaption des Codebuchs für das LLM sei selbst
  hermeneutische Arbeit; Codes mit schwacher Übereinstimmung werden
  ausgeschlossen oder manuell codiert.

## Einordnung

Einzelfallstudie mit einem historisch-literarischen Korpus und einem
einzigen Modellanbieter; die konkreten κ-Werte sind nicht auf andere
Domänen übertragbar (der Autor betont das selbst). Der Wert liegt in den
replizierbaren Design-Prinzipien (CoT, Per Code, Validieren pro Code) und
in der offen dokumentierten Konfiguration. Stand Januar 2024, also
GPT-4-Ära: absolute Leistungswerte sind als untere Schranke heutiger
Modelle zu lesen.

## Relevanz für die Website

Stützt gleich mehrere Empfehlungen von
[Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md):
pro Zeile Begründung verlangen (CoT), Codebuch iterativ nachschärfen,
Stichproben-Vergleich mit menschlicher Codierung. Ergänzt sie um zwei
Punkte: kleine Häppchen auch auf Code-Ebene denken (ein Code pro
Durchgang) und die Warnung, dass sich Automatisierung bei kleinen
Interviewstudien kaum lohnt. Die Versions-Erfahrung (4o-mini vs. 4o) ist
ein Kernbeleg für [Modell und Einsatzart bestimmen das Ergebnis](../konzepte/modell-und-einsatzart.md).

## Querverweise

- [Kempny et al. (2026)](kempny-2026-llm-qualitativ-scoping-review.md) — fordert genau diese Reporting-Tiefe als Standard ein
- [Marston et al. (2026)](marston-2026-humanitaere-daten-benchmark.md) — bestätigt Konfigurationsabhängigkeit (Reasoning-Modi) im grossen Massstab
- Konzepte: [LLM als zweiter Codierer](../konzepte/llm-als-zweiter-codierer.md),
  [Modell und Einsatzart bestimmen das Ergebnis](../konzepte/modell-und-einsatzart.md),
  [Methodologische Kritik am LLM-Einsatz](../konzepte/methodologische-kritik-qualitativ.md)
