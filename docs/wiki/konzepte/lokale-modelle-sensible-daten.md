# Lokale Modelle für sensible Daten

**Konzeptnotiz** · Stand: Juli 2026

Für sensible Daten (Patienteninterviews, humanitäre Erhebungen) sind
**lokal oder selbst gehostet betriebene Modelle** der Weg, Datenhoheit
zu behalten: Nichts verlässt die eigene Infrastruktur, Cloud-Dienste wie
ChatGPT scheiden aus Datenschutzgründen aus. Die Evidenz zeigt aber ein
Leistungsgefälle, das von der Modellgrösse und -generation abhängt:
Kleine lokale Modelle (Gemma2, Llama3.1 via Ollama, 2026 publiziert)
lieferten zur Hälfte kontextarme oder duplizierte Codes; grosse offene
Modelle mit aktiviertem Reasoning (etwa GPT-OSS-120b) erreichten im
selben Jahr dagegen Zuverlässigkeitswerte auf dem Niveau proprietärer
Spitzenmodelle (α ≥ 0,80). "Lokal" ist also kein pauschaler
Qualitätsverzicht mehr, aber die Abwägung Datenschutz gegen Leistung
muss pro Modell validiert werden, nicht angenommen.

Offen bleibt der Ressourcenaspekt: Die leistungsfähigen offenen Modelle
brauchen Infrastruktur, die einzelne Forschende selten haben
(Self-Hosting, GPU-Server); realistisch ist das eher auf Ebene von
Instituten oder Organisationen.

## Belege

- [Misra et al. (2026)](../quellen/misra-2026-open-source-llms-codieren.md) — Peer-reviewed (kleine lokale Modelle, ernüchternde Codequalität)
- [Marston et al. (2026)](../quellen/marston-2026-humanitaere-daten-benchmark.md) — Preprint (grosse Open-Weights-Modelle zuverlässig; Empfehlung Self-Hosting für sensible Daten)
- [Dunivin (2025)](../quellen/dunivin-2025-scaling-hermeneutics.md) — Peer-reviewed (2024 noch: offene Modelle den Aufgaben nicht gewachsen; Begründungspflicht für proprietäre Wahl)

## Verwandte Konzepte

- [Modell und Einsatzart bestimmen das Ergebnis](modell-und-einsatzart.md) — die Abwägung verschiebt sich mit jeder Modellgeneration
- [LLM als zweiter Codierer](llm-als-zweiter-codierer.md) — Anwendungsfall der Abwägung

## Fliesst ein in

- [Synthese: Qualitative Daten codieren](../synthese/qualitativ-codieren.md)
- [Website: Datenschutz & Vertraulichkeit](../../grundlagen/datenschutz.md) (Abschnitt "Lokale Alternativen")
- [Website: Qualitative Daten codieren](../../analysieren/qualitativ-codieren.md)
