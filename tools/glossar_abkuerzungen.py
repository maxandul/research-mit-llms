"""MkDocs-Hook: erzeugt aus dem Glossar die Kurzdefinitionen fuer Tooltips.

Eingebunden in mkdocs.yml unter `hooks:`. Aus jedem Eintrag in
`docs/ressourcen/glossar.md` der Form

    **Begriff**: Erklaerung in einem oder mehreren Saetzen.

entsteht eine Abkuerzungsdefinition

    *[Begriff]: Erster Satz der Erklaerung

Die wird an jede Seite angehaengt. Steht der Begriff irgendwo im Text,
zeigt der Browser die Kurzdefinition beim Zeigen darauf.

Warum als Hook und nicht als gepflegte Datei: Sonst gaebe es zwei Orte
fuer dieselbe Definition, und der zweite laeuft irgendwann dem ersten
davon. Das Glossar bleibt die einzige Quelle.
"""
import re
from pathlib import Path

EINTRAG = re.compile(r"^\*\*(.+?)\*\*:\s*(.+?)(?=\n\n|\n\*\*|\Z)", re.M | re.S)

# Begriffe, die als Tooltip mehr stoeren als helfen: zu kurz, zu haeufig
# im normalen Deutsch, oder Teil laengerer Begriffe.
NICHT_VERLINKEN = {"Kontext / Datei in den Chat laden"}

ABKUERZUNGEN: list = []


# Deutsche Abkuerzungen enden auf einen Punkt, ohne dass der Satz zu
# Ende waere. Ohne diese Liste bricht der Tooltip mitten im Satz ab.
ABKUERZUNGSPUNKT = re.compile(
    r"\b(z\.\s?B|u\.\s?a|d\.\s?h|bzw|ca|vgl|etc|usw|Nr|Abs|S|engl|ggf|bspw)\.$")


def _erster_satz(text: str) -> str:
    text = " ".join(text.split())
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)   # Links entwerten
    text = text.replace("**", "").replace("*", "")
    # Wachsende Praefixe pruefen: das erste Satzende, das nicht zu einer
    # Abkuerzung gehoert, ist das echte.
    for treffer in re.finditer(r"[.!?](?=\s|$)", text):
        satz = text[:treffer.end()]
        if not ABKUERZUNGSPUNKT.search(satz):
            return satz[:180]
    return text[:180]


def on_config(config):
    ABKUERZUNGEN.clear()
    glossar = Path(config["docs_dir"]) / "ressourcen" / "glossar.md"
    if not glossar.exists():
        return config
    text = glossar.read_text(encoding="utf-8")
    for treffer in EINTRAG.finditer(text):
        begriff = treffer.group(1).strip()
        if begriff in NICHT_VERLINKEN or len(begriff) < 3:
            continue
        ABKUERZUNGEN.append(f"*[{begriff}]: {_erster_satz(treffer.group(2))}")
    return config


def on_page_markdown(markdown, page, config, files):
    # Nicht auf dem Glossar selbst: dort stehen die Definitionen im Text,
    # ein Tooltip darueber waere doppelt.
    if not ABKUERZUNGEN or page.file.src_uri == "ressourcen/glossar.md":
        return markdown
    return markdown + "\n\n" + "\n".join(ABKUERZUNGEN) + "\n"
