# Das Kontextfenster

Einer der häufigsten Stolpersteine: anzunehmen, mehr Material im Chat führe
automatisch zu besseren Antworten. Das Gegenteil ist oft der Fall.

## Was ist das Kontextfenster?

Alles, was ein Modell pro Anfrage *gleichzeitig* sehen kann: deine Frage, der
bisherige Gesprächsverlauf und hochgeladene Inhalte zusammen. Gemessen wird es
in "Tokens" (grob: Wortbausteine). Ist das Fenster voll, fällt älterer Inhalt
weg oder passt gar nicht erst hinein.

## Voll ist nicht gleich gut

Je näher am Limit, desto eher leidet die Qualität:

- Modelle übersehen Informationen, die *mitten* in einem langen Text stehen,
  eher als solche am Anfang oder Ende — bekannt als "lost in the middle".
- Bei sehr vollem Kontext werden Antworten ungenaür, das Modell vermischt
  Quellen oder verliert den roten Faden.
- Ein grosses Kontextfenster heisst nicht, dass man es füllen *sollte*.
  "Passt rein" ist nicht dasselbe wie "wird gut genutzt".

!!! warning "Faustregel"
    Gib dem Modell so viel wie nötig und so wenig wie möglich. Relevantes
    Material schlägt viel Material.

## Was das für deine Recherche heisst

- Nur die relevanten Quellen oder Abschnitte geben, nicht die ganze Sammlung
  auf einmal.
- Die eigentliche Frage und wichtige Anweisungen nicht in der Mitte eines
  langen Textes vergraben — besser an den Anfang oder ans Ende.
- Wird ein langes Gespräch zäh oder ungenau: neu starten und das bisher
  Wichtige in wenigen Sätzen mitgeben.
- Bei viel Material lieber gezielt ein Dokument nach dem anderen bearbeiten —
  oder auf RAG bzw. ein LLM-Wiki ausweichen
  (siehe [Kontext, RAG & LLM-Wiki](rag-vs-wiki.md)).

!!! note "Grösse variiert"
    Wie gross das Kontextfenster ist, hängt vom Modell ab und wächst mit
    neuen Generationen. Das Grundprinzip bleibt aber bestehen: je näher am
    Limit, desto grösser das Risiko für Qualitätsverlust.
