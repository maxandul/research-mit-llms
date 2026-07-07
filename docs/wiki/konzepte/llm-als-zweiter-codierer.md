# LLM als zweiter Codierer

**Konzeptnotiz** · Stand: Juli 2026

Beim **deduktiven Codieren mit klarem Codebuch** können aktuelle LLMs die
Zuverlässigkeit erfahrener menschlicher Codierer erreichen: In einem
Benchmark über 46 Modelle (2026, Generation GPT-5.4/Gemini 3.1/Claude 4.6) codieren
32 von 46 Modellen mit Krippendorffs α ≥ 0,80 gegen einen menschlichen
Goldstandard; schon GPT-4 erreichte 2024 bei einzelnen Codes menschliches
Niveau. Die Literatur insgesamt streut aber enorm (Übereinstimmung 36 bis
99 Prozent), und für induktives, interpretatives Arbeiten ist die Evidenz
deutlich schwächer. Das "zweiter Codierer"-Framing trägt also unter
Bedingungen: strukturiertes deduktives Codieren, präzises Codebuch,
Validierung gegen menschliche Codierung pro Code statt pauschal, und
menschlicher Entscheid bei Differenzen. Fast alle publizierten Studien
positionieren das LLM entsprechend als assistives Werkzeug mit
menschlicher Verifikation (97 Prozent), nicht als autonomen Analysten.

Zwei praktische Befunde verfeinern den Workflow: Nach einer **Begründung
pro Codierentscheid** fragen verbessert die Übereinstimmung messbar
(Chain-of-Thought), und ein Code pro Durchgang schlägt das
Gesamt-Codebuch in einem Prompt. Für kleine Interviewstudien kann
Handcodierung dagegen genauso effizient sein wie der Aufbau eines
validierten LLM-Workflows.

## Belege

- [Marston et al. (2026)](../quellen/marston-2026-humanitaere-daten-benchmark.md) — Preprint (46-Modelle-Benchmark, α bis 0,922)
- [Kempny et al. (2026)](../quellen/kempny-2026-llm-qualitativ-scoping-review.md) — Peer-reviewed (Scoping Review: Spannbreite 36-99%, assistive Positionierung)
- [Dunivin (2025)](../quellen/dunivin-2025-scaling-hermeneutics.md) — Peer-reviewed (GPT-4 auf menschlichem Niveau bei einzelnen Codes; CoT, Per-Code-Validierung)
- [Misra et al. (2026)](../quellen/misra-2026-open-source-llms-codieren.md) — Peer-reviewed (Gegenbeispiel: schwache Ergebnisse bei kleinen lokalen Modellen)

## Verwandte Konzepte

- [Modell und Einsatzart bestimmen das Ergebnis](modell-und-einsatzart.md) — warum die Spannbreite so gross ist
- [Grenzen interpretativer Tiefe](grenzen-interpretativer-tiefe.md) — wo das Framing endet
- [LLM-Output prüfen](llm-output-pruefen.md) — die Prüfpflicht gilt auch für Codes
- [Verantwortung bleibt beim Menschen](verantwortung-bleibt-beim-menschen.md) — Entscheid bei Differenzen

## Fliesst ein in

- [Synthese: Qualitative Daten codieren](../synthese/qualitativ-codieren.md)
- [Website: Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md)
