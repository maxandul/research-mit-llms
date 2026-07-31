---
type: Quellnotiz
title: "Liang et al. (2025): Quantifying LLM usage in scientific papers"
description: >-
  Populationsbasierte Schaetzung ueber 1,1 Millionen Papers: LLM-modifizierte
  Texte in der Informatik bis gegen 22 Prozent.
resource: https://www.nature.com/articles/s41562-025-02273-8
tags: [ki-deklarieren, empirie, praevalenz, transparenz]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-06 }
verified:
  - { by: "human:andreas", at: 2026-07-06, umfang: "Volltext des Preprints; publizierte Fassung nur Abstract" }
stale_after: 2028-07-06

sources:
  - id: preprint
    resource: https://arxiv.org/abs/2404.01268
    title: "Quantifying Large Language Model Usage in Scientific Papers (arXiv v1)"
    last_modified: 2024-04-01
  - id: publiziert
    resource: https://www.nature.com/articles/s41562-025-02273-8
    title: "Nature Human Behaviour, publizierte Fassung (hinter Paywall)"

evidenzstufe: Peer-reviewed
pruefnotiz: >-
  Volltext des Preprints gelesen (arXiv v1 vom 01.04.2024, aus
  `rohdaten/`). Achtung: Die publizierte NHB-Fassung erweitert die
  Analyse (1,1 Mio. Papers bis Sep 2024, höhere Endwerte) und liegt
  hinter der Paywall; ihre Zahlen sind nur über Abstract und
  Artikelseite gegengelesen. Auf arXiv existiert keine aktualisierte
  Version.
studie:
  modelle: [GPT-3.5]
  einsatzart: >-
    Keine Faehigkeitsmessung: GPT-3.5 erzeugte das Trainingskorpus fuer ein
    Schaetzverfahren auf Populationsebene (distributional GPT quantification).
  durchgefuehrt: 2024
  sprache: Englisch
---

# Liang et al. (2025): Quantifying LLM usage in scientific papers

> Liang, W., et al. (2025): *Quantifying large language model usage in
> scientific papers.* Nature Human Behaviour.
> <https://www.nature.com/articles/s41562-025-02273-8> ·
> Preprint: [arXiv:2404.01268](https://arxiv.org/abs/2404.01268) (v1, Apr 2024)

## Kernaussagen

- Populationsbasiertes Schätzverfahren ("distributional GPT quantification"):
  Aus Verschiebungen von Worthäufigkeiten (z.B. plötzlicher Anstieg von
  *realm*, *intricate*, *showcasing*, *pivotal* ab 2023) wird der Anteil α
  LLM-modifizierter Sätze in einem Korpus geschätzt, ohne Einzeltexte zu
  klassifizieren. Validierung im Preprint: Schätzfehler unter 3,5
  Prozentpunkten, Fehlalarmrate vor ChatGPT-Launch bei 2-3%.
- Preprint (bis Feb 2024, 950'965 Papers): deutlicher Anstieg seit ChatGPT,
  Informatik-Abstracts bis **17,5%**, Mathematik 4,9%, Nature-Portfolio
  6,3%. Publizierte Fassung (bis Sep 2024, über 1,1 Mio. Papers): Informatik
  bis ~**22%**, Mathematik und Nature-Portfolio bis ~9%.
- LLM-Nutzung ist häufiger bei Erstautor:innen mit hoher Preprint-Frequenz
  (19,3% vs. 15,6%), in dicht besetzten Forschungsfeldern (22,2% vs. 14,7%,
  gemessen über Embedding-Distanz zum ähnlichsten Paper) und bei kürzeren
  Papers (17,7% vs. 13,6%); die Autoren deuten das als Hinweis auf
  Publikationsdruck als Treiber.

## Einordnung

Schätzverfahren auf Populationsebene, keine Einzelfall-Detektion; gerade
deshalb methodisch solider als "KI-Detektoren" für Einzeltexte, deren
Unzuverlässigkeit das Paper selbst referenziert. Grenzen laut Volltext:
"LLM-modifiziert" heisst substanziell verändert (mehr als Rechtschreib- und
Grammatikkorrektur), das Trainingskorpus wurde mit GPT-3.5 erzeugt und auf
ChatGPT zugeschnitten; die Moderator-Befunde sind Korrelationen, keine
Kausalaussagen. Die Prozentwerte sind eher Untergrenzen.

## Relevanz für die Website

Belegt für [KI-Nutzung deklarieren](../../haltung/ki-deklarieren.md), dass
LLM-Nutzung beim wissenschaftlichen Schreiben **verbreitete Realität** ist:
Deklarationsregeln adressieren keinen Randfall. Zusammen mit
[Academ-AI](glynn-2024-academ-ai.md) zeigt sich die Lücke zwischen
tatsächlicher und deklarierter Nutzung. Die Abgrenzung "substanzielle
Modifikation vs. blosse Korrektur" im Messverfahren spiegelt die
Copy-Editing-Ausnahme vieler Policies.

## Querverweise

- [Glynn: Academ-AI](glynn-2024-academ-ai.md) — dokumentierte Einzelfälle nicht deklarierter Nutzung
- [Schilke & Reimann 2025](schilke-reimann-2025-transparenz-dilemma.md) — warum Deklaration schwerfällt
