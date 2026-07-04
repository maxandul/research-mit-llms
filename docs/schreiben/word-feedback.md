# Mit Word-Feedback umgehen

!!! info "Auf einen Blick"
    **Schwierigkeit:** Einsteiger bis Fortgeschritten · **Kosten:** gratis ·
    **Wofür:** Kommentare aus Word zurück in die Markdown-Quelle bringen, ohne die Kette zu brechen

Wer die Arbeit [in Markdown aufbaut](arbeit-in-markdown.md), stösst schnell
auf die Realität des Wissenschaftsbetriebs: Betreuungspersonen und
Gutachter:innen kommentieren nun mal im Word-Dokument, mit Kommentaren und
nachverfolgten Änderungen. Das ist kein Grund, die Kette aufzugeben. Es
braucht nur eine klare Regel.

!!! quote "Die Regel"
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

Pandoc kann das kommentierte Word zurück nach Markdown wandeln und dabei
Kommentare und nachverfolgte Änderungen sichtbar machen:

```bash
pandoc feedback.docx --track-changes=all -t markdown -o feedback.md
```

In `feedback.md` stehen alle Anmerkungen als Text an der richtigen Stelle.
Das ist die ideale Grundlage für Weg 3.

## Weg 3: das LLM arbeitet das Feedback ein

Jetzt zahlt sich das Klartext-Format aus. Gib dem Modell beides, das
extrahierte Feedback und dein Quellkapitel:

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

Die Änderungsliste am Ende ist der wichtige Teil: Du gehst sie durch und
prüfst jede Stelle, denn die inhaltliche Antwort auf das Feedback bleibt
deine (siehe [Rollenteilung](../grundlagen/llms-verstehen.md)). Mit einem
Coding-Agenten (Claude Code, Cursor) geht dasselbe direkt auf den Dateien,
inklusive sichtbarem Diff pro Änderung.

## Versionen im Griff behalten

- Exporte datieren (`arbeit_2026-07-04.docx`), damit klar ist, auf welchem
  Stand ein Feedback beruht.
- Die Markdown-Quelle mit Git versionieren: ein Commit pro eingearbeiteter
  Feedback-Runde, dann ist nachvollziehbar, was sich wann geändert hat.
- Kommt Feedback auf eine ältere Version, zuerst prüfen, ob die Stelle
  inzwischen schon anders ist. Auch das kann das LLM übernehmen ("Welche
  dieser Kommentare betreffen Stellen, die es so noch gibt?").
