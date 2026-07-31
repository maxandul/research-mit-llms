---
type: Synthese
title: "Forschungsstand: LLMs verstehen"
description: >-
  Verdichteter Forschungsstand zum verantwortungsvollen Einsatz von LLMs in der Forschung; bewusst schmal gehalten.
tags: [llms-verstehen, verantwortung, halluzination]

generated: { by: "llm-assistiert, redigiert von human:andreas", at: 2026-07-07 }
---

# Forschungsstand: LLMs verstehen & verantwortungsvoll nutzen

**Synthese** · Stand: Juli 2026 · Quellenbasis: 3 themenübergreifende
Grundsatzquellen (2 peer-reviewed, 1 Preprint) plus Policies aus dem
Sprint "KI-Nutzung deklarieren" ·
Zugehörige Seite: [LLMs verstehen](../../grundlagen/llms-verstehen.md)

Diese Synthese bündelt das Themenfeld "Forschen mit LLMs allgemein". Sie
ist bewusst schmal gehalten und wächst mit dem Sprint "wie-llms-arbeiten"
(Halluzinationen, Kontextfenster, Tokenisierung) weiter.

## Worin die Quellen übereinstimmen

**[Verantwortung bleibt beim Menschen](../konzepte/verantwortung-bleibt-beim-menschen.md)
— Konsens über alle Lager.** In der PNAS-Debatte tragen selbst die sich
widersprechenden Positionen diesen Kern gemeinsam; die Policies (ICMJE,
COPE, Verlage) ziehen daraus die Autorschafts-Konsequenz. Die
Rollenteilung der Website (KI arbeitet zu, Mensch entscheidet, bewertet,
verantwortet) ruht damit auf einem Punkt, über den die Quellen bisher
nicht streiten.

**[LLM-Output muss geprüft werden](../konzepte/llm-output-pruefen.md), und
der Aufwand wird unterschätzt.** Erfundene Referenzen und unbearbeitet
übernommener Output sind empirisch dokumentiert (38% falsche DOIs, 16%
erfundene Referenzen in ChatGPT-generierten Anträgen; 68% reichten
LLM-Output unbearbeitet ein). Prüfkriterien gehören **vor** den Einsatz
festgelegt.

**Die Nutzung ist Normalfall, nicht Randphänomen.** Je nach Fach trugen
2024 bis gegen 22% der Papers LLM-Spuren; unter Forschenden in Ausbildung
ist die Nutzung verbreitet, formale Anleitung fehlt aber meist. Genau
diese Lücke adressiert die Website.

## Was die Evidenz einordnet

Seit dem Codieren-Sprint gilt zusätzlich der Lesegrundsatz
[Modell und Einsatzart bestimmen das Ergebnis](../konzepte/modell-und-einsatzart.md):
Pauschale Aussagen über Stärken und Schwächen "der LLMs" sind zu datieren
und an die getestete Konfiguration zu binden. Die Grundlagen-Seiten
formulieren Schwächen deshalb als mechanische Eigenheiten (Muster statt
Ausführung), nicht als feste Leistungsgrenzen.

## Offene Punkte

- Die mechanischen Einzelaussagen der Seite
  [Wie ein LLM arbeitet](../../grundlagen/wie-llms-arbeiten.md)
  (Tokenisierung/Rechnen, lost in the middle, Prompt-Sensitivität) sind
  noch nicht einzeln belegt; das leistet der geplante Sprint
  "wie-llms-arbeiten".
- Die Rolle der Betreuungsperson bei der LLM-Nutzung Studierender ist ein
  wiederkehrender Befund ohne eigenen Ort auf der Website.

## Konsequenzen für die Website

1. Rollenteilung und Prüfregel auf
   [LLMs verstehen](../../grundlagen/llms-verstehen.md) mit Quellen
   unterlegen. *(Umgesetzt Juli 2026.)*
2. Der Grundsatz Modell/Einsatzart ist im Wiki verankert und fliesst ab
   jetzt in alle Synthesen ein. *(Umgesetzt Juli 2026.)*
3. Beobachten: eigene Seite oder Abschnitt zur Rolle der
   Betreuungsperson.

## Quellen dieser Synthese

- [Binz et al. (2025): Wie sollen LLMs die Praxis der Wissenschaft verändern?](../quellen/binz-2025-llms-praxis-wissenschaft.md) · Peer-reviewed
- [Mabirizi et al. (2025): GenAI in der Postgraduierten-Forschung](../quellen/mabirizi-2025-genai-postgrad-review.md) · Peer-reviewed
- [Eger et al. (2026): Transforming Science with LLMs](../quellen/eger-2026-transforming-science-survey.md) · Preprint
- Policies: siehe [Forschungsstand: KI-Nutzung deklarieren](ki-deklarieren.md)
