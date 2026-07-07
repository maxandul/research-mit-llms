# Marston et al. (2026): Benchmark — 46 LLMs codieren humanitäre Daten

**Evidenzstufe:** Preprint ·
**Geprüft:** 07.07.2026, Volltext gelesen (arXiv-PDF, aus `rohdaten/`).
Explizit als nicht begutachtet gekennzeichnet; Befunde als vorläufig
behandeln.

> Marston, J., Kreutzer, T., Garnier, S., Boone, E., Pham, P. N. & Vinck,
> P. (2026): *Can Large Language Models Reliably Code Qualitative
> Humanitarian Data? A Benchmark Study Against Human Expert Adjudication.*
> Preprint. <https://arxiv.org/abs/2606.26541>

## Kernaussagen

- Breit angelegter Benchmark zum deduktiven Codieren: **46 LLMs** (u.a.
  GPT-5.4, Gemini 3.1, Claude Opus 4.6, DeepSeek, Mistral, offene Modelle
  wie GPT-OSS und Gemma) codieren 150 synthetische Transkripte humanitärer
  Bedarfserhebungen gegen einen menschlichen Goldstandard, 48'300
  Codier-Iterationen, Krippendorffs Alpha plus Fehlerklassifikation plus
  qualitative Prüfung.
- **32 von 46 Modellen erreichen α ≥ 0,80**, also das Zuverlässigkeitsmass
  erfahrener menschlicher Codierer; Spitzenwert α = 0,922. Die besten
  Modelle codieren zudem über sieben Läufe hinweg konsistent.
- **Die Konfiguration entscheidet:** Reasoning-/Thinking-Modi bringen 10
  bis 15 Prozentpunkte Relevanz. Dieselbe Architektur fällt ohne Reasoning
  von "zuverlässig" auf "unzuverlässig" (Claude Sonnet 4.5 Basis:
  α = 0,651; Claude Haiku 4.5 Basis: α = 0,606). Schwächste Modelle bis
  α = 0,169.
- Aggregatwerte täuschen: Alle Modelle schwächeln systematisch bei
  **indirekt geäusserten Bedürfnissen und Schutzthemen** (physische
  Sicherheit, Diskriminierung, Einkommen). Ein Modell mit 93%
  Gesamt-Relevanz kann genau die folgenreichsten Kategorien verzerren.
  Konsequenz der Autoren: abgestufte menschliche Kontrolle je nach
  Fallhöhe der Kategorie, kein Ersatz menschlichen Urteils.
- Für sensible Daten empfehlen die Autoren **selbst gehostete
  Open-Weights-Modelle** als gangbaren Weg (Datenhoheit bei
  vergleichbarer Zuverlässigkeit der besten offenen Modelle).

## Einordnung

Preprint, nicht begutachtet. Zwei Eigenheiten des Designs: Die Transkripte
sind **synthetisch** (aus Ethikgründen; mit Feldpraktikern über neun
Iterationen validiert), und das Generierungsmodell (Claude Opus 4.6) wurde
selbst mitevaluiert und schnitt gut ab; die Autoren diskutieren dieses
Zirkularitätsrisiko, ausschliessen können sie es nicht. Nur Englisch, nur
deduktiv mit festem Codebuch (11+1 Kategorien), eine einzige, eher
klassifikationsnahe Aufgabe. Die hohen Alpha-Werte belegen also
strukturiertes Zuordnen, nicht interpretative Analyse.

## Relevanz für die Website

Aktuellster Beleg (Modellgeneration 2026) dafür, dass deduktives Codieren
mit Codebuch auf menschlichem Zuverlässigkeitsniveau möglich ist, und
zugleich der stärkste Beleg, dass **Modellwahl und Konfiguration über
Brauchbarkeit entscheiden**. Für
[Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md):
Stichprobenprüfung reicht nicht pauschal, heikle Kategorien brauchen
gezielte Kontrolle. Verbindet den Codier-Workflow mit der
Datenschutz-Frage (selbst gehostete offene Modelle).

## Querverweise

- [Kempny et al. (2026)](kempny-2026-llm-qualitativ-scoping-review.md) — ordnet die berichtete Agreement-Spannbreite der Literatur ein
- [Dunivin (2025)](dunivin-2025-scaling-hermeneutics.md) — gleiche Kernbotschaft (Konfiguration, Validierung pro Code) eine Modellgeneration früher
- [Misra et al. (2026)](misra-2026-open-source-llms-codieren.md) — schwache Ergebnisse kleiner offener Modelle als Kontrast
- Konzepte: [LLM als zweiter Codierer](../konzepte/llm-als-zweiter-codierer.md),
  [Modell und Einsatzart bestimmen das Ergebnis](../konzepte/modell-und-einsatzart.md),
  [Grenzen interpretativer Tiefe](../konzepte/grenzen-interpretativer-tiefe.md),
  [Lokale Modelle für sensible Daten](../konzepte/lokale-modelle-sensible-daten.md)
