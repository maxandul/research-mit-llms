---
type: Quellnotiz
title: "Kempny et al. (2026): Scoping Review LLMs in qualitativer Forschung"
description: >-
  75 Studien nach PRISMA-ScR: Uebereinstimmung LLM/Mensch streut von 36 bis
  99 Prozent, das technische Reporting ist massiv lueckenhaft.
resource: https://doi.org/10.1186/s12874-026-02913-1
tags: [qualitativ-codieren, review, intercoder-reliabilitaet, reporting]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-07 }
verified:
  - { by: "human:andreas", at: 2026-07-07, umfang: Volltext }
stale_after: 2028-07-07

evidenzstufe: Peer-reviewed
pruefnotiz: >-
  Volltext gelesen (Open-Access-PDF, aus `rohdaten/`), DOI im Original
  enthalten.
studie:
  modelle: "diverse; 45 Prozent der eingeschlossenen Studien nennen nicht einmal die Einsatzform"
  einsatzart: >-
    Scoping Review ueber 75 Studien aus fuenf Datenbanken, Suchzeitraum
    Januar 2020 bis Mai 2025.
  durchgefuehrt: "2020-01 bis 2025-05"
---

# Kempny et al. (2026): Scoping Review zu LLMs in qualitativer Forschung

> Kempny, C., Frings, J., Rust, P., Meister, S. & Fehring, L. (2026): *The
> use and methodological reporting of large language models in qualitative
> research: a scoping review.* BMC Medical Research Methodology, 26:137.
> <https://doi.org/10.1186/s12874-026-02913-1>

## Kernaussagen

- Scoping Review nach PRISMA-ScR über fünf Datenbanken (PubMed, CINAHL,
  PsycINFO, Business Source Premier, Scopus), Suchzeitraum Januar 2020 bis
  Mai 2025, 75 eingeschlossene Studien. LLMs werden über den ganzen
  qualitativen Forschungsprozess eingesetzt, am häufigsten für
  Codier-Unterstützung (n=43) und Themenidentifikation (n=41), meist im
  Rahmen von Themenanalyse (n=38).
- **Übereinstimmung LLM/Mensch streut extrem: 36% bis 99%**, abhängig von
  Aufgabenkomplexität, Prompt-Qualität und Validierungsstrenge. Die meisten
  Anwendungen bleiben auf der Ebene deskriptiven oder deduktiven Codierens
  mit vordefiniertem Codebuch; für interpretative Tiefenanalyse ist die
  Evidenz dünn.
- **Technisches Reporting ist massiv lückenhaft:** Nur 13 von 75 Studien
  berichten die Temperature, 12 die Kontextlänge, 4 top_p; 75% nennen gar
  keine Parameter, 45% nicht einmal die Einsatzform (API, Web-Oberfläche
  oder lokal). Ohne diese Angaben sind Ergebnisse weder reproduzierbar noch
  vergleichbar.
- OpenAI-GPT-Modelle dominieren mit 93% der Studien; Vergleiche mit
  Open-Source-Modellen fehlen weitgehend, ebenso Evidenz für
  nicht-englische Kontexte.
- 97% der Studien liessen KI-Output durch Menschen verifizieren; LLMs
  werden fast durchgehend als assistive Werkzeuge positioniert, nicht als
  autonome Analysten.
- Die Autoren leiten daraus die Reporting-Erweiterung **COREQ + LLM** ab:
  Modellversion und Anbieter, Parameter, vollständige Prompts,
  Validierungsverfahren und reflexive Dokumentation der Integration.

## Einordnung

Scoping Review, daher bewusst ohne Qualitätsbewertung der Einzelstudien
und ohne Wirksamkeitsurteil: Die 36-99% sind berichtete Spannen, kein
Meta-Ergebnis. Suchzeitraum endet Mai 2025; die untersuchten Studien
arbeiten also überwiegend mit Modellen der GPT-3.5/GPT-4-Ära. Die Autoren
benennen selbst, dass Befunde zu konkreten Modellen schnell veralten.
Nur englischsprachige, begutachtete Journalartikel (keine Preprints,
Konferenzen, graue Literatur).

## Relevanz für die Website

Der Anker-Text für [Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md):
zeigt, dass der dort beschriebene Einsatz (deduktives Codieren mit
Codebuch, Mensch prüft) dem in den 75 eingeschlossenen Studien mit Abstand
häufigsten Muster entspricht. Zugleich Grundlage für eine schärfere Dokumentationsempfehlung
auf der Website: Modellversion, Parameter und Prompts gehören in den
Methodenteil (COREQ + LLM). Stützt ausserdem den Schema-Grundsatz, bei
jeder Studie zuerst auf Modell, Version und Einsatzart zu schauen.

## Querverweise

- [Dunivin (2025)](dunivin-2025-scaling-hermeneutics.md) — Fallstudie, die genau die geforderte technische Transparenz vorlebt
- [Marston et al. (2026)](marston-2026-humanitaere-daten-benchmark.md) — zeigt die Modell- und Konfigurationsabhängigkeit im Benchmark
- [Misra et al. (2026)](misra-2026-open-source-llms-codieren.md) — adressiert die Open-Source-Lücke
- Konzepte: [LLM als zweiter Codierer](../konzepte/llm-als-zweiter-codierer.md),
  [Modell und Einsatzart bestimmen das Ergebnis](../konzepte/modell-und-einsatzart.md),
  [Grenzen interpretativer Tiefe](../konzepte/grenzen-interpretativer-tiefe.md)
