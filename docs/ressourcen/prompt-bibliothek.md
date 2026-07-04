# Prompt-Bibliothek

Kopierfertige Prompts für die häufigsten Aufgaben, geordnet nach
Forschungsphase. Alle Vorlagen sind Ausgangspunkte: an das eigene Projekt,
Fach und Vokabular anpassen.

!!! tip "Eine Regel für alle Prompts"
    Keine erfundenen Angaben zulassen. Baue in jeden Prompt eine Ausstiegs-
    Klausel ein: Was das Modell nicht weiss oder nicht im Material findet,
    soll es als Lücke ausweisen, nicht füllen.

## Literatur

Die bewährten Vorlagen stehen bei den jeweiligen Workflows:

- **Lesenotiz-Schema** für einzelne Paper:
  [Paper lesen & strukturiert ablegen](../workflows/paper-lesen-ablegen.md)
- **Ausgabe-Templates** (Wiki, Notion, Zotero) samt Router:
  [Vom Thema zur Literaturübersicht](../workflows/thema-zu-uebersicht.md)
- **Wiki-Schema** (`CLAUDE.md`):
  [Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md)

## Daten erheben & schützen

### Anonymisierungs-Check (nur lokal oder nach manueller Runde)

Für ein lokales LLM oder als zweite Prüfung nach dem manuellen
[Anonymisieren](../erheben/anonymisieren.md):

```text
Du prüfst einen pseudonymisierten Text auf verbleibende Personenbezüge.
Suche nach:
1. Namen, Orten, Institutionen, Daten, die nicht ersetzt wurden
   (auch Schreibvarianten und Abkürzungen).
2. Indirekten Identifikatoren: Kombinationen aus Beruf, Ort, Alter,
   Funktion oder einmaligen Ereignissen, die eine Person erkennbar machen.

Gib eine Liste aus: Fundstelle (Zitat), Art des Personenbezugs, Vorschlag
zur Entschärfung. Ändere den Text nicht selbst. Wenn du nichts findest,
sage das explizit.
```

## Daten analysieren

### Codebuch entwickeln (induktiv)

```text
Hier sind {N} Aussagen aus meinen Interviews zum Thema {Thema}.
Schlage mir 5 bis 10 Kategorien vor, die das Material abdecken.
Pro Kategorie: Name, Definition (1-2 Sätze), zwei Ankerbeispiele aus dem
Material (wörtlich zitiert), mögliche Abgrenzungsprobleme zu anderen
Kategorien. Erfinde keine Beispiele. Ich entscheide danach selbst, welche
Kategorien ins Codebuch kommen.
```

### Zeilenweises Codieren

Die wichtigste Vorlage, Hintergrund auf
[Qualitative Daten codieren](../analysieren/qualitativ-codieren.md):

```text
Du codierst qualitative Daten strikt nach meinem Codebuch (unten).

Regeln:
1. Codiere JEDE Zeile einzeln. Keine Zusammenfassungen, keine
   Auslassungen, keine Pauschalurteile über mehrere Zeilen.
2. Jede Zeile enthält die gestellte Frage und die Antwort. Interpretiere
   die Antwort immer im Kontext ihrer Frage ("Ja, auf jeden Fall" bedeutet
   je nach Frage etwas anderes).
3. Die Ausgabe ist eine Tabelle mit exakt so vielen Zeilen wie die
   Eingabe, mit denselben IDs: ID | Code | Begründung (1 Satz) |
   Ankerzitat (wörtlich aus der Antwort).
4. Passt keine Kategorie, vergib UNKLAR und begründe kurz. Erfinde
   keine neuen Codes.
5. Ich liefere die Daten in Blöcken von 20-30 Zeilen. Warte nach jedem
   Block auf den nächsten.

Codebuch:
{Codebuch einfügen}

Block 1:
{Zeilen im Format ID | Frage | Antwort einfügen}
```

Danach immer: Zeilenzahl und IDs der Ausgabe gegen die Eingabe prüfen.

### Intercoder-Vergleich auswerten

```text
Hier sind meine Codes und deine Codes für dieselben {N} Zeilen.
Liste alle Abweichungen auf: ID, mein Code, dein Code, und deine
Einschätzung, woran die Abweichung liegt (unscharfe Definition,
Grenzfall, Fehler). Schlage vor, welche Codebuch-Definitionen
nachgeschärft werden sollten. Entscheiden werde ich.
```

## Schreiben & Publizieren

### Feedback aus Word einarbeiten

Hintergrund auf [Mit Word-Feedback umgehen](../schreiben/word-feedback.md):

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

### Kritisches Gegenlesen

```text
Lies dieses Kapitel als kritische:r Gutachter:in. Suche:
1. Behauptungen ohne Beleg oder mit schwachem Beleg.
2. Sprünge in der Argumentation.
3. Stellen, an denen Methode und Schlussfolgerung nicht zusammenpassen.
4. Unklare oder mehrdeutige Formulierungen.

Gib pro Fund: Zitat der Stelle, Problem, konkrete Rückfrage an mich.
Schreibe den Text nicht um.
```
