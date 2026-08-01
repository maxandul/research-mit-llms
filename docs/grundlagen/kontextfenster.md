# Das Kontextfenster

Einer der häufigsten Stolpersteine: anzunehmen, mehr Material im Chat führe
automatisch zu besseren Antworten. Das Gegenteil ist oft der Fall.

## Was ist das Kontextfenster?

Alles, was ein Modell pro Anfrage *gleichzeitig* sehen kann: deine Frage, der
bisherige Gesprächsverlauf und hochgeladene Inhalte zusammen. Gemessen wird es
in "Tokens" (grob: Wortbausteine, siehe
[Wie ein LLM arbeitet](wie-llms-arbeiten.md)). Ist das Fenster voll, fällt
älterer Inhalt weg oder passt gar nicht erst hinein.

## Voll ist nicht gleich gut

Je näher am Limit, desto eher leidet die Qualität:

- Modelle übersehen Informationen, die *mitten* in einem langen Text stehen,
  eher als solche am Anfang oder Ende, bekannt als "lost in the middle".
- Bei sehr vollem Kontext werden Antworten ungenauer, das Modell vermischt
  Quellen oder verliert den roten Faden.
- Ein grosses Kontextfenster heisst nicht, dass man es füllen *sollte*.
  "Passt rein" ist nicht dasselbe wie "wird gut genutzt".

!!! warnung "Faustregel"
    Gib dem Modell so viel wie nötig und so wenig wie möglich. Relevantes
    Material schlägt viel Material.

## Was das für deine Arbeit heisst

- Nur die relevanten Quellen oder Abschnitte geben, nicht die ganze Sammlung
  auf einmal.
- Die eigentliche Frage und wichtige Anweisungen nicht in der Mitte eines
  langen Textes vergraben, besser an den Anfang oder ans Ende.
- Wird ein langes Gespräch zäh oder ungenau: neu starten und das bisher
  Wichtige in wenigen Sätzen mitgeben.
- Bei viel Material lieber gezielt ein Dokument nach dem anderen bearbeiten,
  oder auf RAG bzw. ein LLM-Wiki ausweichen
  (siehe [Kontext, RAG & LLM-Wiki](rag-vs-wiki.md)).
- Auch beim Schreiben gilt das Prinzip: Kapitel als einzelne Dateien führen
  und dem Modell nur das relevante Kapitel geben, siehe
  [Die Arbeit in Markdown aufbauen](../schreiben/arbeit-in-markdown.md).

### Praxis-Trick: erst detailliert zusammenfassen lassen

Lade ein Paper hoch und bitte zuerst um eine detaillierte
Zusammenfassung, bevor du inhaltlich weiterarbeitest. Das hat zwei
handfeste Effekte. Erstens durchläuft das Modell das ganze Dokument
einmal aktiv und legt das Destillat ans Ende des Gesprächs: genau dort,
wo Folgeantworten am stärksten hinschauen ("lost in the middle" wird
entschärft). Zweitens ist die Zusammenfassung ein Kontrollschritt: Du
siehst sofort, ob die Datei vollständig gelesen wurde oder ob das Tool
im Hintergrund nur Fragmente geholt hat.

!!! randnotiz "Grösse variiert"
    Wie gross das Kontextfenster ist, hängt vom Modell ab und wächst mit
    neuen Generationen. Das Grundprinzip bleibt aber bestehen: je näher am
    Limit, desto grösser das Risiko für Qualitätsverlust.

---

Damit Material überhaupt sauber ins Kontextfenster passt, braucht es das
richtige Format: [Markdown als Arbeitsformat](markdown-arbeitsformat.md).
