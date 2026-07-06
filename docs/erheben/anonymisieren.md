# Daten anonymisieren

!!! info "Auf einen Blick"
    **Schwierigkeit:** Einsteiger · **Kosten:** gratis ·
    **Wofür:** sensible Daten so aufbereiten, dass sie in Cloud-Diensten bearbeitet werden können

Die [Datenschutz-Grundregel](../grundlagen/datenschutz.md) sagt: nichts
hochladen, was du nicht auch einer fremden Firma mailen würdest. Interviews,
Fallnotizen und Befragungsdaten fallen fast immer darunter. Die Lösung ist
nicht Verzicht, sondern ein sauberer Anonymisierungsschritt **vor** dem
ersten Upload.

## Anonymisieren oder pseudonymisieren?

- **Pseudonymisieren:** Identifikatoren werden durch Platzhalter ersetzt
  (Frau Müller wird P01). Es existiert eine Zuordnungstabelle, mit der sich
  das rückgängig machen lässt. Solange dieser Schlüssel existiert, gelten
  die Daten rechtlich weiterhin als Personendaten.
- **Anonymisieren:** Der Bezug ist auch mit Zusatzwissen nicht mehr
  herstellbar. Das ist der strengere Massstab und in der Praxis schwer
  vollständig zu erreichen.

Für die Arbeit mit Cloud-LLMs ist die Pseudonymisierung mit lokal
verwahrtem Schlüssel der praktikable Standard: Sie senkt das Risiko
drastisch, und du kannst die Ergebnisse später wieder zuordnen. Sie
entbindet aber nicht von den institutionellen Vorgaben, siehe unten.

## Der Workflow

### 1. Zuordnungstabelle anlegen (bleibt lokal!)

Eine simple zweispaltige Tabelle in Excel: Original und Ersatz.

| Original | Ersatz |
|----------|--------|
| Anna Müller | P01 |
| Kantonsspital X-Stadt | Spital A |
| Rorschach | Stadt B |
| 14. März 2025 | Frühjahr 2025 |

Konsistent bleiben: dieselbe Person ist in allen Dokumenten P01. Nur so
bleiben die Daten auswertbar und die Ergebnisse rückübersetzbar.

!!! danger "Die Tabelle ist der Schlüssel"
    Die Zuordnungstabelle wird **nie** hochgeladen, in keinen Chat, keinen
    Cloud-Speicher, keine E-Mail. Sie liegt getrennt von den Daten, idealerweise
    verschlüsselt oder auf einem anderen Laufwerk.

### 2. Manuell suchen und ersetzen

Der Standardweg ist bewusst unspektakulär: **Suchen & Ersetzen** direkt in
Excel oder Word, Eintrag für Eintrag aus deiner Tabelle. Kein Tool, kein
Skript, volle Kontrolle. Mit "Alle ersetzen" plus Trefferanzahl siehst du
genau, was passiert ist.

### 3. Einmal komplett gegenlesen

Suchen & Ersetzen findet nur, was exakt so geschrieben ist. Es verpasst:

- **Schreibvarianten und Tippfehler:** "Müler", "Frau M.", Spitznamen.
- **Indirekte Identifikatoren:** "die einzige Bäckerin im Dorf", "der
  Abteilungsleiter, der letztes Jahr angefangen hat". Kombinationen aus
  Beruf, Ort und Alter reichen oft zur Re-Identifikation.
- **Kontextwissen:** Ereignisse, die nur eine Person erlebt haben kann.

Darum einmal vollständig durchlesen und heikle Stellen von Hand
umformulieren oder vergröbern (aus "42-jährige Primarlehrerin in Wattwil"
wird "Lehrerin mittleren Alters in einer ländlichen Gemeinde").

### 4. Metadaten prüfen

Dateien tragen unsichtbare Angaben: Autorname in Word-Eigenschaften,
Kommentare, nachverfolgte Änderungen. Am sichersten: den bereinigten Text
in eine **neue, leere Datei** kopieren und nur diese verwenden.

### 5. Erst jetzt hochladen

Ab hier kannst du mit dem pseudonymisierten Material in Cloud-Diensten
arbeiten, etwa [qualitativ codieren](../analysieren/qualitativ-codieren.md).
Die Ergebnisse übersetzt du am Schluss lokal mit deiner Tabelle zurück.

## Eskalation bei grossen Datenmengen

Bei dutzenden Transkripten wird Handarbeit unrealistisch. Dann:

- **Skript statt Handarbeit:** Ein kleines Such-Ersetz-Skript (das dir ein
  LLM schreiben kann) wendet die Zuordnungstabelle auf alle Dateien an.
  Läuft lokal, die Tabelle bleibt bei dir.
- **Lokales LLM als zusätzlicher Prüfer:** Ein Modell via Ollama oder
  LM Studio (siehe [Datenschutz](../grundlagen/datenschutz.md)) kann lokal
  nach übersehenen Personenbezügen suchen. Es ersetzt das Gegenlesen nicht,
  ist aber ein gutes zweites Augenpaar, ohne dass Daten den Rechner verlassen.

## Grenzen & Einordnung

- Pseudonymisierte Daten mit existierendem Schlüssel sind rechtlich weiter
  Personendaten. Der Workflow minimiert Risiken, ersetzt aber nicht die
  Freigabe durch Ethikkommission, Datenschutzstelle oder die Vorgaben
  deiner Hochschule.
- Prüfe die Einwilligungserklärungen deiner Teilnehmenden: Deckt sie die
  Verarbeitung mit (Cloud-)Software ab?
- Im Zweifel gilt weiter die Grundregel: weglassen oder lokal arbeiten.

---

Mit sauber pseudonymisierten Daten steht die Auswertung offen:
[Qualitative Daten codieren](../analysieren/qualitativ-codieren.md).
