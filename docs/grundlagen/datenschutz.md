# Datenschutz & Vertraulichkeit

Ein Querschnittsthema, das bei jedem Werkzeug mitzudenken ist, gerade in
der Forschung mit unveröffentlichten Manuskripten, fremden Daten oder
sensiblen Quellen.

!!! warnung "Grundregel"
    Lade nichts in einen Cloud-Dienst hoch, das du nicht auch per E-Mail an
    eine fremde Firma schicken würdest. Im Zweifel: anonymisieren oder
    weglassen.

## Worauf achten?

- **Wo liegen die Daten?** Cloud-Dienste verarbeiten deine Eingaben auf
  fremden Servern, oft ausserhalb der Schweiz/EU.
- **Werden Eingaben zum Training genutzt?** Viele Dienste bieten an, das
  abzuschalten. Prüfe die Einstellungen und die Datenschutzerklärung.
- **Rechte Dritter.** Urheberrecht, Personendaten in Interviews,
  Geheimhaltungsvereinbarungen: all das gilt auch beim Hochladen in ein LLM.
- **Institutionelle Vorgaben.** Deine Hochschule oder Organisation hat
  womöglich eigene Regeln zu KI-Werkzeugen und Datenschutz.

## Wenn das LLM selbst zugreift: angebundene Werkzeuge

Beim Hochladen entscheidest du bei jeder Eingabe neu, was das Modell sieht.
Anders bei angebundenen Werkzeugen (Actions, Connectors, MCP-Server): Dort
erhält das LLM dauerhaften Zugriff auf ein Konto, oft auch schreibend. Das
ist praktisch (siehe [Zotero](../werkzeuge/sammeln/zotero.md)), verlangt
aber eigene Vorsicht:

- **So wenig Rechte wie möglich.** Zugriff auf eine dedizierte Sammlung
  oder einen eigenen Ordner beschränken, nie auf das ganze Konto.
- **Zugangsschlüssel lokal halten.** API-Keys gehören in die lokale
  Konfiguration, nie in ein Repository oder einen Chat.
- **Schreibaktionen kontrollieren.** Was das LLM anlegt oder ändert,
  regelmässig durchsehen; LLMs machen Fehler.

## Der Ausweg für sensible Daten: anonymisieren

"Nichts Sensibles hochladen" heisst nicht, auf Cloud-Werkzeuge verzichten zu
müssen. Mit einer sauberen Pseudonymisierung vor dem ersten Upload lassen
sich Interviews und andere Personendaten datenschutzkonform bearbeiten.
Der Schritt-für-Schritt-Workflow:
[Daten anonymisieren](../erheben/anonymisieren.md).

## Lokale Alternativen

Wer mit besonders sensiblen Daten arbeitet, kann LLMs auch **lokal** auf dem
eigenen Rechner betreiben (Stichworte: Ollama, LM Studio). Dann verlässt
nichts den eigenen Computer, auf Kosten von etwas mehr Einrichtung. Auch die
[Transkription von Interviews](../erheben/transkription.md) geht komplett
lokal.

Zur Leistung lohnt sich ein differenzierter Blick, denn "lokal" heisst
nicht mehr automatisch "deutlich schwächer": Kleine Modelle, die auf
einem normalen Rechner laufen, fallen bei anspruchsvollen Aufgaben (etwa
dem [Codieren](../analysieren/qualitativ-codieren.md)) messbar ab. Grosse
offene Modelle mit Reasoning erreichen inzwischen das Niveau der
Cloud-Spitzenmodelle, brauchen aber Server-Infrastruktur, wie sie eher
Institute oder Hochschulen betreiben (Belege im
[Forschungsstand](../wiki/konzepte/lokale-modelle-sensible-daten.md)).
Vor dem Einsatz mit den eigenen Daten in jedem Fall an einer kleinen
Stichprobe prüfen, ob die Qualität reicht.

!!! randnotiz "Hinweis pro Werkzeug"
    Jede Werkzeug-Seite enthält einen kurzen Datenschutz-Hinweis im
    Abschnitt "Grenzen & Datenschutz". Die hier genannten Grundregeln gelten
    aber überall.

---

Damit sind die Grundlagen komplett. Weiter geht es im Forschungsprozess mit
der Literatur, beginnend beim Fundament der meisten Recherche-Werkzeuge:
[Semantic Scholar](../werkzeuge/finden/semantic-scholar.md).
