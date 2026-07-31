---
type: Quellnotiz
title: "Kapania et al. (2025): Simulacrum of Stories"
description: >-
  19 erfahrene qualitativ Forschende pruefen LLM-Personas als Ersatz fuer
  Teilnehmende; anfangs plausibel, dann grundsaetzliche Maengel.
resource: https://doi.org/10.1145/3706598.3713220
tags: [qualitativ-codieren, empirie, methodenkritik, synthetische-daten]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-07 }
verified:
  - { by: "human:andreas", at: 2026-07-07, umfang: Volltext }
stale_after: 2028-07-07

evidenzstufe: Peer-reviewed
studie:
  modelle: [GPT-4-turbo]
  einsatzart: >-
    API, Persona per System-Prompt, LLM als simulierte Teilnehmende in
    Hands-on-Interviews mit 19 Forschenden.
  durchgefuehrt: "2024-03 bis 2024-06"
  sprache: Englisch
---

# Kapania et al. (2025): Simulacrum of Stories — LLMs als "Teilnehmende"

**Evidenzstufe:** Peer-reviewed ·
**Geprüft:** 07.07.2026, Volltext gelesen (Open-Access-PDF, aus
`rohdaten/`), DOI im Original enthalten.

> Kapania, S., Agnew, W., Eslami, M., Heidari, H. & Fox, S. E. (2025):
> *Simulacrum of Stories: Examining Large Language Models as Qualitative
> Research Participants.* CHI '25, Yokohama.
> <https://doi.org/10.1145/3706598.3713220>

## Kernaussagen

- Untersucht nicht das Codieren, sondern den radikaleren Vorschlag,
  **menschliche Teilnehmende durch LLM-generierte "synthetische Daten" zu
  ersetzen** (Interviews mit simulierten Personas). 19 erfahrene
  qualitative Forschende führten dazu Hands-on-Interviews mit einem
  LLM-Probanden-Werkzeug (GPT-4-turbo via API, Persona per System-Prompt,
  Erhebung März bis Juni 2024) und verglichen mit eigenen echten
  Transkripten.
- Verlaufsbefund: Anfangs wirkten die LLM-Antworten **überraschend
  plausibel** und ähnelten echten Narrativen; über mehrere Gesprächsrunden
  identifizierten die Forschenden dann grundsätzliche Mängel: fehlende
  Greifbarkeit und Kontexttiefe, keine gelebte Erfahrung, geglättete
  Unterschiede, keine Positionalität.
- Zentrale These ("surrogate effect"): LLMs als Teilnehmer-Ersatz
  unterlaufen **Einwilligung und Handlungsmacht** der Communities, deren
  Daten das Modell verarbeitet hat, und delegitimieren qualitative
  Wissensformen. Bessere Prompts oder Modelle beheben das nicht, weil das
  Problem epistemologisch ist, nicht technisch.
- Selbst die diskutierten "harmloseren" Einsatzzwecke (etwa
  Interview-Training für Studierende) blieben unter den Teilnehmenden
  umstritten: schlechte Interviewgewohnheiten, falsche Erwartungen an
  echte Gespräche.

## Einordnung

Qualitative Interviewstudie mit US-Fokus (16 von 19 aus der Academia),
Stand GPT-4-turbo 2024. Die Pointe ist bewusst modellunabhängig
formuliert: Der Einwand richtet sich gegen die Ersetzungslogik, nicht
gegen eine Modellgeneration. Für die enger gefasste Frage "LLM als
zweiter Codierer bei echten Daten" gilt die Kritik nur abgeschwächt, sie
markiert aber, wo die Grenze verläuft (Daten *erzeugen* vs. Daten
*verarbeiten*).

## Relevanz für die Website

Bisheriger blinder Fleck: Die Website behandelt LLMs als Werkzeug zur
Verarbeitung selbst erhobener Daten und erwähnt die Debatte um
synthetische Daten und die epistemologische Kritik nicht. Für
[Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md)
liefert die Studie die Begründung, warum die Interpretation beim Menschen
bleibt, und eine klare rote Linie: LLMs simulieren keine Teilnehmenden.

## Querverweise

- [Kempny et al. (2026)](kempny-2026-llm-qualitativ-scoping-review.md) — verortet die Skepsis-Spannbreite in der Community
- [Dunivin (2025)](dunivin-2025-scaling-hermeneutics.md) — Gegenentwurf: Automatisierung unter Erhalt der Hermeneutik
- Konzepte: [Methodologische Kritik am LLM-Einsatz](../konzepte/methodologische-kritik-qualitativ.md),
  [Verantwortung bleibt beim Menschen](../konzepte/verantwortung-bleibt-beim-menschen.md)
