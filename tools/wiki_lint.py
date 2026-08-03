"""Prueft das Forschungsstand-Wiki gegen die Regeln aus CLAUDE.md.

Aufruf aus dem Repository-Wurzelverzeichnis:

    python tools/wiki_lint.py

Geprueft wird, was sich aus dem OKF-Frontmatter maschinell ableiten laesst:
fehlendes oder unvollstaendiges Frontmatter, vorlaeufige Notizen (nur
Abstract geprueft), fehlende Verifikation, abgelaufene Pruefdaten,
ueberholte Notizen, verwaiste Notizen und tote interne Links.

Auf den Inhaltsseiten ausserhalb von `docs/wiki/` kommt dazu: unvollstaendige
`werkzeug:`-Bloecke, unbekannte Hinweisbox-Typen und Abkuerzungen, die weder
im Glossar noch in KUERZEL_AUSNAHMEN stehen.

Inhaltliche Aufgaben aus CLAUDE.md bleiben Handarbeit: Widersprueche
zwischen Konzepten markiert dieses Skript nicht. Die Kuerzel-Pruefung
findet nur Grossbuchstaben-Abkuerzungen; erklaerungsbeduerftige Woerter
wie "Frontmatter" oder "Freemium" muss weiterhin ein Mensch bemerken.

Rueckgabewert: 0 wenn keine Befunde, sonst 1 (fuer CI verwendbar).
"""
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

from mkdocs.utils import meta

LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)")
PFLICHT_QUELLE = ("type", "title", "description", "resource", "evidenzstufe",
                  "verified", "stale_after")
PFLICHT_UEBRIGE = ("type", "title", "description")


def _lesen(pfad: Path):
    rumpf, kopf = meta.get_data(pfad.read_text(encoding="utf-8"))
    return rumpf, kopf or {}


def _trust_stufe(kopf: dict) -> str:
    """Vertrauensstufe nach OKF v0.2, abgeleitet aus `verified`."""
    verified = kopf.get("verified") or []
    if not verified:
        return "unverified"
    if any(str(v.get("by", "")).startswith("human:") for v in verified):
        return "human-reviewed"
    return "machine-confirmed"


def pruefen(wurzel: Path, heute: dt.date | None = None) -> list[str]:
    heute = heute or dt.date.today()
    wiki = (wurzel / "docs" / "wiki").resolve()
    befunde: list[str] = []
    eingehend: dict[str, int] = defaultdict(int)
    notizen: dict[str, dict] = {}

    for pfad in sorted(wiki.rglob("*.md")):
        # index.md und die generierte Schlagwortseite sind Zugaenge zum
        # Wiki, keine Notizen: kein OKF-Frontmatter, keine Verifikation.
        if pfad.name in ("index.md", "schlagworte.md"):
            continue
        rel = pfad.relative_to(wiki).as_posix()
        try:
            rumpf, kopf = _lesen(pfad)
        except Exception as fehler:
            befunde.append(f"{rel}: Frontmatter nicht lesbar ({fehler})")
            continue
        notizen[rel] = kopf

        if not kopf.get("type"):
            befunde.append(f"{rel}: kein Frontmatter mit `type` (nicht OKF-konform)")
            continue

        pflicht = PFLICHT_QUELLE if kopf["type"] == "Quellnotiz" else PFLICHT_UEBRIGE
        fehlend = [feld for feld in pflicht if not kopf.get(feld)]
        if fehlend:
            befunde.append(f"{rel}: Frontmatter unvollstaendig, fehlt: {', '.join(fehlend)}")

        if kopf["type"] == "Quellnotiz":
            stufe = _trust_stufe(kopf)
            if stufe == "unverified":
                befunde.append(f"{rel}: keine Verifikation hinterlegt")
            for eintrag in kopf.get("verified") or []:
                if "abstract" in str(eintrag.get("umfang", "")).lower():
                    befunde.append(
                        f"{rel}: Verifikation stuetzt sich ganz oder teilweise auf "
                        f"ein Abstract ({eintrag['umfang']}), Volltext nachruesten")

        faellig = kopf.get("stale_after")
        if isinstance(faellig, dt.date) and faellig < heute:
            befunde.append(f"{rel}: seit {faellig} faellig zur Nachpruefung")

        if kopf.get("status") == "deprecated":
            befunde.append(f"{rel}: als ueberholt markiert, Verweise pruefen")
        if kopf.get("status") == "draft":
            befunde.append(f"{rel}: als Entwurf markiert")

        for treffer in LINK_RE.finditer(rumpf):
            ziel = (pfad.parent / treffer.group(1)).resolve()
            if not ziel.exists():
                befunde.append(f"{rel}: toter Link auf {treffer.group(1)}")
                continue
            if ziel.name == "index.md":
                continue
            try:
                eingehend[ziel.relative_to(wiki).as_posix()] += 1
            except ValueError:
                pass  # Link auf eine Website-Seite ausserhalb des Wikis

    for rel in notizen:
        if eingehend[rel] == 0:
            befunde.append(f"{rel}: verwaist, kein eingehender Link aus dem Wiki")

    befunde += _pruefen_seiten(wurzel, heute)
    return befunde


# --------------------------------------------------------------------
#  Prueflauf ueber die Inhaltsseiten (ausserhalb von docs/wiki/).
#  Seit Etappe 3 des Facelifts werden Steckbrief und Notizkopf aus dem
#  Frontmatter gerendert (tools/wiki_komponenten.py). Hier wird geprueft,
#  dass niemand versehentlich wieder von Hand danebenschreibt.
# --------------------------------------------------------------------

DUBLETTEN = {
    r'^!!! \w+ "Auf einen Blick"': "Steckbrief von Hand statt im `werkzeug:`-Frontmatter",
    r"^\*\*Evidenzstufe:\*\*": "Evidenzstufe als Fliesstext statt im Frontmatter",
    r"^\*\*Geprüft:\*\*": "Pruefvermerk als Fliesstext statt im Frontmatter",
}

WERKZEUG_PFLICHT = ("schwierigkeit", "kosten", "verarbeitung", "wofuer",
                    "phase", "stand")
STUFEN = ("Einsteiger", "Fortgeschritten", "Profi")

# Kontrollierte Werte. Konkrete Preise stehen bewusst nicht auf den
# Seiten: Sie veralten am schnellsten von allem und muessten dann
# ueberall nachgezogen werden. Die Kategorie reicht zum Aussortieren.
KOSTEN = ("gratis", "Freemium", "kostenpflichtig")
# Wo gerechnet wird. Technische Angabe, keine rechtliche Einschaetzung.
VERARBEITUNG = ("lokal", "Cloud", "beides")
PHASEN = ("finden", "befragen", "verwalten", "transkribieren",
          "analysieren", "schreiben", "lokal", "agentisch")

# Werkzeugangaben veralten schneller als Studien, nicht langsamer.
WERKZEUG_FRIST_MONATE = 12
MONATE = {"januar": 1, "februar": 2, "maerz": 3, "märz": 3, "april": 4,
          "mai": 5, "juni": 6, "juli": 7, "august": 8, "september": 9,
          "oktober": 10, "november": 11, "dezember": 12}

# Zugelassene Hinweisbox-Typen: drei Boxen und die Randnotiz, die keine
# Box ist. Mehr nicht. Alles andere ist entweder ein Tippfehler oder ein
# Rueckfall in die alten Material-Typen (tip, note, info, warning ...).
# Ein neuer Typ braucht einen Eintrag hier, in extra.css und in CLAUDE.md.
BOX_TYPEN = {"merksatz", "warnung", "evidenz", "randnotiz"}
BOX_RE = re.compile(r"^(?:!!!|\?\?\?\+?)\s+([a-zA-Z-]+)", re.M)

# Der Merksatz ist der eine Satz einer Seite. Zwei davon heben sich auf.
MAX_MERKSATZ = 1

# Abkuerzungen, die keinen Glossareintrag brauchen: Eigennamen, gaengige
# Dateiendungen, Platzhalter. Alles andere meldet die Pruefung, damit ein
# neuer Fachbegriff nicht unerklaert stehen bleibt. Wer hier etwas
# eintraegt, behauptet: das versteht die Leserschaft ohne Erklaerung.
KUERZEL_AUSNAHMEN = {
    # Dateiformate und Alltagstechnik
    "PDF", "HTML", "CSS", "XML", "JSON", "TXT", "RTF", "DOC", "DOCX", "XLSX",
    "PPTX", "ZIP", "PNG", "JPG", "SVG", "URL", "HTTP", "HTTPS", "REST",
    "CPU", "GPU", "RAM", "USB", "OCR", "PC",
    # Hochschulen, Verlage, Zeitschriften, Gremien
    "UZH", "ZHAW", "ETH", "PNAS", "JAMA", "BMC", "EPJ", "CHI", "ACM", "IEEE",
    "WAME", "DOAJ", "SJR", "CINAHL", "PRISMA", "USA", "EU",
    # Produkte und Firmen
    "MAXQDA", "ATLAS", "NVIDIA", "CUDA", "VERBI", "SPSS", "MIT", "GPL",
    "CLAUDE", "OKF",
    # Platzhalter in Vorlagen und Beispielen
    "JJJJ", "MM", "TT", "P01", "P02",
}

# Nur Grossbuchstaben-Kuerzel ab drei Zeichen. Kuerzere sind zu oft
# normale Woerter, laengere Wortmarken faengt die Ausnahmeliste.
KUERZEL_RE = re.compile(r"\b[A-ZÄÖÜ][A-ZÄÖÜ0-9]{2,}\b")
# Code, Links und Frontmatter enthalten Kuerzel, die niemand liest.
CODE_RE = re.compile(r"```.*?```|`[^`]*`", re.S)
URL_RE = re.compile(r"https?://\S+|<[^>]+>")


def _glossar_tokens(docs: Path) -> set[str]:
    """Alle Kuerzel, die im Glossar erklaert sind.

    Die Begriffe kommen aus derselben Datei und mit demselben Muster wie
    die Tooltips (`tools/glossar_abkuerzungen.py`), damit Erklaerung und
    Pruefung nicht auseinanderlaufen. Aus "QDA-Software" wird "QDA".
    """
    glossar = docs / "ressourcen" / "glossar.md"
    if not glossar.exists():
        return set()
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from glossar_abkuerzungen import EINTRAG
    tokens: set[str] = set()
    for treffer in EINTRAG.finditer(glossar.read_text(encoding="utf-8")):
        tokens |= set(KUERZEL_RE.findall(treffer.group(1)))
    return tokens


def _kuerzel_pruefen(rel: str, rumpf: str, bekannt: set[str]) -> list[str]:
    """Meldet Abkuerzungen ohne Glossareintrag.

    Der Tooltip entsteht automatisch, sobald ein Begriff im Glossar
    steht. Fehlt er dort, steht das Kuerzel unerklaert auf der Seite,
    und genau das faellt beim Schreiben am wenigsten auf.
    """
    text = URL_RE.sub(" ", CODE_RE.sub(" ", rumpf))
    offen = {k for k in KUERZEL_RE.findall(text)
             if k not in bekannt and k not in KUERZEL_AUSNAHMEN}
    if not offen:
        return []
    return [f"{rel}: Kuerzel ohne Glossareintrag: {', '.join(sorted(offen))} "
            f"(erklaeren in docs/ressourcen/glossar.md oder, wenn "
            f"selbsterklaerend, in KUERZEL_AUSNAHMEN aufnehmen)"]


def _stand_pruefen(rel: str, stand, heute: dt.date) -> list[str]:
    """Meldet Werkzeugangaben, die aelter als WERKZEUG_FRIST_MONATE sind.

    `stand` steht als "August 2026" in der Datei, damit es lesbar bleibt;
    hier wird daraus ein Datum."""
    if not stand:
        return []  # fehlend meldet schon die Pflichtfeldpruefung
    treffer = re.match(r"([A-Za-zÄÖÜäöü]+)\s+(\d{4})", str(stand).strip())
    if not treffer:
        return [f"{rel}: `werkzeug.stand` nicht lesbar ('{stand}'), "
                f"erwartet wird etwa 'August 2026'"]
    monat = MONATE.get(treffer.group(1).lower())
    if not monat:
        return [f"{rel}: `werkzeug.stand` nennt keinen deutschen Monat "
                f"('{treffer.group(1)}')"]
    geprueft = dt.date(int(treffer.group(2)), monat, 1)
    alter = (heute.year - geprueft.year) * 12 + (heute.month - geprueft.month)
    if alter > WERKZEUG_FRIST_MONATE:
        return [f"{rel}: Werkzeugangaben seit {stand} nicht geprueft "
                f"({alter} Monate), Kosten und Funktionsumfang nachziehen"]
    return []


def _pruefen_seiten(wurzel: Path, heute: dt.date) -> list[str]:
    docs = (wurzel / "docs").resolve()
    wiki = (docs / "wiki").resolve()
    befunde: list[str] = []
    # Nur die Inhaltsseiten: Wiki-Notizen richten sich an Leser, die den
    # Forschungsstand vertiefen, und tragen Fachkuerzel aus den Quellen.
    glossar_tokens = _glossar_tokens(docs)

    for pfad in sorted(docs.rglob("*.md")):
        if wiki in pfad.parents or pfad == wiki:
            continue
        rel = pfad.relative_to(docs).as_posix()
        try:
            rumpf, kopf = _lesen(pfad)
        except Exception as fehler:
            befunde.append(f"{rel}: Frontmatter nicht lesbar ({fehler})")
            continue

        # docs/index.md zeigt die Bausteine absichtlich als Beispiel.
        if rel != "index.md":
            for muster, hinweis in DUBLETTEN.items():
                if re.search(muster, rumpf, re.M):
                    befunde.append(f"{rel}: {hinweis}")

        werkzeug = kopf.get("werkzeug")
        if isinstance(werkzeug, dict):
            fehlend = [f for f in WERKZEUG_PFLICHT if not werkzeug.get(f)]
            if fehlend:
                befunde.append(f"{rel}: `werkzeug:` unvollstaendig, fehlt: "
                               f"{', '.join(fehlend)}")

            stufe = werkzeug.get("schwierigkeit")
            if stufe and stufe not in STUFEN:
                befunde.append(f"{rel}: Schwierigkeit '{stufe}' ist keine der "
                               f"drei Stufen ({', '.join(STUFEN)}); Spannen und "
                               f"Vorbehalte gehoeren in `schwierigkeit_zusatz`")

            kosten = werkzeug.get("kosten")
            if kosten and kosten not in KOSTEN:
                befunde.append(f"{rel}: Kosten '{kosten}' ist kein zugelassener "
                               f"Wert ({', '.join(KOSTEN)}); Details gehoeren "
                               f"in `kosten_zusatz`")

            verarbeitung = werkzeug.get("verarbeitung")
            if verarbeitung and verarbeitung not in VERARBEITUNG:
                befunde.append(f"{rel}: Verarbeitung '{verarbeitung}' ist kein "
                               f"zugelassener Wert ({', '.join(VERARBEITUNG)})")

            phasen = werkzeug.get("phase") or []
            if isinstance(phasen, str):
                befunde.append(f"{rel}: `phase` muss eine Liste sein, auch bei "
                               f"nur einem Wert")
                phasen = [phasen]
            for phase in phasen:
                if phase not in PHASEN:
                    befunde.append(f"{rel}: unbekannte Phase '{phase}', "
                                   f"zugelassen sind {', '.join(PHASEN)}")

            befunde += _stand_pruefen(rel, werkzeug.get("stand"), heute)

        typen = [t.group(1) for t in BOX_RE.finditer(rumpf)]
        for typ in sorted(set(typen)):
            if typ not in BOX_TYPEN:
                befunde.append(f"{rel}: unbekannter Hinweisbox-Typ '{typ}', "
                               f"zugelassen sind {', '.join(sorted(BOX_TYPEN))}")
        if typen.count("merksatz") > MAX_MERKSATZ:
            befunde.append(f"{rel}: {typen.count('merksatz')} Merksaetze, "
                           f"hoechstens {MAX_MERKSATZ} pro Seite")

        if rel != "ressourcen/glossar.md":
            befunde += _kuerzel_pruefen(rel, rumpf, glossar_tokens)

    return befunde


def main() -> int:
    wurzel = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    befunde = pruefen(wurzel)
    if not befunde:
        print("wiki_lint: keine Befunde.")
        return 0
    print(f"wiki_lint: {len(befunde)} Befunde\n")
    for zeile in befunde:
        print(f"  - {zeile}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
