# Markdown als Arbeitsformat

Wer viel mit LLMs arbeitet, merkt schnell: Das Format der eigenen Dateien
entscheidet mit, wie gut die Zusammenarbeit klappt. Markdown ist dafür das
beste Arbeitsformat. Diese Seite erklärt warum und gibt konkrete Regeln,
damit deine Dateien für Claude, ChatGPT und Co. gut les- und bearbeitbar sind.

## Warum Markdown statt Word?

- **Reiner Text.** Ein LLM sieht genau das, was du siehst. Word-Dateien
  enthalten unsichtbares Markup, Formatierungsreste und Metadaten, die das
  Modell verwirren oder Platz im [Kontextfenster](kontextfenster.md) fressen.
- **Struktur ist explizit.** Überschriften (`#`, `##`), Listen und Tabellen
  sind als Zeichen im Text sichtbar. Das Modell erkennt den Aufbau deines
  Dokuments zuverlässig, statt ihn aus Schriftgrössen zu raten.
- **Änderungen sind nachvollziehbar.** Textdateien lassen sich Zeile für
  Zeile vergleichen und mit Git versionieren. Du siehst exakt, was ein LLM
  geändert hat.
- **LLMs kennen Markdown bestens.** Modelle sind auf riesigen Mengen
  Markdown trainiert und geben es auch selbst bevorzugt aus.

## Regeln für LLM-freundliche Markdown-Dateien

1. **Saubere Überschriften-Hierarchie.** Genau ein `#` pro Datei als Titel,
   darunter `##` und `###` in korrekter Schachtelung. Keine fett gedruckten
   Zeilen als Pseudo-Überschriften.
2. **Eine Datei pro Einheit.** Lieber ein Kapitel, ein Interview oder ein
   Konzept pro Datei als ein Monolith. Kleine Dateien passen einzeln ins
   Kontextfenster und lassen sich gezielt mitgeben.
3. **Aussagekräftige Dateinamen.** `03-methoden.md` statt `neu_final2.md`.
   Das LLM nutzt Dateinamen zur Orientierung, genau wie du.
4. **Strukturiertes als Tabelle oder Liste.** Was tabellarisch ist, gehört
   in eine Markdown-Tabelle, nicht in Fliesstext. Das Modell kann damit
   gezielter arbeiten.
5. **Bedeutung nie nur über Formatierung.** "Alles Kursive ist ein Zitat"
   geht verloren. Besser explizit: `> Zitat:` oder ein eigenes Feld.
6. **Frontmatter für Metadaten.** Ein YAML-Block am Dateianfang (Titel,
   Datum, Tags, Quelle) macht Dateien sortier- und filterbar, für dich und
   fürs LLM. Beispiel siehe
   [Vom Thema zur Literaturübersicht](../workflows/thema-zu-uebersicht.md).
7. **Konsistentes Schema über alle Dateien.** Gleiche Feldnamen, gleiche
   Reihenfolge, gleiche Tags. Konsistenz ist das, was Sammlungen später
   auswertbar macht.

## Womit Markdown schreiben und lesen?

- **Obsidian** (gratis): komfortabler Editor mit Vorschau, Verlinkung und
  Graph-Ansicht. Guter Standard für Forschungsnotizen.
- **VS Code** (gratis): Editor mit Markdown-Vorschau, ideal wenn ohnehin
  Coding-Agents wie Claude Code im Spiel sind.
- Zur Not tut es jeder Texteditor. Das ist genau der Punkt: Markdown ist
  nicht an ein Programm gebunden.

!!! tip "Der nächste Schritt"
    Markdown ist nicht nur ein Notizformat. Du kannst deine ganze Arbeit
    darin schreiben und Word nur noch als Exportformat behandeln. Wie das
    geht, zeigt [Die Arbeit in Markdown aufbauen](../schreiben/arbeit-in-markdown.md).

---

Bleibt das Querschnittsthema, das bei jedem Werkzeug mitläuft:
[Datenschutz & Vertraulichkeit](datenschutz.md).
