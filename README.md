# Research mit LLMs — GitHub Page

Niederschwelliger Wegweiser fuer wissenschaftliches Arbeiten mit
LLM-Werkzeugen. Gebaut mit [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Inhalte bearbeiten

Alle Inhalte liegen als Markdown unter `docs/`. Eine Seite aendern = die
`.md`-Datei bearbeiten. Eine Seite hinzufuegen = neue `.md`-Datei anlegen und
in `mkdocs.yml` unter `nav:` eintragen.

## Lokal ansehen (optional)

Voraussetzung: Python 3.

```bash
pip install -r requirements.txt
mkdocs serve
```

Dann im Browser <http://127.0.0.1:8000> oeffnen. Aenderungen werden live
angezeigt.

## Veroeffentlichen auf GitHub Pages

1. Dieses Verzeichnis als GitHub-Repository hochladen (Branch `main`).
2. Beim ersten Push baut die Action unter `.github/workflows/deploy.yml` die
   Seite automatisch und legt sie auf dem Branch `gh-pages` ab.
3. In den Repo-Einstellungen unter **Settings -> Pages** als Quelle den
   Branch `gh-pages` waehlen.
4. Nach kurzer Zeit ist die Seite unter
   `https://DEIN-NUTZERNAME.github.io/DEIN-REPO/` erreichbar.
5. Diese URL in `mkdocs.yml` bei `site_url` eintragen.

## Vor dem Live-Gang ausfuellen

- `site_author` und `site_url` in `mkdocs.yml`
- Name, Datum und Feedback-Link in `docs/ueber.md`
- alle Boxen `!!! note "Noch zu ergaenzen"` pruefen/fuellen
- Kosten-/Limit-Angaben bei Elicit, NotebookLM und Connected Papers verifizieren
