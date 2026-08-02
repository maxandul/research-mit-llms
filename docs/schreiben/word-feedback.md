# Mit Word-Feedback umgehen

Wer die Arbeit [in Markdown aufbaut](arbeit-in-markdown.md), bekommt das
Feedback trotzdem in Word: Betreuungspersonen und Gutachter:innen
kommentieren dort, mit Anmerkungen und nachverfolgten Änderungen. Das
lässt sich nicht ändern, aber es braucht die Kette nicht zu brechen.

!!! merksatz "Die Regel"
    Feedback wird **nie im Word-Dokument eingearbeitet**. Das Word ist ein
    Export und wird beim nächsten Mal überschrieben. Jede Änderung wandert
    zurück in die Markdown-Quelle. Nur so bleibt die Quelle die Wahrheit.

## Weg 1: von Hand übertragen (Einsteiger)

Bei überschaubarem Feedback der einfachste Weg: kommentiertes Word und
Markdown-Datei nebeneinander, Kommentare der Reihe nach durchgehen und die
Änderungen in der Quelle machen. Danach neu exportieren und bei Bedarf die
neue Version zurückschicken.

Praktisch: In der Markdown-Datei erledigte Punkte mit einer kurzen
To-do-Liste abhaken, dann geht nichts verloren.

## Weg 2: Kommentare maschinell herausziehen (Fortgeschritten)

[Pandoc](../werkzeuge/schreiben/pandoc.md) kann das kommentierte Word
zurück nach Markdown wandeln und dabei Kommentare und nachverfolgte
Änderungen sichtbar machen:

```bash
pandoc feedback.docx --track-changes=all -t markdown -o feedback.md
```

In `feedback.md` stehen alle Anmerkungen als Text an der richtigen
Stelle, damit auch ein Modell sie lesen kann. Das ist die Grundlage für
Weg 3.

## Weg 3: das LLM arbeitet das Feedback ein

Weil beides Klartext ist, kannst du dem Modell das extrahierte Feedback
und dein Quellkapitel zusammen geben:

```text
Hier ist mein Kapitel (Markdown) und das Feedback meiner Betreuerin
(aus Word extrahiert, Kommentare im Text markiert).

Arbeite das Feedback in das Kapitel ein. Regeln:
1. Nimm nur Änderungen vor, die sich auf einen konkreten Kommentar
   zurückführen lassen.
2. Liste am Ende jede Änderung auf: Kommentar, was du geändert hast,
   und wo.
3. Wenn ein Kommentar mehrere Lösungen zulässt oder du ihn nicht
   verstehst, ändere nichts und stelle mir stattdessen eine Rückfrage.
```

Regel 2 ist der Grund, warum der Prompt so aussieht: Ohne
Änderungsliste müsstest du das ganze Kapitel neu lesen, um zu sehen, was
passiert ist. Mit ihr gehst du Stelle für Stelle durch. Die inhaltliche
Antwort auf das Feedback bleibt in jedem Fall deine, siehe
[Rollenteilung](../grundlagen/llms-verstehen.md).

Mit einem [Coding-Agenten](../werkzeuge/agenten/coding-agenten.md) geht
dasselbe direkt auf den Dateien, mit sichtbarem Unterschied pro Änderung.

## Grenzen

- **Kommentare sind oft nicht ausformuliert.** "Unklar" oder ein
  Fragezeichen am Rand verlangen eine Rückfrage bei der Person, nicht
  eine Vermutung des Modells. Regel 3 im Prompt oben fängt das ab,
  solange du dich daran hältst.
- **Nachverfolgte Änderungen sind Vorschläge, keine Anweisungen.** Wer
  sie ungeprüft übernimmt, übernimmt auch Missverständnisse.
- **Der Export verliert Feinlayout.** Wenn das Word bereits
  formatierte Tabellen oder ein Deckblatt enthält, kommt beides beim
  Rückweg nicht heil an. Der Rückweg ist für den Text gedacht, nicht
  für das Layout.

## Versionen im Griff behalten

- Exporte datieren (`arbeit_2026-07-04.docx`), damit klar ist, auf welchem
  Stand ein Feedback beruht.
- Die Markdown-Quelle mit Git versionieren: ein Commit pro eingearbeiteter
  Feedback-Runde, dann ist nachvollziehbar, was sich wann geändert hat.
- Kommt Feedback auf eine ältere Version, zuerst prüfen, ob die Stelle
  inzwischen schon anders ist. Auch das kann das LLM übernehmen ("Welche
  dieser Kommentare betreffen Stellen, die es so noch gibt?").

---

Zum Schluss des Forschungsprozesses die Haltungsfrage: Wie legst du den
KI-Einsatz sauber offen? [KI-Nutzung deklarieren](../haltung/ki-deklarieren.md).
