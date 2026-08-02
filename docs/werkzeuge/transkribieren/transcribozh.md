---
title: TranscriboZH
werkzeug:
  schwierigkeit: Profi
  schwierigkeit_zusatz: Einrichtung über die Kommandozeile, Nutzung danach im Browser
  kosten: gratis
  verarbeitung: lokal
  wofuer: Audio und Video lokal transkribieren, auch Schweizerdeutsch
  phase: [transkribieren, lokal]
  stand: August 2026
---

# TranscriboZH

Ein quelloffenes Transkriptionswerkzeug der Zürcher Kantonsverwaltung,
entwickelt vom Statistischen Amt zusammen mit der Oberstaatsanwaltschaft.
Es baut auf Whisper v3 large auf, in der unquantisierten Fassung, und
läuft vollständig auf dem eigenen Rechner. Für vertrauliche Interviews
ist das der entscheidende Unterschied zu jedem Cloud-Dienst: Die
Aufnahmen verlassen den Computer nicht.

Es ist unter MIT-Lizenz veröffentlicht und für die Nutzung nach
Schweizer Recht entwickelt worden.

## Wofür es taugt

- **Audio und Video transkribieren**, laut Projektangaben bis zu
  fünfzehnmal schneller als Echtzeit, sofern eine passende Grafikkarte
  vorhanden ist.
- **Schweizerdeutsch verarbeiten.** Das Projekt nennt für Englisch und
  Landessprachen hohe Qualität und für Schweizerdeutsch eine brauchbare
  Genauigkeit. Das ist der Punkt, an dem die meisten anderen Werkzeuge
  ausfallen.
- **Sprecher unterscheiden.** Die Diarisierung erkennt und trennt
  Sprechende automatisch; im Editor lassen sich ihnen Namen zuweisen.
- **Eigenes Vokabular vorgeben.** Über "Hotwords" legst du die
  Schreibweise von Namen und Fachbegriffen fest, bevor transkribiert
  wird.
- **Im Browser korrigieren.** Der mitgelieferte Editor spielt die
  Aufnahme synchron zum Text ab, mit Tastaturkürzeln für Start, Stopp
  und Springen. Er ist quelloffen und braucht keine Installation.
- **Exportieren** als Text, SRT für Untertitel oder als
  synchronisierter Viewer mit eingebettetem Medium.

## Voraussetzungen und Einrichtung

Der Aufwand liegt vollständig in der Einrichtung; danach bedient man das
Werkzeug im Browser.

**Hardware.** Das Projekt empfiehlt nachdrücklich eine CUDA-fähige
NVIDIA-Grafikkarte mit mindestens 8 GB VRAM, besser 16 GB, dazu 8 GB
Arbeitsspeicher. Ohne Grafikkarte läuft es auf der CPU, nach
Projektangabe aber extrem langsam. Für ein einzelnes wichtiges Interview
mag das vertretbar sein, für eine ganze Interviewstudie nicht.

**Software.** Passender NVIDIA-Treiber und CUDA, ffmpeg, eine
Conda-Umgebung mit Python 3.10, PyTorch in der zur CUDA-Version
passenden Fassung. Alternativ gibt es einen Docker-Weg, der die meisten
dieser Schritte abnimmt.

**Zugangstoken.** Die Sprechertrennung nutzt die pyannote-Modelle. Dafür
brauchst du ein HuggingFace-Konto, musst die Nutzungsbedingungen zweier
Modelle akzeptieren und einen Zugangstoken in einer `.env`-Datei
hinterlegen.

Die verbindliche Anleitung steht im Repository:
<https://github.com/machinelearningZH/audio-transcription>

!!! warnung "Token gehört nicht ins Repository"
    Der HuggingFace-Token steht in der `.env`-Datei. Sie gehört in die
    `.gitignore`, bevor der erste Commit passiert.

## Zwei Funktionen für Fortgeschrittene

**Eine REST-Schnittstelle** nimmt Dateien entgegen, meldet den
Bearbeitungsstand und liefert das Ergebnis als HTML, SRT oder Text. Damit
lässt sich die Transkription in einen eigenen Ablauf einbauen, etwa um
dreissig Interviews der Reihe nach durchlaufen zu lassen, statt sie
einzeln hochzuladen.

**Eine optionale Zusammenfassung** kann ein lokales Sprachmodell über
llama-cpp-python erzeugen. Das Projekt selbst bezeichnet das als nur für
Leute empfehlenswert, die Erfahrung mit lokalen Modellen haben, weil Code
und Parameter an die eigene Hardware angepasst werden müssen.

## Grenzen

- **Ohne Grafikkarte kaum brauchbar.** Das ist die eigentliche Hürde,
  nicht die Installation.
- **Die Einrichtung ist nichts für nebenbei.** Conda, CUDA-Versionen,
  PyTorch und Tokens greifen ineinander; wenn etwas nicht passt, sind
  die Fehlermeldungen wenig hilfreich. Ein Coding-Agent oder die
  IT-Abteilung erledigt das deutlich schneller.
- **Automatische Transkripte sind Rohmaterial.** Namen, Dialektpassagen
  und Fachbegriffe gehören gegengehört, bevor damit weitergearbeitet
  wird.
- **Lokal löst nicht alles.** Die Aufnahmen bleiben zwar auf deinem
  Rechner, aber Aufbewahrung und Löschung richten sich weiterhin nach
  deinem Ethik- und Datenmanagementplan.
- **Rechtlicher Hinweis des Projekts:** Die Software wurde für Schweizer
  Recht entwickelt; unter Umständen ist der EU AI Act auf deine Nutzung
  anwendbar. Die Prüfung liegt bei dir.

## Wann etwas anderes passt

Ohne passende Grafikkarte oder ohne Lust auf die Kommandozeile ist
[noScribe](noscribe.md) die naheliegende Alternative, auf einem Mac
[MacWhisper](macwhisper.md). Wurde das Interview ohnehin per Videocall
geführt, transkribieren
[Teams und Google Meet](online-meetings.md) direkt mit, allerdings in der
Cloud und mit schwacher Schweizerdeutsch-Qualität. Und viele Hochschulen
betreiben inzwischen eigene, datenschutzrechtlich geprüfte
Whisper-Dienste; das ist oft der einfachste konforme Weg.

Repository und Anleitung:
<https://github.com/machinelearningZH/audio-transcription>

---

Bevor Transkripte in einen Cloud-Dienst dürfen, kommt
[Daten anonymisieren](../../erheben/anonymisieren.md).
