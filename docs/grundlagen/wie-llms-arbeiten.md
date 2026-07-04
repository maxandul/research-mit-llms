# Wie ein LLM arbeitet

[LLMs verstehen & verantwortungsvoll nutzen](llms-verstehen.md) klärt die
Haltungsfrage: Was lässt sich delegieren, was bleibt bei dir? Diese Seite
geht eine Ebene tiefer. Wer ein paar mechanische Eigenheiten von LLMs kennt,
versteht, *warum* bestimmte Aufgaben zuverlässig funktionieren und andere
systematisch schiefgehen. Und kann die Werkzeuge entsprechend einsetzen.

## Tokens: das Modell denkt nicht in Wörtern

Text wird für das Modell in "Tokens" zerlegt, also Wortbausteine von wenigen
Zeichen Länge. Das Modell sieht nie einzelne Buchstaben und rechnet nicht mit
Zahlen, sondern setzt Token-Folgen fort.

**Praktische Folge:** Aufgaben, die exaktes Zählen oder Rechnen verlangen
(Wörter zählen, Buchstaben rückwärts, Arithmetik), sind unzuverlässig, obwohl
sie trivial wirken. Verlässlich wird Rechnen erst, wenn das Modell dafür
Code schreibt und ausführt (siehe
[Quantitativ auswerten](../analysieren/quantitativ-auswerten.md)).

## Das Modell lernt im Chat nichts dazu

Ein LLM wird einmal trainiert und ist danach eingefroren. Was du ihm im Chat
erklärst, verändert das Modell nicht. Es steht nur so lange zur Verfügung,
wie es im [Kontextfenster](kontextfenster.md) liegt. Neue Unterhaltung heisst:
alles vergessen.

**Praktische Folge:** "Das habe ich dir doch schon gesagt" funktioniert über
Sitzungen hinweg nicht. Wissen, das bleiben soll, gehört in eine externe
Ablage, die du bei Bedarf wieder mitgibst: ein Dokument, ein Template oder
ein [LLM-Wiki](rag-vs-wiki.md).

## Die Ausgabe ist probabilistisch

Das Modell wählt das nächste Token nach Wahrscheinlichkeiten, mit einem
bewussten Zufallsanteil. Derselbe Prompt kann heute eine andere Antwort
liefern als morgen.

**Praktische Folge:** Ein einmaliges gutes Ergebnis ist kein Beleg, dass es
immer klappt. Wichtige Ergebnisse reproduzieren oder stichprobenartig
gegenprüfen. Und umgekehrt: Eine schwache Antwort heisst nicht, dass die
Aufgabe unmöglich ist. Ein zweiter Anlauf mit präziserem Prompt lohnt sich.

## Mustervervollständigung statt Abarbeitung

Ein LLM ist kein Programm, das eine Liste Punkt für Punkt durchläuft. Es
setzt Muster fort. Gibst du ihm 200 Tabellenzeilen zum Codieren, "erkennt"
es nach 30 Zeilen das Muster und neigt dazu, den Rest grosszügig zu schätzen
oder zusammenzufassen, statt jede Zeile einzeln zu bearbeiten.

**Praktische Folge:** Bei Aufgaben über viele Einzelelemente (Zeilen,
Einträge, Dateien) explizit Vollständigkeit einfordern, in Häppchen arbeiten
und das Ergebnis nachzählen. Wie das konkret geht, zeigt
[Qualitative Daten codieren](../analysieren/qualitativ-codieren.md).
Garantiert vollständig wird es erst, wenn eine echte Programmschleife die
Elemente durchläuft und das LLM nur den Inhalt je Element bearbeitet.

## Alles läuft durch das Kontextfenster

Das Modell sieht pro Anfrage nur, was ins Kontextfenster passt: Frage,
Verlauf und mitgegebene Inhalte. Mehr Material heisst nicht bessere
Antworten, im Gegenteil. Details dazu auf der Seite
[Das Kontextfenster](kontextfenster.md).

## Zusammenfassung

| Mechanik | Praktische Konsequenz |
|----------|----------------------|
| Text wird als Tokens verarbeitet | Zählen und Rechnen nicht dem Chat überlassen, sondern Code ausführen lassen |
| Kein Dazulernen im Chat | Bleibendes Wissen extern ablegen (Dokument, Template, Wiki) |
| Probabilistische Ausgabe | Wichtige Ergebnisse reproduzieren und gegenprüfen |
| Muster statt Schleife | Bei Listenaufgaben Vollständigkeit einfordern, häppchenweise arbeiten, nachzählen |
| Begrenztes Kontextfenster | So viel wie nötig, so wenig wie möglich mitgeben |

!!! quote "Der rote Faden"
    Fast alle Überraschungen im Alltag mit LLMs gehen auf dieselbe Wurzel
    zurück: Das Modell setzt Sprache fort, es führt nichts aus. Wo Ausführung
    nötig ist (zählen, rechnen, jede Zeile bearbeiten), braucht es Werkzeuge
    oder deine Kontrolle.
