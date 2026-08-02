---
title: noScribe
werkzeug:
  schwierigkeit: Einsteiger
  schwierigkeit_zusatz: Installation per Doppelklick, keine Kommandozeile
  kosten: gratis
  verarbeitung: lokal
  wofuer: Interviews lokal transkribieren, mit Optionen für qualitative Forschung
  phase: [transkribieren, lokal]
  stand: August 2026
---

# noScribe

noScribe transkribiert Interviews vollständig auf dem eigenen Rechner,
mit grafischer Oberfläche und ohne Kommandozeile. Entwickelt hat es
Kai Dröge, promovierter Soziologe an der Hochschule Luzern und am
Institut für Sozialforschung Frankfurt. Das merkt man dem Werkzeug an:
Es kennt Optionen, die man nur braucht, wenn man qualitativ arbeitet.

Es ist quelloffen (GPL-3.0), kostenlos und läuft unter Windows, macOS
und Linux. Unter der Haube arbeiten Whisper, faster-whisper und pyannote.

!!! warnung "Nachahmer im Netz"
    Jemand hat die Domain **noscribe.ai** registriert und verkauft dort
    Transkriptionsdienste. Das hat mit diesem Projekt nichts zu tun. Der
    Entwickler weist ausdrücklich darauf hin. Die offizielle Seite ist
    <https://noscribe.de>, der Quellcode liegt auf GitHub.

## Wofür es taugt

- **Interviews transkribieren, ohne dass sie den Rechner verlassen.**
  Kein Konto, keine Cloud, keine Upload-Frage.
- **Sprecher unterscheiden.** Anzahl vorgeben oder automatisch erkennen
  lassen; abschalten halbiert die Rechenzeit.
- **Transkriptionskonventionen abbilden.** Pausen werden je nach
  Einstellung ab einer, zwei oder drei Sekunden markiert, in Klammern
  mit einem Punkt pro Sekunde. Überlappendes Sprechen kann in
  Doppelschrägstriche gesetzt werden. Und Verzögerungslaute und
  Wortabbrüche lassen sich mittranskribieren, statt sie zu glätten. Für
  eine Konversationsanalyse ist genau das der Unterschied zwischen
  brauchbar und wertlos.
- **Im mitgelieferten Editor korrigieren.** Der Text folgt der Aufnahme,
  Wiedergabe per Tastenkürzel, Geschwindigkeit einstellbar.
- **Mehrere Dateien nacheinander abarbeiten.** Seit Version 0.7 gibt es
  eine Warteschlange, praktisch bei einer ganzen Interviewstudie.
- **Passende Formate ausgeben.** HTML als Standard, das jede
  QDA-Software liest, VTT für den Import nach EXMARaLDA, oder Text.

## Voraussetzungen

Der Download ist mehrere Gigabyte gross, weil die Modelle enthalten
sind. Installiert wird per Setup-Datei beziehungsweise durch Ziehen ins
Programmverzeichnis.

Für Windows gibt es zwei Fassungen: eine normale für Rechner ohne
NVIDIA-Grafikkarte und eine CUDA-Fassung, die eine Karte mit mindestens
6 GB VRAM und einen aktuellen Treiber verlangt. Auf dem Mac läuft die
aktuelle Version auf Apple Silicon ab macOS 14; für ältere Intel-Macs
gibt es nur eine frühere Version.

**Rechne mit Zeit.** Ein einstündiges Interview kann bis zu drei Stunden
Verarbeitung brauchen und lastet den Rechner aus. Auf Akku ist das keine
gute Idee.

## Grenzen

- **Halluzinationen in stillen Passagen.** Whisper erfindet in Stille
  oder bei Hintergrundgeräuschen mitunter Text. noScribe filtert
  Nicht-Sprache heraus, aber es sind auch Fälle berichtet, in denen
  Wörter erfunden wurden, die syntaktisch passen und im Audio nicht
  vorkommen. Solche Fehler sind besonders schwer zu finden.
- **Namen von Personen, Orten und Organisationen** werden häufig falsch
  geschrieben. Genau die brauchst du beim Anonymisieren.
- **Schleifen bei langen Dateien.** Das Modell kann sich in wiederholtem
  Text verfangen; dann hilft, in Abschnitten zu transkribieren.
- **Zeichensetzung und Grossschreibung** können über lange Interviews
  hinweg nachlassen.
- **Schweizerdeutsch geht, kostet aber Nacharbeit.** Whisper kommt mit
  Dialekten laut Projekt ordentlich zurecht, das Ergebnis braucht aber
  mehr Korrektur als Hochdeutsch.
- **Nonverbales wie Lachen** wird nicht transkribiert und muss von Hand
  ergänzt werden.

!!! warnung "Die Protokolldateien enthalten deinen Text"
    noScribe legt für jeden Auftrag eine Protokolldatei im
    Benutzerverzeichnis ab, und darin steht auch der transkribierte
    Text. Bei vertraulichen Interviews gehören diese Dateien in dieselbe
    Behandlung wie die Transkripte selbst.

## Wann etwas anderes passt

Wenn eine leistungsfähige NVIDIA-Karte vorhanden ist und es auf Tempo
oder eine Schnittstelle für viele Dateien ankommt, ist
[TranscriboZH](transcribozh.md) die stärkere Lösung, mit deutlich
höherem Einrichtungsaufwand. Auf einem Mac ist
[MacWhisper](macwhisper.md) noch einen Schritt einfacher. Wurde das
Gespräch ohnehin per Videocall geführt, transkribieren
[Teams und Google Meet](online-meetings.md) direkt mit, allerdings in der
Cloud.

Offizielle Seite: <https://noscribe.de> ·
Quellcode: <https://github.com/kaixxx/noScribe>

Zitierfähig nach APA: Dröge, K. (2025). *noScribe. AI-powered Audio
Transcription* [Computer software].

---

Bevor Transkripte in einen Cloud-Dienst dürfen, kommt
[Daten anonymisieren](../../erheben/anonymisieren.md).
