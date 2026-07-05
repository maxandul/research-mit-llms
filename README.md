# Forschen mit LLMs

**Zur Webseite: <https://maxandul.github.io/research-mit-llms/>**

Ein niederschwelliger Wegweiser, wie grosse Sprachmodelle (LLMs) alle
Schritte des Forschungsprozesses unterstützen können. Für Forschende und
Studierende, ohne Programmierkenntnisse als Voraussetzung.

## Was die Seite abdeckt

- **Grundlagen**: wie LLMs arbeiten, wo ihre Grenzen liegen, Datenschutz,
  Markdown als Arbeitsformat
- **Literatur**: Werkzeuge zum Finden, Befragen und Sammeln von Literatur,
  verkettet zu durchgängigen Workflows
- **Daten erheben & schützen**: Interviews lokal transkribieren (auch
  Schweizerdeutsch), Daten anonymisieren für die Arbeit mit Cloud-Diensten
- **Daten analysieren**: qualitative Daten codieren, quantitativ auswerten
- **Schreiben & Publizieren**: die Arbeit in Markdown aufbauen, Word als
  Export, Umgang mit Feedback
- **Haltung & gute Praxis**: KI-Nutzung deklarieren
- **Ressourcen**: Glossar, Linksammlung, kopierfertige Prompt-Bibliothek

## Feedback & Fragen

- Frage stellen: [Q&A-Diskussionen](https://github.com/maxandul/research-mit-llms/discussions/categories/q-a)
- Fehler oder Vorschlag: [Issue eröffnen](https://github.com/maxandul/research-mit-llms/issues)

## Technisches

Die Seite ist mit [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
gebaut. Alle Inhalte liegen als Markdown unter `docs/`. Eine Seite ändern
heisst die `.md`-Datei bearbeiten; eine Seite hinzufügen heisst neue
`.md`-Datei anlegen und in `mkdocs.yml` unter `nav:` eintragen.

### Lokal ansehen

Voraussetzung: Python 3.

```bash
pip install -r requirements.txt
mkdocs serve
```

Dann im Browser <http://127.0.0.1:8000> öffnen. Änderungen werden live
angezeigt.

### Veröffentlichung

Bei jedem Push auf `main` baut die GitHub Action unter
`.github/workflows/deploy.yml` die Seite automatisch und veröffentlicht sie
auf GitHub Pages.

## Lizenz

Die Inhalte stehen unter der Lizenz
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de): Sie
dürfen geteilt und bearbeitet werden, auch kommerziell, solange
[maxandul](https://github.com/maxandul) als Quelle genannt wird. Details
in der Datei [LICENSE](LICENSE).
