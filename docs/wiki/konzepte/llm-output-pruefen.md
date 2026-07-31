---
type: Konzeptnotiz
title: "LLM-Output pruefen"
description: >-
  LLM-Output muss inhaltlich geprueft werden, und dieser Pruefaufwand wird systematisch unterschaetzt.
tags: [llms-verstehen, halluzination, verantwortung]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-07 }
---

# LLM-Output prüfen

**Konzeptnotiz** · Stand: Juli 2026

LLM-Output muss vor Verwendung inhaltlich geprüft werden, und dieser
Prüfaufwand wird systematisch unterschätzt. Die Evidenz dazu ist
konsistent: In einem Experiment mit ChatGPT-generierten Forschungsanträgen
hatten 38% der Referenzen falsche DOIs und 16% waren komplett erfunden; in
publizierter Literatur führte eine einzige stehengebliebene Chatbot-Phrase
zur Entdeckung von 18 nicht existierenden Referenzen; und in einem
Schreibexperiment reichten 68% der Teilnehmenden LLM-Output unbearbeitet
ein. Bender et al. weisen zudem darauf hin, dass es kaum Studien dazu
gibt, wie viel Zeit sorgfältiges Prüfen tatsächlich kostet und wie
zuverlässig Menschen es unter Druck leisten; Marelli et al. empfehlen,
Prüf- und Qualitätskriterien **vor** dem LLM-Einsatz festzulegen und den
Effizienzgewinn ehrlich gegen den Prüfaufwand zu rechnen.

Wichtige Grenze: Prüfen heilt die verräterischen Oberflächenfehler, aber
nicht automatisch tieferliegende Probleme (verzerrte Auswahl, plausible
Fehlinterpretationen). Leicht redigierter LLM-Text ist von aussen nicht
mehr erkennbar; die Prüfpflicht bleibt deshalb eine Frage der
Selbstverpflichtung, nicht der Detektierbarkeit
([Risiken der Nichtdeklaration](risiken-der-nichtdeklaration.md)).

## Belege

- [Mabirizi et al. (2025)](../quellen/mabirizi-2025-genai-postgrad-review.md) — Peer-reviewed (Review; Referenzfehler-Quoten, unbearbeiteter Output)
- [Binz et al. (2025)](../quellen/binz-2025-llms-praxis-wissenschaft.md) — Peer-reviewed (unterschätzter Prüfaufwand, Prüfkriterien vorab)
- [Glynn (2024/2025): Academ-AI](../quellen/glynn-2024-academ-ai.md) — Preprint (konfabulierte Referenzen in publizierter Literatur)

## Verwandte Konzepte

- [Verantwortung bleibt beim Menschen](verantwortung-bleibt-beim-menschen.md) — Prüfen als operative Verantwortung
- [Risiken der Nichtdeklaration](risiken-der-nichtdeklaration.md) — ungeprüfter Output ist der häufigste Entdeckungsgrund
- [Prävalenz der LLM-Nutzung](praevalenz-llm-nutzung.md) — Ausmass, in dem geprüft werden müsste

## Fliesst ein in

- [Website: KI-Nutzung deklarieren](../../haltung/ki-deklarieren.md) (Abschnitt "Was die Deklaration nicht ersetzt")
- [Synthese: LLMs verstehen](../synthese/llms-verstehen.md)
- [Website: LLMs verstehen](../../grundlagen/llms-verstehen.md) (Kernregel "alles Belegrelevante selbst prüfen")
