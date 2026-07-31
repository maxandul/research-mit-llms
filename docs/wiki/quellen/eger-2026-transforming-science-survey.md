---
type: Quellnotiz
title: "Eger et al. (2026): Transforming Science with LLMs"
description: >-
  Workflow-zentrierter Survey ueber fuenf Etappen des Forschungszyklus;
  Gesamtfazit: begrenzte, ungleich verteilte Faehigkeiten, ergaenzender
  Werkzeugkasten statt Ersatz.
resource: https://arxiv.org/abs/2502.05151
tags: [llms-verstehen, review, literaturrecherche, peer-review]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-06 }
verified:
  - { by: "human:andreas", at: 2026-07-06, umfang: "Volltext teilweise" }
stale_after: 2027-07-06

evidenzstufe: Preprint
studie:
  modelle: "diverse, Survey ueber Fremdstudien"
  einsatzart: >-
    Literatur-Survey ueber fuenf Etappen des Forschungszyklus, Stand arXiv
    v3 (Maerz 2026), begleitendes Ressourcen-Repository.
  durchgefuehrt: 2026-03
---

# Eger et al. (2026): Transforming Science with LLMs — Survey

**Evidenzstufe:** Preprint ·
**Geprüft:** 06.07.2026, Volltext (arXiv v3 vom 05.03.2026, 46 S., aus
`rohdaten/`): Einleitung, Methodik, Ethik-Kapitel und Fazit vollständig
gelesen, die fünf Aufgaben-Kapitel kursorisch (Struktur, Limitations).
arXiv-Link aufgelöst; begleitendes, laufend aktualisiertes
Ressourcen-Repository auf GitHub.

> Eger, S., Cao, Y., D'Souza, J., et al. (2026): *Transforming Science
> with Large Language Models: A Survey on AI-assisted Scientific
> Discovery, Experimentation, Content Generation, and Evaluation.*
> Preprint, [arXiv:2502.05151](https://arxiv.org/abs/2502.05151) (v3, März 2026).

## Kernaussagen

- Workflow-zentrierter Survey über fünf Etappen des Forschungszyklus:
  (1) Literatursuche und -zusammenfassung, (2) Ideen-/Hypothesengenerierung
  und Experimente, (3) Texterstellung, (4) multimodale Inhalte (Abbildungen,
  Tabellen, Folien), (5) Peer Review; je mit Datensätzen, Methoden,
  Evaluation und Grenzen.
- Gesamtfazit: Die Fähigkeiten sind **begrenzt und ungleich verteilt**;
  viele Methoden hängen an engen Benchmarks, generalisieren schlecht und
  brauchen substanzielle menschliche Aufsicht. AI4Science sei derzeit als
  **ergänzender Werkzeugkasten** zu verstehen, nicht als Ersatz
  menschlicher Expertise.
- Zur Literatursuche: Kategorisiert die Werkzeuglandschaft (semantische
  Suche wie Elicit/Consensus/OpenScholar, graphbasierte Systeme, Paper-Chat,
  Recommender). Grenzen: Abdeckungslücken, Ranking-Bias, und viele Tools
  hängen an proprietären Daten und wechselnden LLM-Backends, was
  Reproduzierbarkeit erschwert.
- Ethik-Kapitel bündelt die Verlags-Perspektive: volle
  Autor:innen-Verantwortung, transparente Deklaration (teils inkl. Prompts
  und Tool-Versionen), keine KI-Autorschaft, Verbot im Review-Prozess;
  dazu Befunde zu Halluzination, Bias und Trustworthiness-Benchmarks.
- Kontext: Zitationen von LLM-Papers steigen auch ausserhalb der
  Informatik rasant (Analyse über ~148'000 Papers aus 22 Disziplinen);
  laut einer Wiley-Befragung erwarten Forschende breite Normalisierung,
  nutzen KI bisher aber v.a. als Schreibhilfe.

## Einordnung

Preprint (bei ACM eingereicht, Stand v3 nicht begutachtet), 14
Autor:innen, NLP-Perspektive: Der Blick gilt Modellen, Datensätzen und
Benchmarks, weniger der Forschungspraxis von Anwender:innen. Bewusst
kuratierend statt erschöpfend. Als technisches Nachschlagewerk und
Aktualitätsanker stark (wird gepflegt, GitHub-Ressourcenliste), für
praxisnahe Empfehlungen nur indirekt ergiebig.

## Relevanz für die Website

Validiert den Aufbau der Website entlang des Forschungsprozesses: Die
fünf Survey-Etappen decken sich weitgehend mit den Website-Rubriken
(Finden, Erheben, Analysieren, Schreiben). Das Gesamtfazit ("ergänzender
Werkzeugkasten, menschliche Aufsicht nötig") ist die technische
Begründung der Website-Haltung. Die Werkzeug-Kategorisierung und die
dokumentierten Grenzen der Such-Tools sind direkt für die
Werkzeuge-Seiten (Elicit, Semantic Scholar, Connected Papers) nutzbar.

## Querverweise

- [Binz et al. 2025](binz-2025-llms-praxis-wissenschaft.md) — normative Debatte zur selben Werkzeuglandschaft
- [Mabirizi et al. 2025](mabirizi-2025-genai-postgrad-review.md) — Nutzungsempirie bei Forschenden in Ausbildung
- [Liang et al. 2025](liang-2025-llm-praevalenz.md) — Prävalenz LLM-modifizierter Texte
