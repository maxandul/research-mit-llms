---
type: Konzeptnotiz
title: "Modell und Einsatzart bestimmen das Ergebnis"
description: >-
  Aussagen darueber, was LLMs koennen, sind ohne Angabe von Modell, Version, Konfiguration und Einsatzart kaum belastbar.
tags: [llms-verstehen, reporting, reasoning]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-07 }
---

# Modell und Einsatzart bestimmen das Ergebnis

**Konzeptnotiz** · Stand: Juli 2026

Aussagen über das, was "LLMs" in der Forschung können, sind ohne Angabe
von **Modell, Version, Konfiguration und Einsatzart** fast wertlos. Die
Evidenz dafür ist über alle Quellen des Codier-Sprints konsistent:
GPT-4 verdoppelte gegenüber GPT-3.5 die Übereinstimmung mit menschlichen
Codierern (mittleres κ 0,68 vs. 0,34); ein aktiviertes Reasoning
entscheidet bei identischer Architektur darüber, ob ein Modell als
zuverlässig oder unzuverlässig einzustufen ist (10 bis 15
Prozentpunkte); Prompt-Design (Begründung verlangen, ein Code pro
Durchgang) verschiebt Ergebnisse in ähnlicher Grössenordnung; und
nominell "gleiche" Modelle sind es nicht (gpt-4o-mini scheiterte an
Aufgaben, die GPT-4o löste). Dazu kommt das Tempo der Entwicklung:
Studien mit Modellen von 2023/2024 beschreiben bei Erscheinen oft schon
überholte Fähigkeiten, ihre *unteren* Schranken bleiben aber informativ.

Daraus folgen zwei Regeln. **Für das Lesen von Studien:** zuerst in den
Methodenteil schauen (welches Modell, welche Version, wie eingesetzt,
wann durchgeführt?) und Schlussfolgerungen entsprechend datieren;
negative Befunde mit schwachen oder falsch konfigurierten Modellen
widerlegen nicht die Machbarkeit, positive Befunde garantieren nichts
für andere Aufgaben. **Für eigene Arbeit:** Modellversion, Parameter und
Prompts dokumentieren (Vorschlag COREQ + LLM) und jeden Modell- oder
Versionswechsel neu validieren, statt Gültigkeit anzunehmen. Genau diese
Angaben fehlen bisher in der Mehrheit der Studien (75 Prozent ohne
jegliche Parameter), was Vergleichbarkeit und Reproduzierbarkeit
untergräbt.

## Belege

- [Kempny et al. (2026)](../quellen/kempny-2026-llm-qualitativ-scoping-review.md) — Peer-reviewed (Reporting-Lücken, COREQ + LLM, Spannbreite der Ergebnisse)
- [Dunivin (2025)](../quellen/dunivin-2025-scaling-hermeneutics.md) — Peer-reviewed (GPT-4 vs. GPT-3.5, CoT, Per Code, Versions-Warnung)
- [Marston et al. (2026)](../quellen/marston-2026-humanitaere-daten-benchmark.md) — Preprint (Reasoning-Modi als Kippschalter, 46 Modelle im Vergleich)
- [Misra et al. (2026)](../quellen/misra-2026-open-source-llms-codieren.md) — Peer-reviewed (schwache Konfiguration erklärt schwache Ergebnisse)

## Verwandte Konzepte

- [LLM als zweiter Codierer](llm-als-zweiter-codierer.md) — Anwendungsfall, an dem der Effekt sichtbar wird
- [LLM-Output prüfen](llm-output-pruefen.md) — Validierung als Konsequenz
- [Lokale Modelle für sensible Daten](lokale-modelle-sensible-daten.md) — Abwägung, bei der die Modellwahl zentral ist

## Fliesst ein in

- Alle Synthesen (Lese- und Einordnungsgrundsatz, verankert im Schema/CLAUDE.md)
- [Synthese: Qualitative Daten codieren](../synthese/qualitativ-codieren.md)
- [Website: Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md) (Dokumentations-Empfehlung)
