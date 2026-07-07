# Misra et al. (2026): Open-Source-LLMs lokal für Themenanalyse

**Evidenzstufe:** Peer-reviewed ·
**Geprüft:** 07.07.2026, Volltext gelesen (Open-Access-PDF, aus
`rohdaten/`), DOI im Original enthalten.

> Misra, R., Dahal, R., Kirk, B., Khan, R., Dogan, G., Chataut, R. &
> Gyawali, P. (2026): *Large Language Models in Qualitative Analysis:
> Comparing Traditional and Researcher-Interpreted Approaches.*
> International Journal of Qualitative Methods, 25, 1-15.
> <https://doi.org/10.1177/16094069261426100>

## Kernaussagen

- Testet bewusst **lokal laufende Open-Source-Modelle** (Gemma2 und
  Llama3.1 via Ollama/LangChain), um Patientendaten nicht in die Cloud
  geben zu müssen; ChatGPT wurde aus Datenschutzgründen ausgeschlossen.
  Material: 34 semistrukturierte Patienteninterviews (Typ-2-Diabetes,
  ländliches Appalachia); Goldstandard ist die induktive Analyse zweier
  Forscherinnen in NVivo.
- **Methodik:** Transkripte vorverarbeitet und in Häppchen von 20 Tokens
  zerlegt (auch zur Halluzinations-Kontrolle), Default-Parameter
  (Temperature 0,8), induktives vs. deduktives Vorgehen, Zero-Shot vs.
  Few-Shot. Zwei Forscherinnen bewerteten alle LLM-Codes auf Kontext,
  Duplikate und Passung zu den menschlichen Themen (Übereinstimmung der
  Bewerterinnen 74 bis 94 Prozent).
- Ergebnis ernüchternd: Nur **rund 45% der LLM-Codes lieferten sinnvollen
  Kontext**, 22 bis 39 Prozent waren Duplikate; knapp die Hälfte war zu
  kontextarm oder repetitiv. Der deduktive Ansatz (Codes entlang der
  Forschungsfrage) lieferte mehr und nuanciertere Codes als der induktive.
- Fazit der Autoren: Open-Source-LLMs taugen als Ideengeber für
  Erstcodes und können blinde Flecken aufzeigen, ersetzen aber keine
  menschliche Analyse; für höhere Zuverlässigkeit braucht es weitere
  Forschung bzw. domänenspezifische Modelle.

## Einordnung

Wichtiger Kontrapunkt zu den optimistischen GPT-4-Studien, aber die
Einsatzart erklärt einen Teil des schwachen Ergebnisses: kleine, ältere
Open-Source-Modelle, sehr kleine Chunks (20 Tokens), hohe Temperature
(0,8 statt 0) und kein Begründungsschritt. Genau deshalb illustrativ für
den Grundsatz, Befunde nie ohne Blick auf Modell und Konfiguration zu
übernehmen: "LLMs codieren schlecht" wäre die falsche Schlussfolgerung,
"diese Modelle, so eingesetzt, codieren schlecht" die richtige.
Peer-reviewed, klare Dokumentation der Pipeline.

## Relevanz für die Website

Relativiert für [Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md)
die Erwartung, der Chat-Workflow funktioniere mit jedem Modell gleich gut,
und liefert den bisher fehlenden Beleg zur Frage lokaler Modelle: Der
Datenschutz-Gewinn ([Datenschutz](../../grundlagen/datenschutz.md),
[Anonymisieren](../../erheben/anonymisieren.md)) wird derzeit mit
deutlich schwächerer Codierleistung erkauft. Diese Abwägung gehört auf
die Website.

## Querverweise

- [Kempny et al. (2026)](kempny-2026-llm-qualitativ-scoping-review.md) — benennt die Open-Source-Lücke, die diese Studie füllt
- [Marston et al. (2026)](marston-2026-humanitaere-daten-benchmark.md) — grössere Open-Weights-Modelle mit Reasoning schneiden dort deutlich besser ab
- Konzepte: [Lokale Modelle für sensible Daten](../konzepte/lokale-modelle-sensible-daten.md),
  [Modell und Einsatzart bestimmen das Ergebnis](../konzepte/modell-und-einsatzart.md),
  [Grenzen interpretativer Tiefe](../konzepte/grenzen-interpretativer-tiefe.md)
