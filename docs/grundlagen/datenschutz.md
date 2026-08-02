# Datenschutz & Vertraulichkeit

Diese Frage läuft bei jedem Werkzeug auf dieser Website mit. In der
Forschung geht es dabei selten nur um eigene Daten: unveröffentlichte
Manuskripte, Interviews mit Dritten, Material unter
Geheimhaltungsvereinbarung.

!!! warnung "Grundregel"
    Ein Upload ist keine Werkzeugnutzung, sondern eine Weitergabe an ein
    fremdes Unternehmen. Ob du dazu befugt bist, entscheidet das Material,
    nicht das Werkzeug. Kläre das, bevor du hochlädst; im Zweifel
    anonymisieren oder weglassen.

## Worauf achten?

- **Wo liegen die Daten?** Cloud-Dienste verarbeiten deine Eingaben auf
  fremden Servern, oft ausserhalb der Schweiz/EU.
- **Werden Eingaben zum Training genutzt?** Viele Dienste bieten an, das
  abzuschalten. Prüfe die Einstellungen und die Datenschutzerklärung.
- **Was für dein Material gilt.** Je nach Fall greifen Datenschutzrecht,
  Auflagen der Ethikkommission, Bedingungen von Fördergebern,
  Geheimhaltungsvereinbarungen, Urheberrecht, Verlagsverträge oder ein
  Berufsgeheimnis. Welche davon, hängt von Fach, Datenart, Institution
  und Land ab.
- **Institutionelle Vorgaben.** Viele Hochschulen haben eigene Regeln zu
  KI-Werkzeugen. Sie sind der erste Ort zum Nachschauen, ersetzen aber
  die übrigen Pflichten nicht.

Diese Seite kann nicht klären, was in deinem Fall gilt, und ersetzt keine
Rechts- oder Datenschutzberatung. Sie soll nur erreichen, dass du die
Frage stellst, bevor die Datei hochgeladen ist.

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

## Sensible Daten: anonymisieren statt verzichten

Die Grundregel oben verlangt keinen Verzicht auf Cloud-Werkzeuge. Mit
einer sauberen Pseudonymisierung vor dem ersten Upload lassen sich
Interviews und andere Personendaten bearbeiten, ohne die Regel zu
verletzen. Wie das Schritt für Schritt geht, steht unter
[Daten anonymisieren](../erheben/anonymisieren.md); dort stehen auch die
Grenzen des Verfahrens.

## Lokale Alternativen

Wer mit besonders sensiblen Daten arbeitet, kann LLMs auch **lokal** auf
dem eigenen Rechner betreiben, etwa mit
[Ollama oder LM Studio](../werkzeuge/lokal/ollama-lmstudio.md). Auch die
[Transkription von Interviews](../erheben/transkription.md) geht
vollständig lokal.

!!! warnung "Werkzeug heisst nicht Verarbeitungsort"
    Mehrere dieser Werkzeuge bieten inzwischen zusätzlich Cloud-Modelle
    an, erreichbar aus derselben Oberfläche. Ollama etwa lässt sich
    weiterhin offline betreiben, führt aber auch bezahlte Cloud-Modelle.
    Dass ein Werkzeug installiert ist, sagt also nichts darüber, wo
    gerechnet wird. Prüfe, welches Modell tatsächlich antwortet.

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

Damit sind die Grundlagen durch. Weiter im Forschungsprozess mit dem
Bereich [Literatur](../literatur/index.md): Werkzeuge zum Finden,
Befragen und Sammeln, dazu drei durchgängige Workflows.
