# Changelog

Was sich inhaltlich verändert hat, chronologisch. Das Feld bewegt sich
schnell; dieser Changelog macht sichtbar, ob und wo die Seite seit deinem
letzten Besuch dazugelernt hat. Kleinere Korrekturen (Tippfehler, Links)
sind nicht aufgeführt; die vollständige Historie liegt im
[GitHub-Repository](https://github.com/maxandul/research-mit-llms/commits/main).

## Juli 2026

- **Neu erklärt: das Open Knowledge Format (OKF).** Google Cloud hat im
  Juni 2026 eine offene Spezifikation dafür veröffentlicht, wie ein
  LLM-Wiki aufgebaut sein sollte, im Juli gefolgt von Version 0.2 mit
  Feldern für Herkunft, Prüfstand und Verfallsdatum einer Notiz. Was das
  ist, was es bringt und wie neu es noch ist, steht jetzt auf
  [LLM-Wiki (nach Karpathy)](../werkzeuge/sammeln/llm-wiki.md#ein-standard-zeichnet-sich-ab-das-open-knowledge-format);
  die [Wiki-Vorlagen](wiki-vorlagen.md) sind entsprechend ergänzt (der
  Datenblock bleibt dort optional).

- **Der Forschungsstand dieser Website weist seinen Prüfstand jetzt
  maschinenlesbar aus.** Evidenzstufe, Prüfdatum, Prüfumfang und die in
  einer Studie getesteten Modelle standen bisher nur im Text der
  Quellnotizen; sie stehen jetzt zusätzlich in einem Datenblock nach OKF.
  Für dich als Lesende ändert sich der Text nicht, aber zwei Dinge werden
  sichtbar: Notizen, die erst vorläufig sind oder als überholt gelten,
  tragen in der Navigation eine Statusmarke, und der Wissensgraph zeigt die
  Evidenzstufe im Tooltip. Wichtiger ist der unsichtbare Teil: Ob eine
  Notiz nur auf einem Abstract beruht oder eine Policy zur Nachprüfung
  fällig ist, meldet nun ein Prüfskript automatisch, statt dass jemand
  daran denken muss. Aktuell offen ist genau ein Punkt, die
  [Prävalenz-Studie von Liang et al.](../wiki/quellen/liang-2025-llm-praevalenz.md),
  deren publizierte Fassung hinter einer Paywall liegt.

- **Thema [Qualitative Daten codieren](../analysieren/qualitativ-codieren.md)
  auf eine geprüfte Quellenbasis gestellt** (5 Quellen, davon 4
  peer-reviewed). Erste Studien stützen den "zweiter Codierer"-Ansatz der
  Seite: Beim deduktiven Codieren mit Codebuch erreichten aktuelle
  Modelle mit aktiviertem Reasoning in Tests die Zuverlässigkeit
  erfahrener menschlicher Codierer. Die Studienlage ist allerdings jung
  und schnell veraltend; die Seite formuliert die Befunde deshalb als
  Momentaufnahmen. Neu auf der Seite: pro Entscheid eine Begründung
  verlangen, heikle Codes gezielter prüfen als per
  Zufallsstichprobe, exakte Modellversion und Einstellungen im
  Methodenteil dokumentieren, eine ehrliche Einordnung, wann sich der
  Aufwand bei kleinen Interviewstudien nicht lohnt, und eine rote Linie:
  LLMs simulieren keine Interview-Teilnehmenden. Details im
  [Forschungsstand: Qualitative Daten codieren](../wiki/synthese/qualitativ-codieren.md).

- **Neuer Lesegrundsatz im Forschungsstand: Modell und Einsatzart
  bestimmen das Ergebnis.** Ob eine Studie GPT-3.5 im Web-Chat oder ein
  aktuelles Reasoning-Modell per API getestet hat, entscheidet darüber,
  was ihre Zahlen heute bedeuten. Jede Quellnotiz weist Modell, Version
  und Einsatzart deshalb explizit aus; die Begründung steht im neuen
  Konzept [Modell und Einsatzart](../wiki/konzepte/modell-und-einsatzart.md).

- **Lokale Modelle differenzierter eingeordnet.** "Lokal heisst schwächer"
  stimmt so pauschal nicht mehr: Kleine Modelle für den eigenen Rechner
  fallen bei anspruchsvollen Aufgaben ab, grosse selbst gehostete offene
  Modelle erreichen inzwischen Spitzenniveau, brauchen aber
  Infrastruktur. Neu auf [Datenschutz](../grundlagen/datenschutz.md).

- **Grundlagen mit Quellen unterlegt.** Die Rollenteilung und die
  Prüfregel auf [LLMs verstehen](../grundlagen/llms-verstehen.md) sind
  jetzt belegt (u.a. PNAS-Debatte); neue Synthese
  [LLMs verstehen](../wiki/synthese/llms-verstehen.md).

- **Fallbeispiel erweitert: eine Zotero-Bibliothek per MCP an ein LLM
  anbinden.** Der [Forschungsstand](../wiki/index.md) verwaltet seine Quellen
  jetzt zusätzlich in Zotero, angebunden über einen MCP-Server, sodass das
  LLM Referenzen und PDFs zitierfähig ablegt. Wie das eingerichtet wird und
  wie man sauber einpflegt, steht neu auf
  [Zotero](../werkzeuge/sammeln/zotero.md) und im Workflow
  [Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md).

- **MCP verständlich erklärt.** Was hinter dem Model Context Protocol
  steckt, erklären jetzt die Grundlagen
  ([Wie du ein LLM einspannst](../grundlagen/llm-einspannen.md)) und das
  [Glossar](glossar.md). Neu auf
  [Datenschutz & Vertraulichkeit](../grundlagen/datenschutz.md): worauf zu
  achten ist, wenn ein LLM per Anbindung direkt auf eigene Konten zugreift.

- **Neues Themenfeld: LLMs in der Forschung allgemein.** Drei
  Grundsatzquellen eingearbeitet (die PNAS-Debatte von Binz et al. 2025, ein
  Systematic Review zu generativer KI in der Postgraduierten-Forschung von
  Mabirizi et al. 2025, der AI4Science-Survey von Eger et al. 2026) und zwei
  Konzepte ergänzt: Die Verantwortung bleibt bei den Menschen (Konsens über
  alle Positionen hinweg) und LLM-Output muss geprüft werden (in
  ChatGPT-generierten Anträgen waren 38% der DOIs falsch und 16% der
  Referenzen frei erfunden).

- **Thema [KI-Nutzung deklarieren](../haltung/ki-deklarieren.md) auf eine
  breite, geprüfte Quellenbasis gestellt.** Neu belegt: Nichtdeklaration kann
  laut ICMJE als wissenschaftliches Fehlverhalten gelten; Offenlegen kostet
  kurzfristig Vertrauen, aufgedecktes Verschweigen bei Entdeckung rund
  doppelt so viel (Schilke & Reimann 2025); die Grenze zwischen zulässigem
  Copy-Editing und deklarationspflichtiger Inhaltserzeugung ist präzisiert
  (Springer Nature, Elsevier). Von den dokumentierten Academ-AI-Fällen wurden
  nur 4,3% je korrigiert. Neun verifizierte Quellen, Details im
  [Forschungsstand: KI-Nutzung deklarieren](../wiki/synthese/ki-deklarieren.md).

- **Neu: [Forschungsstand-Wiki](../wiki/index.md).** Die Empfehlungen der
  Website werden fortlaufend mit wissenschaftlichen Quellen unterlegt,
  sichtbar als begehbares LLM-Wiki (Quellnotizen, Konzeptnotizen, Synthesen)
  mit automatisch erzeugtem [Wissensgraphen](../wiki/index.md#wissensgraph).
  Es dient zugleich als Fallbeispiel für
  [Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md);
  kopierfertige [Wiki-Vorlagen](wiki-vorlagen.md) stehen bereit.

- **Weitere inhaltliche Ergänzungen:**
  [Transkription via Teams/Google Meet](../erheben/transkription.md) für
  Online-Interviews; Praxis-Trick "erst zusammenfassen lassen" auf
  [Das Kontextfenster](../grundlagen/kontextfenster.md); Empfehlung zu
  bezahlten Abos auf der [Startseite](../index.md); Karpathys
  LLM-Deep-Dive-Video auf [Wie ein LLM arbeitet](../grundlagen/wie-llms-arbeiten.md);
  [Claude Cowork als Steuerzentrale](../workflows/thema-zu-uebersicht.md) als
  Workflow-Variante; durchgehende Überleitungen am Seitenende entlang des
  Forschungsprozesses.

- **Neu: dieser Changelog** und automatisches "Zuletzt aktualisiert"-Datum
  auf jeder Seite.
