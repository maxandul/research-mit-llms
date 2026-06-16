# Das Kontextfenster

Einer der haeufigsten Stolpersteine: anzunehmen, mehr Material im Chat fuehre
automatisch zu besseren Antworten. Das Gegenteil ist oft der Fall.

## Was ist das Kontextfenster?

Alles, was ein Modell pro Anfrage *gleichzeitig* sehen kann: deine Frage, der
bisherige Gespraechsverlauf und hochgeladene Inhalte zusammen. Gemessen wird es
in "Tokens" (grob: Wortbausteine). Ist das Fenster voll, faellt aelterer Inhalt
weg oder passt gar nicht erst hinein.

## Voll ist nicht gleich gut

Je naeher am Limit, desto eher leidet die Qualitaet:

- Modelle uebersehen Informationen, die *mitten* in einem langen Text stehen,
  eher als solche am Anfang oder Ende — bekannt als "lost in the middle".
- Bei sehr vollem Kontext werden Antworten ungenauer, das Modell vermischt
  Quellen oder verliert den roten Faden.
- Ein grosses Kontextfenster heisst nicht, dass man es fuellen *sollte*.
  "Passt rein" ist nicht dasselbe wie "wird gut genutzt".

!!! warning "Faustregel"
    Gib dem Modell so viel wie noetig und so wenig wie moeglich. Relevantes
    Material schlaegt viel Material.

## Was das fuer deine Recherche heisst

- Nur die relevanten Quellen oder Abschnitte geben, nicht die ganze Sammlung
  auf einmal.
- Die eigentliche Frage und wichtige Anweisungen nicht in der Mitte eines
  langen Textes vergraben — besser an den Anfang oder ans Ende.
- Wird ein langes Gespraech zaeh oder ungenau: neu starten und das bisher
  Wichtige in wenigen Saetzen mitgeben.
- Bei viel Material lieber gezielt ein Dokument nach dem anderen bearbeiten —
  oder auf RAG bzw. ein LLM-Wiki ausweichen
  (siehe [Kontext, RAG & LLM-Wiki](rag-vs-wiki.md)).

!!! note "Groesse variiert"
    Wie gross das Kontextfenster ist, haengt vom Modell ab und waechst mit
    neuen Generationen. Das Grundprinzip bleibt aber bestehen: je naeher am
    Limit, desto groesser das Risiko fuer Qualitaetsverlust.
