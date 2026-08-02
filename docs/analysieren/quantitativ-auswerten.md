# Quantitativ auswerten

Moderne Chat-Werkzeuge können nicht nur reden, sondern auch **Code schreiben
und ausführen**: ChatGPT (Funktion "Datenanalyse", früher Code Interpreter)
und Claude (Analysis) nehmen eine Datentabelle entgegen, schreiben Python-
oder JavaScript-Code, führen ihn aus und zeigen Ergebnis samt Diagramm.

Das ist der entscheidende Unterschied zum blossen Chat: Nicht das Modell
"rechnet im Kopf" (das ist unzuverlässig, siehe
[Wie ein LLM arbeitet](../grundlagen/wie-llms-arbeiten.md)), sondern es
schreibt ein Programm, und das Programm rechnet. Die Zahlen stimmen dann so
gut wie der Code.

## Was gut funktioniert

- **Deskriptive Statistik:** Verteilungen, Mittelwerte, Kreuztabellen,
  fehlende Werte finden.
- **Visualisierung:** Diagramme aus der eigenen Tabelle, inklusive Anpassung
  ("beschrifte die Achsen auf Deutsch").
- **Datenaufbereitung:** umkodieren, filtern, zusammenführen, aus breitem
  ins lange Format bringen.
- **Standardtests mit Erklärung:** t-Test, Chi-Quadrat, Korrelationen,
  einfache Regressionen, inklusive der Erklärung, was der Test voraussetzt
  und was das Ergebnis bedeutet.
- **Lernen:** "Erkläre mir, warum du diesen Test gewählt hast" ist oft
  lehrreicher als manches Statistik-Tutorial.

## Spielregeln

1. **Nur anonymisierte Daten hochladen.** Auch Tabellen können
   Personenbezug haben, siehe [Daten anonymisieren](../erheben/anonymisieren.md).
2. **Code anzeigen lassen und aufheben.** Der ausgeführte Code ist dein
   Analyseprotokoll. Lokal speichern, dann ist die Auswertung
   reproduzierbar und im Methodenteil belegbar.
3. **Ergebnisse plausibilisieren.** Stimmen Fallzahlen und Vorzeichen?
   Eine Handvoll Werte von Hand oder in Excel nachprüfen.
4. **Methodenwahl nicht delegieren.** Das LLM schlägt Tests vor und
   begründet sie, aber ob das Design die Frage beantwortet, ist eine
   fachliche Entscheidung. Bei Unsicherheit die Statistik-Beratung der
   Hochschule nutzen.
5. **Verstehen statt abnicken.** Lass dir jeden Schritt erklären, bis du
   ihn selbst vertreten kannst. Was du übernimmst, verantwortest du.

## Typischer Ablauf

1. Anonymisierte Tabelle (CSV/Excel) in den Chat laden.
2. Kontext geben: was die Spalten bedeuten, was die Forschungsfrage ist.
3. Mit Deskriptivem starten ("Beschreibe die Stichprobe"), dann gezielt
   auswerten.
4. Am Ende: kompletten Code und alle Abbildungen exportieren und ablegen.
5. Einsatz im Methodenteil dokumentieren
   ([KI-Nutzung deklarieren](../haltung/ki-deklarieren.md)).

## Grenzen

- Sehr grosse Datensätze überfordern die Chat-Umgebungen; dann ist ein
  echtes Statistikprogramm (R, SPSS, Python lokal) die bessere Wahl. Das
  LLM kann dir dafür weiterhin den Code schreiben und erklären.
- Die Ausführungsumgebungen haben Zeit- und Speicherlimits; komplexe
  Modelle (Mehrebenenanalysen, grosse Simulationen) gehören in eine lokale
  Umgebung.

---

Die Ergebnisse wollen aufgeschrieben sein. Wie die ganze Arbeit in
Markdown entsteht und Word nur noch Exportformat ist:
[Die Arbeit in Markdown aufbauen](../schreiben/arbeit-in-markdown.md).
