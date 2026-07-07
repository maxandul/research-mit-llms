# Forschungsstand: Qualitative Daten codieren

**Synthese** · Stand: Juli 2026 · Quellenbasis: 5 Quellen (4 peer-reviewed,
1 Preprint), Sprint Juli 2026

Vorab der Lesegrundsatz dieses Themas: Die Studienlage ist jung (breite
LLM-Nutzung erst seit Ende 2022), lückenhaft und schnell veraltend. Alle
Befunde hängen an Modell, Version und Einsatzart, siehe
[Modell und Einsatzart bestimmen das Ergebnis](../konzepte/modell-und-einsatzart.md).
Diese Synthese formuliert deshalb bewusst Momentaufnahmen, keine
gesicherten Befunde; Jahreszahlen der Studien sind Teil der Aussage.

## Was die bisherige Evidenz nahelegt

**Deduktives Codieren mit Codebuch kann menschliches
Zuverlässigkeitsniveau erreichen, wenn Modell und Konfiguration
stimmen.** In einem breit angelegten Benchmark (46 Modelle der Generation
2026, allerdings Preprint und synthetische Daten) erreichten 32 Modelle
Krippendorffs α ≥ 0,80 gegen einen menschlichen Goldstandard; schon
GPT-4 erreichte 2024 bei einzelnen klaren Codes menschliches Niveau. Die
[Bedingungen](../konzepte/llm-als-zweiter-codierer.md): präzises
Codebuch, strukturierte Prompts, Validierung pro Code gegen menschliche
Codierung, Mensch entscheidet bei Differenzen.

**Zwei Prompt-Prinzipien tauchen übereinstimmend in mehreren Studien
auf:** Nach einer Begründung pro Codierentscheid fragen verbesserte die
Übereinstimmung deutlich (Chain-of-Thought), und kleinere Aufgabenpakete
schlugen den grossen Wurf (ein Code pro Durchgang statt ganzes Codebuch
in einem Prompt).

**Die Leistung ist keine Eigenschaft "der LLMs".** Übereinstimmungen
zwischen 36 und 99 Prozent in der Literatur erklären sich massgeblich
durch Modellwahl, Version, Reasoning-Modus, Prompt-Qualität und
Validierungsstrenge. Negative Befunde mit kleinen oder schlecht
konfigurierten Modellen widerlegen die Machbarkeit nicht, positive
garantieren nichts für die eigene Aufgabe.

## Was die Evidenz einordnet, aber nicht relativiert

**Interpretative Tiefe ist derzeit die Grenze.** Alle Quellen verorten
die Stärke beim deskriptiven und deduktiven Codieren. Bei implizit
Geäussertem, Randfällen und heiklen Kategorien (im Benchmark: physische
Sicherheit, Diskriminierung) zeigten auch die leistungsstärksten
getesteten Modelle systematische Schwächen, bei guten Aggregatwerten.
Ob kommende Modellgenerationen das beheben, ist offen. Kontrolle deshalb
[fallhöhenabhängig staffeln](../konzepte/grenzen-interpretativer-tiefe.md),
nicht gleichverteilt stichproben.

**Das Reporting der Studien selbst ist mangelhaft.** 75 Prozent der
Studien im Scoping Review nennen keine Parameter, fast die Hälfte nicht
einmal die Einsatzform. Für die eigene Praxis folgt daraus die
Dokumentationspflicht: Modellversion, Parameter, Prompts,
Validierungsschritte (Vorschlag COREQ + LLM).

## Was die Evidenz kompliziert macht

**Die methodologische Kritik ist nicht erledigt.** Ein Teil der
qualitativen Community bestreitet die Passung von LLMs und reflexiver
qualitativer Analyse grundsätzlich; beim Ersatz von Teilnehmenden durch
LLM-Personas ("synthetische Daten") ist die Ablehnung ausführlich und
bewusst modellunabhängig begründet (fehlende Positionalität,
Einwilligung, "surrogate effect").
Konsens beider Lager: Interpretationshoheit und Verantwortung bleiben
beim Menschen; LLMs erzeugen keine qualitativen Daten. Der Dissens, ob
schon maschinelles Codieren die Reflexivität verletzt, bleibt
[offen](../konzepte/methodologische-kritik-qualitativ.md).

**Lokal vs. Cloud ist eine echte Abwägung geworden.** Kleine lokale
Modelle codieren derzeit deutlich schwächer; grosse selbst gehostete
Open-Weights-Modelle mit Reasoning erreichen dagegen Spitzenniveau,
brauchen aber Infrastruktur. Details:
[Lokale Modelle für sensible Daten](../konzepte/lokale-modelle-sensible-daten.md).

**Für kleine Interviewstudien lohnt sich Automatisierung oft nicht.**
Der Aufbau eines validierten LLM-Workflows (Codebuch adaptieren,
Goldstandard codieren, vergleichen) kostet ähnlich viel wie das
Handcodieren kleiner Datensätze, das zudem Datennähe stiftet. Der
LLM-Einsatz spielt seine Stärke bei grossen Korpora aus; beim
klassischen Interviewprojekt ist er Zweitmeinung, nicht Zeitersparnis.

## Offene Punkte

- Kaum Evidenz für **deutschsprachiges Material** (die Studien sind fast
  durchgehend englischsprachig) und für induktive Codebuch-Entwicklung.
- Wenig systematische Vergleiche verschiedener Modelle am selben
  qualitativen Material; der grosse Benchmark ist ein Preprint mit
  synthetischen Daten.
- Langzeitfragen (Verlust von Datennähe und Codier-Kompetenz) sind
  unbeforscht; Anschluss an Sprint 7 (kognitive Auslagerung).

## Konsequenzen für die Website

1. [Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md)
   im Kern bestätigt (zweiter Codierer, Codebuch als Herzstück, Prüfen
   wie beim Intercoder-Vergleich, Begründung pro Zeile verlangen). Neu zu
   ergänzen: Dokumentations-Empfehlung (Modellversion, Parameter, Prompts
   im Methodenteil), Hinweis auf fallhöhenabhängige Kontrolle statt nur
   Stichprobe, Reasoning-Modelle bevorzugen, Einordnung "bei kleinen
   Studien kein Zeitgewinn", rote Linie synthetische Daten.
2. Die 20-30-Zeilen-Häppchenregel bleibt Praxiserfahrung ohne direkten
   Beleg; das "ein Code pro Durchgang"-Prinzip ist die belegte
   Verwandte. Auf der Website entsprechend kennzeichnen.
3. [Datenschutz](../../grundlagen/datenschutz.md) und Codieren-Seite:
   lokale/selbst gehostete Modelle differenzierter darstellen (Leistung
   hängt an Grösse und Reasoning, Validierung nötig).

## Quellen dieser Synthese

- [Kempny et al. (2026): Scoping Review](../quellen/kempny-2026-llm-qualitativ-scoping-review.md) · Peer-reviewed
- [Dunivin (2025): Scaling hermeneutics](../quellen/dunivin-2025-scaling-hermeneutics.md) · Peer-reviewed
- [Misra et al. (2026): Open-Source-LLMs lokal](../quellen/misra-2026-open-source-llms-codieren.md) · Peer-reviewed
- [Kapania et al. (2025): Simulacrum of Stories](../quellen/kapania-2025-simulacrum-of-stories.md) · Peer-reviewed
- [Marston et al. (2026): 46-Modelle-Benchmark](../quellen/marston-2026-humanitaere-daten-benchmark.md) · Preprint
