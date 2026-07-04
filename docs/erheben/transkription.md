# Interviews transkribieren

!!! info "Auf einen Blick"
    **Schwierigkeit:** Profi (Alternativen: Einsteiger) · **Kosten:** gratis ·
    **Wofür:** Audio- und Videoaufnahmen lokal transkribieren, auch Schweizerdeutsch

Für qualitative Arbeiten ist die Transkription oft der mühsamste Schritt.
Whisper-basierte Werkzeuge nehmen dir den Grossteil davon ab, und zwar
**lokal auf dem eigenen Rechner**: Die Aufnahmen verlassen deinen Computer
nicht. Genau das macht sie für vertrauliche Interviews interessant.

## TranscriboZH (audio-transcription)

Ein Open-Source-Werkzeug der Kantonsverwaltung Zürich (Statistisches Amt und
Oberstaatsanwaltschaft), gebaut auf dem Whisper-v3-large-Modell.

**Was es kann:**

- Transkribiert Audio- und Videodateien in hoher Qualität, mit brauchbaren
  Ergebnissen **auch für Schweizerdeutsch**.
- **Sprecher-Diarisierung:** erkennt und unterscheidet Sprecher:innen
  automatisch.
- **Eigenes Vokabular:** Schreibweisen von Namen und Fachbegriffen vorgeben
  ("Hotwords").
- **Integrierter Editor:** Transkript im Browser korrigieren, synchron zur
  Aufnahme, mit Tastatur-Shortcuts. Export als Text, SRT oder
  synchronisierter Viewer.

**Was es braucht:**

- Am besten eine NVIDIA-Grafikkarte mit mindestens 8 GB VRAM. **Ohne GPU
  geht es auch, dauert dann aber sehr lange**: rechne mit einem Vielfachen
  der Aufnahmedauer. Für ein einzelnes wichtiges Interview vertretbar, für
  eine ganze Interviewstudie unpraktisch.
- Installation über die Kommandozeile: Conda-Umgebung, ffmpeg,
  PyTorch passend zur CUDA-Version, HuggingFace-Token für die
  Diarisierungs-Modelle. Alternativ Docker.
- Deshalb die Einstufung **Profi**. Die Anleitung im Repository ist gut,
  aber ohne Kommandozeilen-Erfahrung wird es zäh. Tipp: Die Einrichtung ist
  eine ideale Aufgabe für einen Coding-Agenten oder die IT-Abteilung, danach
  ist die Nutzung per Browser-Oberfläche einfach.

**Link:** <https://github.com/machinelearningZH/audio-transcription>

## Einsteiger-Alternativen

- **noScribe** (gratis, lokal): Whisper-Transkription mit grafischer
  Oberfläche und Sprechererkennung, entwickelt für qualitative
  Sozialforschung. Deutlich einfachere Installation, läuft auch ohne
  dedizierte GPU (langsamer). <https://github.com/kaixxx/noScribe>
- **MacWhisper** (Freemium, lokal, nur macOS): Whisper als fertige Mac-App,
  Installation per Doppelklick. <https://goodsnooze.gumroad.com/l/macwhisper>
- **Angebot der eigenen Hochschule prüfen:** Viele Hochschulen betreiben
  inzwischen eigene Whisper-Dienste, die datenschutzrechtlich geprüft sind.
  Das ist dann oft der einfachste konforme Weg.

## Grenzen & Datenschutz

- Lokal heisst: Aufnahmen und Transkripte bleiben auf deinem Rechner. Das
  löst das Upload-Problem, aber nicht die Aufbewahrung: Aufnahmen und
  Transkripte weiterhin gemäss deinem Ethik-/Datenmanagementplan sichern
  und löschen.
- Automatische Transkripte sind Rohmaterial. Namen, Dialekt-Passagen und
  Fachbegriffe immer gegenhören und korrigieren, bevor du damit
  weiterarbeitest.
- Soll das Transkript danach in einen Cloud-Dienst (etwa zum
  [Codieren](../analysieren/qualitativ-codieren.md)), führt der Weg zuerst
  über [Daten anonymisieren](anonymisieren.md).

!!! note "Hinweis zu Kosten & Limits"
    Angaben Stand Juli 2026. Verbindlich sind die verlinkten
    Original-Quellen.
