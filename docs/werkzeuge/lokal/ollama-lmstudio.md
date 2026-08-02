---
title: Ollama und LM Studio
werkzeug:
  schwierigkeit: Fortgeschritten
  schwierigkeit_zusatz: "LM Studio: Einsteiger, Ollama über die Kommandozeile"
  kosten: gratis
  kosten_zusatz: die lokale Nutzung; Ollama bietet zusätzlich bezahlte Cloud-Modelle
  verarbeitung: beides
  verarbeitung_zusatz: lokal möglich, Ollama bietet inzwischen auch Cloud-Modelle
  wofuer: Offene Sprachmodelle auf dem eigenen Rechner betreiben
  phase: [lokal, analysieren]
  stand: August 2026
---

# Ollama und LM Studio

Zwei Wege, offene Sprachmodelle auf dem eigenen Rechner laufen zu
lassen. **Ollama** ist ein Kommandozeilen-Werkzeug mit App, das Modelle
herunterlädt und startet und eine Schnittstelle bereitstellt, an die
sich andere Programme hängen können. **LM Studio** ist eine grafische
Anwendung mit Chatfenster, Modellkatalog und Einstellungen zum Klicken.

Der Zweck ist derselbe: Text verarbeiten, ohne dass er den Rechner
verlässt. Für Interviewmaterial und andere vertrauliche Daten ist das
der Unterschied, den die
[Grundregel zum Datenschutz](../../grundlagen/datenschutz.md) meint.

!!! warnung "Ollama ist nicht mehr nur lokal"
    Ollama bietet inzwischen auch **Cloud-Modelle** an, erreichbar aus
    derselben Oberfläche, mit einem Gratis-Kontingent bei Konto und
    einem bezahlten Tarif darüber. Der Anbieter nennt Standorte in den
    USA, Europa und Singapur und gibt an, nicht mit Nutzerdaten zu
    trainieren. Offline betreiben lässt sich Ollama weiterhin.

    Wer es wegen des Datenschutzes einsetzt, muss also darauf achten,
    dass tatsächlich ein lokales Modell antwortet und nicht ein
    Cloud-Modell. "Ich benutze Ollama" ist keine Aussage über den
    Verarbeitungsort mehr.

## Wofür es taugt

- **Sensible Texte verarbeiten**, ohne die Upload-Frage zu stellen.
  Zusammenfassen, umformulieren, sortieren, alles auf dem Gerät.
- **Beim Anonymisieren gegenlesen.** Ein lokales Modell kann Transkripte
  nach übersehenen Personenbezügen durchsuchen, ohne dass die Daten
  irgendwohin gehen; siehe
  [Daten anonymisieren](../../erheben/anonymisieren.md).
- **Offene Modelle vergleichen**, bevor man sich auf eines festlegt.
- **Andere Programme anbinden.** Ollama stellt eine Schnittstelle
  bereit, über die eigene Skripte und Werkzeuge das lokale Modell
  ansprechen.

## Grenzen

- **Die Hardware entscheidet über die Qualität.** Modelle, die auf einem
  normalen Rechner laufen, sind kleiner als die Cloud-Spitzenmodelle. In
  einem Benchmark von 2026 fielen kleine offene Modelle beim
  [qualitativen Codieren](../../analysieren/qualitativ-codieren.md)
  messbar ab, während grosse offene Modelle mit Reasoning das Niveau der
  Cloud-Modelle erreichten, dafür aber Server-Infrastruktur brauchen,
  wie sie eher Institute betreiben. Belege im
  [Forschungsstand](../../wiki/konzepte/lokale-modelle-sensible-daten.md).
- **Prüfen statt vertrauen.** Bevor ein lokales Modell echte Daten
  bearbeitet, an einer kleinen Stichprobe testen, ob die Qualität für
  deine Aufgabe reicht.
- **Speicherplatz und Geduld.** Modelle sind mehrere Gigabyte gross, und
  ohne passende Grafikkarte antwortet der Rechner langsam.
- **Lokal löst nicht alles.** Die Daten bleiben bei dir, aber
  Aufbewahrung, Zugriff und Löschung richten sich weiterhin nach deinem
  Datenmanagementplan.

## Wann etwas anderes passt

Wenn das Material unproblematisch ist, sind die Cloud-Modelle in
Leistung und Bequemlichkeit voraus. Geht es nur um Transkription, sind
[noScribe](../transkribieren/noscribe.md) und
[TranscriboZH](../transkribieren/transcribozh.md) die passenderen
lokalen Werkzeuge; sie bringen alles Nötige mit, statt dass du dir ein
Modell aussuchst. Und viele Hochschulen betreiben inzwischen eigene
Modell-Dienste, die datenschutzrechtlich geprüft sind; das ist oft der
einfachere konforme Weg als ein eigener Rechner unter dem Schreibtisch.

Ollama: <https://ollama.com> · <https://docs.ollama.com> ·
LM Studio: <https://lmstudio.ai>

---

Wie lokale Modelle in den Datenschutz eingeordnet werden, steht unter
[Datenschutz & Vertraulichkeit](../../grundlagen/datenschutz.md).
