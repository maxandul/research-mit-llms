---
type: Quellnotiz
title: "Glynn (2024/2025): Academ-AI"
description: >-
  Fallsammlung von 768 publizierten Arbeiten mit mutmasslich nicht
  deklarierter KI-Nutzung, erkannt an stehengebliebenen Chatbot-Phrasen.
resource: https://arxiv.org/abs/2411.15218
tags: [ki-deklarieren, empirie, transparenz, halluzination]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-06 }
verified:
  - { by: "human:andreas", at: 2026-07-06, umfang: Volltext }
stale_after: 2027-07-06

evidenzstufe: Preprint
---

# Glynn (2024/2025): Academ-AI — nicht deklarierte KI in Publikationen

**Evidenzstufe:** Preprint ·
**Geprüft:** 06.07.2026, Volltext gelesen (arXiv v2 vom 15.11.2025, aus
`rohdaten/`), arXiv-Link und Datenrepositorium (Figshare) aufgelöst.

> Glynn, A. (2024, rev. 2025): *Academ-AI: documenting the undisclosed use
> of generative artificial intelligence in academic publishing.*
> Preprint, [arXiv:2411.15218](https://arxiv.org/abs/2411.15218) (v2, Nov 2025).

## Kernaussagen

- Dokumentiert **768 Fälle mutmasslich nicht deklarierter KI-Nutzung** in
  der akademischen Literatur: 633 Journal-Artikel, 107 Konferenzbeiträge,
  28 Buchkapitel. Erkennungsmerkmal sind stehengebliebene Chatbot-Phrasen:
  Ich-Form (52% der Fälle), Hinweis auf den Wissensstand des Modells
  ("since my last update", 44%), "Certainly, here is ..." (34%), Knopf-Text
  "Regenerate response" (8%).
- Betroffen sind auch renommierte Verlage (IEEE, Springer, Elsevier stellen
  zusammen über 20% der Fälle); rund jeder vierte Fall passierte die
  Qualitätssicherung eines Grossverlags mit expliziter Deklarationspflicht.
- Journals mit solchen Fällen haben **höhere Zitationsmetriken und höhere
  Publikationsgebühren** als vergleichbare Journals (SJR- und DOAJ-Vergleich,
  p < 0.001): gerade die Outlets mit den meisten Ressourcen übersehen sie.
- Nachträgliche Korrektur ist die Ausnahme: Nur 33 von 768 Dokumenten
  (4,3%) wurden überhaupt verändert, davon 12 als intransparente
  "stealth corrections" ohne formelle Notiz. Mehrere Errata kündigen eine
  Deklaration an, die im Artikel bis heute fehlt.
- Ein illustrativer Fall: Die Phrase "Regenerate response" im
  Literaturverzeichnis führte zur Prüfung der Bibliografie, 18 von 76
  Referenzen existierten nicht (konfabuliert).
- Die 768 Fälle sind vermutlich nur die sichtbare Spitze ("dark AI"):
  Schon leichtes Gegenlesen entfernt die verräterischen Phrasen, nicht aber
  tieferliegende Probleme wie erfundene Inhalte. Glynn folgert, dass
  Verlage ihre eigenen Policies in den detektierbaren Fällen durchsetzen
  müssen, analog zur etablierten Offenlegung von Interessenkonflikten.

## Einordnung

Preprint (nicht begutachtet), aber mit offengelegten Daten (Figshare) und
klaren Ein-/Ausschlusskriterien. Manuelle Fallsammlung über
Google-Scholar-Phrasensuchen: Selektionseffekt bestätigt sich im Volltext,
erfasst werden nur die auffälligsten Fälle in englischsprachiger,
indexierter Literatur. Als Existenz- und Verbreitungsnachweis dennoch
aussagekräftig; die Prävalenz insgesamt kann daraus nicht geschätzt werden
(dafür: [Liang et al.](liang-2025-llm-praevalenz.md)).

## Relevanz für die Website

Zeigt für [KI-Nutzung deklarieren](../../haltung/ki-deklarieren.md) die
Kehrseite der Nichtdeklaration: Sie fliegt regelmässig auf, auch bei
etablierten Verlagen, und wird selten sauber korrigiert. Der Fall der 18
konfabulierten Referenzen stützt direkt die Empfehlung, KI-Output stets
gegenzulesen; das "dark AI"-Argument zeigt zugleich, dass Gegenlesen allein
Nichtdeklaration nicht heilt.

## Querverweise

- [Liang et al. 2025](liang-2025-llm-praevalenz.md) — Prävalenz auf Populationsebene
- [ICMJE](icmje-ki-nutzung-autoren.md) — Nichtdeklaration als mögliches Fehlverhalten
- [Schilke & Reimann 2025](schilke-reimann-2025-transparenz-dilemma.md) — Auffliegen schadet mehr als Offenlegen
