# Quantitativ auswerten

Moderne Chat-Werkzeuge können nicht nur reden, sondern auch **Code schreiben
und ausführen**: ChatGPT (Funktion "Datenanalyse", früher Code Interpreter)
und Claude (Analysis) nehmen eine Datentabelle entgegen, schreiben Python-
oder JavaScript-Code, führen ihn aus und zeigen Ergebnis samt Diagramm.

Damit rechnet nicht das Modell, sondern ein Programm. Das ist keine
Feinheit: Ein Modell, das Zahlen im Kopf fortsetzt, liegt regelmässig
daneben, siehe [Wie ein LLM arbeitet](../grundlagen/wie-llms-arbeiten.md).
Ein ausgeführtes Programm dagegen ist so richtig wie sein Code, und den
kannst du lesen.

!!! merksatz "Wenn du nur eines mitnimmst"
    Lass dir den Code zeigen und heb ihn auf. Er ist dein
    Analyseprotokoll: ohne ihn ist die Auswertung weder reproduzierbar
    noch im Methodenteil belegbar.

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
2. **Code anzeigen lassen und aufheben.** Lokal speichern, nicht im Chat
   liegen lassen; Chatverläufe verschwinden.
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

- **Der Code kann falsch sein und trotzdem laufen.** Ein Programm, das
  ohne Fehlermeldung durchläuft, hat nicht bewiesen, dass es das
  Richtige rechnet. Falsch herum kodierte Variablen, stillschweigend
  gelöschte Fälle und vertauschte Gruppen erzeugen plausible Zahlen.
  Deshalb Regel 3.
- **Sehr grosse Datensätze überfordern die Chat-Umgebungen.** Dann ist
  ein Statistikprogramm (R, SPSS, Python lokal) die bessere Wahl; den
  Code dafür kann dir das Modell weiterhin schreiben und erklären.
- **Die Ausführungsumgebungen haben Zeit- und Speicherlimits.** Komplexe
  Modelle wie Mehrebenenanalysen oder grosse Simulationen gehören in
  eine lokale Umgebung.
- **Zur Korrektheit LLM-generierten Analysecodes gibt es hier noch keine
  Belege.** Der Recherche-Sprint dazu ist geplant, siehe
  [Über dieses Wiki](../wiki/index.md).

---

Die Ergebnisse wollen aufgeschrieben sein. Wie die ganze Arbeit in
Markdown entsteht und Word nur noch Exportformat ist:
[Die Arbeit in Markdown aufbauen](../schreiben/arbeit-in-markdown.md).
