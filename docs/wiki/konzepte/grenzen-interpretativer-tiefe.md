---
type: Konzeptnotiz
title: "Grenzen interpretativer Tiefe"
description: >-
  LLMs codierten in bisherigen Tests zuverlaessig, was explizit im Text steht, und schwaecher, wo Bedeutung erschlossen werden muss.
tags: [qualitativ-codieren, methodenkritik, intercoder-reliabilitaet]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-07 }
---

# Grenzen interpretativer Tiefe

**Konzeptnotiz** · Stand: Juli 2026

In bisherigen Tests codieren LLMs am zuverlässigsten, was explizit im
Text steht und sich einem klaren Codebuch zuordnen lässt. Systematisch
schwächer waren sie dort, wo Bedeutung erschlossen werden muss: bei
**implizit Geäussertem, Randfällen und mehrdeutigen Passagen**. Der 46-Modelle-Benchmark findet
diese Schwäche über alle Modelle hinweg ausgerechnet bei den
folgenreichsten Kategorien (physische Sicherheit, Diskriminierung);
GPT-4 scheiterte in der Du-Bois-Fallstudie genau an den Codes, die
implizites Kontextwissen verlangen (Stimmen-Zuordnung); und kleine
Modelle produzierten zur Hälfte kontextarme oder duplizierte Codes. Auch
das Scoping Review verortet die belastbare Evidenz beim deskriptiven und
deduktiven Codieren, nicht bei interpretativer Tiefenanalyse oder
Themensynthese.

Praktisch heisst das: Aggregierte Übereinstimmungswerte genügen nicht
als Freigabe. Die Kontrolle gehört dorthin, wo Fehlcodierung am meisten
kostet: **abgestufte menschliche Prüfung pro Kategorie**, gezielt bei
heiklen, impliziten und seltenen Codes, statt gleichverteilter
Stichproben. Interpretation, Ironie, Kontextabhängiges und die Synthese
der Befunde bleiben menschliche Aufgaben.

Stand Juli 2026. Ob kommende Modellgenerationen diese Schwächen beheben,
ist offen; das Konzept ist bei jedem Sprint gegen neue Evidenz zu prüfen.

## Belege

- [Marston et al. (2026)](../quellen/marston-2026-humanitaere-daten-benchmark.md) — Preprint (systematische Schwäche bei Schutzthemen trotz α > 0,85)
- [Dunivin (2025)](../quellen/dunivin-2025-scaling-hermeneutics.md) — Peer-reviewed (Randfälle mit implizitem Wissen als konsistente Fehlerquelle)
- [Kempny et al. (2026)](../quellen/kempny-2026-llm-qualitativ-scoping-review.md) — Peer-reviewed (Evidenz konzentriert sich auf deskriptiv/deduktiv)
- [Misra et al. (2026)](../quellen/misra-2026-open-source-llms-codieren.md) — Peer-reviewed (kontextarme und duplizierte Codes)

## Verwandte Konzepte

- [LLM als zweiter Codierer](llm-als-zweiter-codierer.md) — die Stärkenseite desselben Bildes
- [Methodologische Kritik am LLM-Einsatz](methodologische-kritik-qualitativ.md) — grundsätzlichere Fassung des Einwands
- [Verantwortung bleibt beim Menschen](verantwortung-bleibt-beim-menschen.md) — Interpretation als nicht delegierbarer Kern

## Fliesst ein in

- [Synthese: Qualitative Daten codieren](../synthese/qualitativ-codieren.md)
- [Website: Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md) (Abschnitt "Grenzen")
