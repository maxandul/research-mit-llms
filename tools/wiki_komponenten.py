"""MkDocs-Hook: rendert wiederkehrende Seitenkoepfe aus dem Frontmatter.

Eingebunden in mkdocs.yml unter `hooks:`. Zwei Komponenten:

1. **Notizkopf** auf jeder Quellnotiz (`type: Quellnotiz`): Evidenzstufe,
   Pruefvermerk, Ampel aus `stale_after`, Angaben aus `studie`.
2. **Werkzeug-Steckbrief** auf jeder Seite mit einem `werkzeug:`-Block:
   Schwierigkeit, Kosten, Wofuer, Stand.

Warum als Hook und nicht von Hand geschrieben: Beide Bloecke standen
vorher als Fliesstext in den Seiten und mussten parallel zum Frontmatter
gepflegt werden. Jetzt ist das Frontmatter die einzige Quelle. Wer eine
Angabe aendert, aendert sie an einer Stelle, und die Darstellung ist auf
allen Seiten gleich.

Die Ampel wird bei jedem Build neu gegen das aktuelle Datum gerechnet:
Eine Notiz kann also faellig werden, ohne dass jemand die Datei anfasst.
"""
import datetime as dt
import html
import posixpath
import re
import sys
from pathlib import Path

from mkdocs.utils import meta

# Wie lange vor `stale_after` die Ampel von gruen auf gelb springt.
VORWARNUNG_TAGE = 90

EVIDENZ_SCHLUESSEL = {
    "peer-reviewed": "peer",
    "preprint": "preprint",
    "policy": "policy",
    "doku": "doku",
    "praxis": "praxis",
}

SCHWIERIGKEIT_STUFEN = ["Einsteiger", "Fortgeschritten", "Profi"]

# Die Phasen des Forschungsprozesses, in der Reihenfolge, in der sie
# vorkommen. Ein Werkzeug kann zu mehreren gehoeren; Zotero etwa
# verwaltet Literatur und liefert die Bibliografie beim Schreiben.
PHASEN = {
    "finden":         "Literatur finden",
    "befragen":       "Literatur befragen",
    "verwalten":      "Sammeln und verwalten",
    "transkribieren": "Transkribieren",
    "analysieren":    "Daten analysieren",
    "schreiben":      "Schreiben und exportieren",
    "lokal":          "Lokal betreiben",
    "agentisch":      "Agentisch arbeiten",
}

# Wird in on_files gefuellt: alles, was einen `werkzeug:`-Block hat.
WERKZEUGE: list = []

# Nachbarschaft im Wiki, ebenfalls in on_files gefuellt.
# NACHBARN[quelle] = {"raus": [...], "rein": [...]}, je mit Angaben zum Ziel.
NACHBARN: dict = {}
WIKI_NOTIZEN: dict = {}
WIKI_LINK = re.compile(r"\]\(([^)#\s]+\.md)")

SCHICHTEN = {
    "wiki/quellen/":  "Quellnotiz",
    "wiki/konzepte/": "Konzept",
    "wiki/synthese/": "Synthese",
}

# Platzhalter im Markdown, etwa {{ werkzeuge:transkribieren }} oder
# {{ werkzeuge:alle }}. Bewusst sichtbar gewaehlt: Wenn der Hook
# ausfaellt, steht der Platzhalter im Text statt spurlos zu fehlen.
PLATZHALTER = re.compile(r"^\{\{\s*werkzeuge:([a-z]+)\s*\}\}\s*$", re.M)


def _e(wert) -> str:
    """Text fuer die HTML-Ausgabe absichern."""
    return html.escape(str(wert), quote=False)


def _inline(wert) -> str:
    """Wie _e, uebersetzt aber `code` in <code>. Der Block wird als rohes
    HTML eingesetzt (markdown="0"), Markdown greift darin also nicht."""
    text = _e(wert)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def _datum(wert):
    """Nimmt date, datetime oder ISO-String und gibt ein date zurueck."""
    if isinstance(wert, dt.datetime):
        return wert.date()
    if isinstance(wert, dt.date):
        return wert
    try:
        return dt.date.fromisoformat(str(wert)[:10])
    except ValueError:
        return None


def _de(datum) -> str:
    d = _datum(datum)
    return d.strftime("%d.%m.%Y") if d else _e(datum)


def _chip(text: str, art: str = "neutral", titel: str = "") -> str:
    attr = f' title="{_e(titel)}"' if titel else ""
    return f'<span class="fl-chip fl-chip--{art}"{attr}>{_e(text)}</span>'


def _evidenz_chip(kopf: dict) -> str:
    stufe = kopf.get("evidenzstufe")
    if not stufe:
        return ""
    art = EVIDENZ_SCHLUESSEL.get(str(stufe).strip().lower(), "neutral")
    zusatz = kopf.get("evidenzstufe_zusatz")
    text = f"{stufe} ({zusatz})" if zusatz else str(stufe)
    return f'<span class="fl-chip fl-chip--{art}">{_e(text)}</span>'


def _status_chip(kopf: dict) -> str:
    status = kopf.get("status")
    if status == "draft":
        return _chip("Vorläufig", "warnung", "Nur das Abstract wurde geprüft")
    if status == "deprecated":
        return _chip("Überholt", "gefahr", "Wird nicht mehr gepflegt")
    return ""


def _pruef_chips(kopf: dict) -> list:
    """Ein Chip pro Verifikation, plus die Ampel aus stale_after."""
    chips = []
    for eintrag in kopf.get("verified") or []:
        if not isinstance(eintrag, dict):
            continue
        wer = str(eintrag.get("by", "")).replace("human:", "").strip()
        umfang = str(eintrag.get("umfang", "")).strip()
        wann = _de(eintrag.get("at")) if eintrag.get("at") else ""
        nur_abstract = "abstract" in umfang.lower()
        # "Volltext" allein sagt nicht, dass geprueft wurde.
        text = f"{umfang} geprüft" if umfang and "geprüft" not in umfang.lower() \
            else (umfang or "geprüft")
        titel = " ".join(t for t in [f"geprüft am {wann}" if wann else "",
                                     f"von {wer}" if wer else ""] if t)
        chips.append(_chip(text, "warnung" if nur_abstract else "geprueft", titel))
    return chips


def _ampel_chip(kopf: dict, heute: dt.date) -> str:
    frist = _datum(kopf.get("stale_after"))
    if not frist:
        return ""
    rest = (frist - heute).days
    if rest < 0:
        return _chip(f"Nachprüfung fällig seit {_de(frist)}", "gefahr",
                     "Das Datum aus stale_after liegt in der Vergangenheit")
    art = "warnung" if rest <= VORWARNUNG_TAGE else "neutral"
    return _chip(f"Nachprüfen bis {_de(frist)}", art)


def _studie_zeilen(kopf: dict) -> list:
    """Der studie-Block, beschriftet. Reihenfolge ist bewusst fix."""
    studie = kopf.get("studie")
    if not isinstance(studie, dict):
        return []
    beschriftung = {
        "modelle": "Modelle",
        "einsatzart": "Einsatzart",
        "durchgefuehrt": "Durchgeführt",
        "sprache": "Sprache",
        "daten": "Daten",
    }
    zeilen = []
    for schluessel, label in beschriftung.items():
        wert = studie.get(schluessel)
        if not wert:
            continue
        if isinstance(wert, (list, tuple)):
            wert = ", ".join(str(w) for w in wert)
        zeilen.append((label, str(wert).strip()))
    # Unbekannte Zusatzfelder nicht verschlucken
    for schluessel, wert in studie.items():
        if schluessel not in beschriftung and wert:
            zeilen.append((schluessel.capitalize(), str(wert).strip()))
    return zeilen


def _notizkopf(kopf: dict, heute: dt.date) -> str:
    chips = [c for c in [_evidenz_chip(kopf), _status_chip(kopf)] if c]
    chips += _pruef_chips(kopf)
    ampel = _ampel_chip(kopf, heute)
    if ampel:
        chips.append(ampel)

    teile = ['<div class="fl-notizkopf" markdown="0">']
    if chips:
        teile.append('<div class="fl-chips">' + "".join(chips) + "</div>")

    notiz = kopf.get("pruefnotiz")
    if notiz:
        teile.append(f'<p class="fl-notizkopf__notiz">{_inline(str(notiz).strip())}</p>')

    zeilen = _studie_zeilen(kopf)
    if zeilen:
        teile.append('<dl class="fl-studie">')
        for label, wert in zeilen:
            teile.append(f"<dt>{_e(label)}</dt><dd>{_inline(wert)}</dd>")
        teile.append("</dl>")

    teile.append('<p class="fl-herkunft">Dieser Kopf wird beim Bauen der '
                 "Website aus dem Datenblock der Notiz erzeugt, nicht von "
                 "Hand geschrieben.</p>")
    teile.append("</div>")
    return "\n".join(teile)


_GLOSSAR: dict = {}


def _glossar(config) -> dict:
    """Begriff -> Kurzdefinition, aus dem Glossar.

    Der Steckbrief ist fertiges HTML, und die Tooltip-Erweiterung fasst
    HTML-Bloecke nicht an. "Freemium" stuende dort also unerklaert,
    ausgerechnet an der Stelle, an der ein Leser dem Wort zuerst
    begegnet. Darum hier derselbe Griff ins Glossar wie beim Fliesstext:
    gelesen wird dieselbe Datei mit demselben Muster, damit es nur eine
    Quelle fuer die Definition gibt.
    """
    if _GLOSSAR:
        return _GLOSSAR
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from glossar_abkuerzungen import EINTRAG, _erster_satz
    pfad = Path(config["docs_dir"]) / "ressourcen" / "glossar.md"
    if not pfad.exists():
        return _GLOSSAR
    for treffer in EINTRAG.finditer(pfad.read_text(encoding="utf-8")):
        _GLOSSAR[treffer.group(1).strip()] = _erster_satz(treffer.group(2))
    return _GLOSSAR


def _wert_mit_tooltip(wert: str, glossar: dict) -> str:
    erklaerung = glossar.get(wert)
    if not erklaerung:
        return _e(wert)
    return f'<abbr title="{html.escape(erklaerung)}">{_e(wert)}</abbr>'


def _steckbrief(werkzeug: dict, glossar: dict | None = None) -> str:
    if not isinstance(werkzeug, dict):
        return ""
    glossar = glossar or {}
    teile = ['<div class="fl-steckbrief" markdown="0">']

    stufe = str(werkzeug.get("schwierigkeit", "")).strip()
    if stufe:
        try:
            punkte = SCHWIERIGKEIT_STUFEN.index(stufe) + 1
        except ValueError:
            punkte = 0
        # Punkte zusaetzlich zur Farbe, damit die Stufe nicht allein an
        # der Farbe haengt.
        marke = "●" * punkte + "○" * (len(SCHWIERIGKEIT_STUFEN) - punkte)
        zusatz = werkzeug.get("schwierigkeit_zusatz")
        teile.append(
            '<div class="fl-steckbrief__feld">'
            "<dt>Schwierigkeit</dt>"
            f'<dd><span class="fl-stufe" aria-hidden="true">{marke}</span> {_e(stufe)}'
            + (f'<span class="fl-zusatz">{_e(zusatz)}</span>' if zusatz else "")
            + "</dd></div>"
        )

    for schluessel, label in (("kosten", "Kosten"),
                              ("verarbeitung", "Verarbeitung"),
                              ("wofuer", "Wofür")):
        wert = werkzeug.get(schluessel)
        if not wert:
            continue
        zusatz = werkzeug.get(f"{schluessel}_zusatz")
        teile.append(
            '<div class="fl-steckbrief__feld">'
            f"<dt>{label}</dt><dd>"
            f"{_wert_mit_tooltip(str(wert).strip(), glossar)}"
            + (f'<span class="fl-zusatz">{_e(zusatz)}</span>' if zusatz else "")
            + "</dd></div>"
        )

    teile.append("</div>")

    stand = werkzeug.get("stand")
    if stand:
        teile.append(
            f'<p class="fl-stand">Angaben zu Kosten und Funktionsumfang: '
            f"Stand {_e(stand)}. Verbindlich sind die offiziellen Seiten "
            f"des Anbieters.</p>"
        )
    return "\n".join(teile)


def _einfuegen(markdown: str, block: str) -> str:
    """Setzt den Block direkt hinter die erste Ueberschrift der Seite."""
    treffer = re.search(r"^#\s+.*$", markdown, re.M)
    if not treffer:
        return block + "\n\n" + markdown
    schnitt = treffer.end()
    return markdown[:schnitt] + "\n\n" + block + "\n" + markdown[schnitt:]


# Notizen, die bewusst nicht in der Navigation stehen. Bei aktuell 34 und
# absehbar ueber 80 Notizen waere eine flache Nav-Liste keine Navigation
# mehr; sie sind ueber die thematisch gruppierten Indexseiten, die Suche,
# den Wissensgraphen und die Querverweise erreichbar. Ohne Nav-Eintraege
# bliebe die Seitenleiste dort aber leer, deshalb wird sie ausgeblendet.
OHNE_SEITENLEISTE = {"Quellnotiz", "Konzeptnotiz"}


def on_files(files, config):
    """Registry aller Werkzeuge aufbauen, bevor Seiten gerendert werden.

    Damit kann jede Themenseite die zu ihr passenden Werkzeuge anzeigen,
    ohne dass sie irgendwo doppelt gepflegt werden."""
    WERKZEUGE.clear()
    for datei in files.documentation_pages():
        try:
            text = Path(datei.abs_src_path).read_text(encoding="utf-8")
            rumpf, kopf = meta.get_data(text)
        except Exception:
            continue
        werkzeug = (kopf or {}).get("werkzeug")
        if not isinstance(werkzeug, dict):
            continue
        titel = kopf.get("title")
        if not titel:
            treffer = re.search(r"^#\s+(.+)$", rumpf, re.M)
            titel = treffer.group(1).strip() if treffer else datei.src_uri
        WERKZEUGE.append({
            "titel": titel,
            "quelle": datei.src_uri,
            "werkzeug": werkzeug,
        })
    WERKZEUGE.sort(key=lambda w: w["titel"].lower())
    _nachbarschaft_aufbauen(files)
    return files


def _schicht(quelle: str) -> str:
    for praefix, name in SCHICHTEN.items():
        if quelle.startswith(praefix):
            return name
    return ""


def _nachbarschaft_aufbauen(files):
    """Wer verweist auf wen im Wiki.

    Quell- und Konzeptnotizen stehen bewusst nicht in der Navigation
    (siehe OHNE_SEITENLEISTE). Damit man von einer Notiz trotzdem
    weiterkommt, bekommt jede am Ende die Notizen, mit denen sie
    verbunden ist. Die Beziehungen stammen aus denselben Markdown-Links,
    aus denen tools/wiki_graph.py den Wissensgraphen baut."""
    NACHBARN.clear()
    WIKI_NOTIZEN.clear()
    rumpfe = {}

    for datei in files.documentation_pages():
        quelle = datei.src_uri
        if not quelle.startswith("wiki/") or quelle.endswith("index.md"):
            continue
        try:
            text = Path(datei.abs_src_path).read_text(encoding="utf-8")
            rumpf, kopf = meta.get_data(text)
        except Exception:
            continue
        kopf = kopf or {}
        titel = kopf.get("title")
        if not titel:
            treffer = re.search(r"^#\s+(.+)$", rumpf, re.M)
            titel = treffer.group(1).strip() if treffer else quelle
        WIKI_NOTIZEN[quelle] = {
            "titel": str(titel),
            "schicht": _schicht(quelle),
            "evidenzstufe": kopf.get("evidenzstufe"),
        }
        rumpfe[quelle] = rumpf

    for quelle, rumpf in rumpfe.items():
        for treffer in WIKI_LINK.finditer(rumpf):
            ziel = posixpath.normpath(
                posixpath.join(posixpath.dirname(quelle), treffer.group(1)))
            if ziel not in WIKI_NOTIZEN or ziel == quelle:
                continue
            NACHBARN.setdefault(quelle, {"raus": set(), "rein": set()})
            NACHBARN.setdefault(ziel, {"raus": set(), "rein": set()})
            NACHBARN[quelle]["raus"].add(ziel)
            NACHBARN[ziel]["rein"].add(quelle)


def _nachbarn_block(quelle: str) -> str:
    """Liste der verbundenen Notizen, als Markdown ans Seitenende."""
    eintrag = NACHBARN.get(quelle)
    if not eintrag:
        return ""
    verbunden = sorted(eintrag["raus"] | eintrag["rein"],
                       key=lambda z: (WIKI_NOTIZEN[z]["schicht"],
                                      WIKI_NOTIZEN[z]["titel"].lower()))
    if not verbunden:
        return ""

    zeilen = ['<div class="fl-nachbarn" markdown>', "",
              "**Verbunden mit**", ""]
    for ziel in verbunden:
        notiz = WIKI_NOTIZEN[ziel]
        pfad = _relativ(quelle, ziel)
        marke = notiz["schicht"]
        if notiz["evidenzstufe"]:
            marke += f", {notiz['evidenzstufe']}"
        # Die Richtung nur nennen, wenn sie einseitig ist. Beidseitige
        # Verlinkung ist der Normalfall und muesste sonst ueberall
        # dastehen, ohne etwas zu unterscheiden.
        raus, rein = ziel in eintrag["raus"], ziel in eintrag["rein"]
        if raus and not rein:
            marke += " · von hier verlinkt"
        elif rein and not raus:
            marke += " · verweist hierher"
        zeilen.append(f'- [{notiz["titel"]}]({pfad})  \n'
                      f'  <span class="fl-kurzangabe">{_e(marke)}</span>')
    zeilen += ["", "</div>"]
    return "\n".join(zeilen)


def _relativ(von: str, nach: str) -> str:
    """Markdown-Link von einer Seite zur anderen, damit MkDocs ihn
    aufloest und `--strict` ihn mitpruefen kann."""
    return posixpath.relpath(nach, posixpath.dirname(von)) or nach


def _kurzangabe(werkzeug: dict) -> str:
    teile = []
    for schluessel in ("schwierigkeit", "kosten", "verarbeitung"):
        wert = werkzeug.get(schluessel)
        if wert:
            teile.append(str(wert))
    return " · ".join(teile)


def _karten(phase: str, seite: str) -> str:
    """Kartenraster der Werkzeuge einer Phase, als Markdown."""
    treffer = [w for w in WERKZEUGE
               if phase in (w["werkzeug"].get("phase") or [])]
    if not treffer:
        return ""
    zeilen = ['<div class="grid cards fl-werkzeugkarten" markdown>', ""]
    for eintrag in treffer:
        werkzeug = eintrag["werkzeug"]
        ziel = _relativ(seite, eintrag["quelle"])
        zeilen.append(f'-   **[{eintrag["titel"]}]({ziel})**')
        zeilen.append("")
        zeilen.append("    ---")
        zeilen.append("")
        wofuer = werkzeug.get("wofuer")
        if wofuer:
            zeilen.append(f"    {wofuer}")
            zeilen.append("")
        zeilen.append(f'    <span class="fl-kurzangabe">{_e(_kurzangabe(werkzeug))}</span>')
        zeilen.append("")
    zeilen.append("</div>")
    return "\n".join(zeilen)


def _uebersicht(seite: str) -> str:
    """Alle Werkzeuge nach Phase, als Tabelle. Fuer die Vergleichsansicht."""
    teile = []
    for phase, beschriftung in PHASEN.items():
        treffer = [w for w in WERKZEUGE
                   if phase in (w["werkzeug"].get("phase") or [])]
        if not treffer:
            continue
        teile.append(f"### {beschriftung}")
        teile.append("")
        teile.append("| Werkzeug | Schwierigkeit | Kosten | Verarbeitung | Wofür |")
        teile.append("|---|---|---|---|---|")
        for eintrag in treffer:
            werkzeug = eintrag["werkzeug"]
            ziel = _relativ(seite, eintrag["quelle"])
            # Die Zusaetze gehoeren in die Uebersicht, sonst steht dort
            # etwa "kostenpflichtig" bei einem Dienst, den man ueber die
            # Hochschullizenz nutzt, ohne selbst zu zahlen.
            def feld(schluessel):
                wert = werkzeug.get(schluessel, "")
                zusatz = werkzeug.get(f"{schluessel}_zusatz")
                if wert and zusatz:
                    return f'{wert}<br><span class="fl-kurzangabe">{_e(zusatz)}</span>'
                return str(wert)

            teile.append(
                f'| [{eintrag["titel"]}]({ziel}) '
                f'| {feld("schwierigkeit")} '
                f'| {feld("kosten")} '
                f'| {feld("verarbeitung")} '
                f'| {werkzeug.get("wofuer", "")} |')
        teile.append("")
    return "\n".join(teile)


def _graph_als_liste(seite: str) -> str:
    """Der Wissensgraph in Textform.

    Der Graph braucht JavaScript und ist mit einer Tastatur oder einem
    Screenreader nicht bedienbar. Dieselben Verbindungen stehen deshalb
    zusaetzlich als Liste da, aufgeklappt zu bekommen."""
    if not WIKI_NOTIZEN:
        return ""
    nach_schicht: dict = {}
    for quelle, notiz in WIKI_NOTIZEN.items():
        nach_schicht.setdefault(notiz["schicht"] or "Übrige", []).append(quelle)

    zeilen = ['??? randnotiz "Dieselben Verbindungen als Liste"', ""]
    for schicht in ("Synthese", "Konzept", "Quellnotiz"):
        eintraege = sorted(nach_schicht.get(schicht, []),
                           key=lambda q: WIKI_NOTIZEN[q]["titel"].lower())
        if not eintraege:
            continue
        zeilen.append(f"    **{schicht}**")
        zeilen.append("")
        for quelle in eintraege:
            notiz = WIKI_NOTIZEN[quelle]
            nachbarn = NACHBARN.get(quelle, {"raus": set(), "rein": set()})
            anzahl = len(nachbarn["raus"] | nachbarn["rein"])
            pfad = _relativ(seite, quelle)
            zeilen.append(f'    - [{notiz["titel"]}]({pfad}) '
                          f'({anzahl} Verbindungen)')
        zeilen.append("")
    return "\n".join(zeilen)


def _platzhalter_ersetzen(markdown: str, seite: str) -> str:
    def ersatz(treffer):
        was = treffer.group(1)
        if was == "alle":
            return _uebersicht(seite)
        if was == "graphliste":
            return _graph_als_liste(seite)
        if was in PHASEN:
            return _karten(was, seite)
        # Unbekannte Phase sichtbar lassen, damit der Tippfehler auffaellt.
        return treffer.group(0)
    return PLATZHALTER.sub(ersatz, markdown)


def on_page_markdown(markdown, page, config, files):
    kopf = page.meta or {}
    heute = dt.date.today()

    if kopf.get("type") in OHNE_SEITENLEISTE:
        verstecken = list(kopf.get("hide") or [])
        if "navigation" not in verstecken:
            verstecken.append("navigation")
        page.meta["hide"] = verstecken

    markdown = _platzhalter_ersetzen(markdown, page.file.src_uri)

    if kopf.get("type") in OHNE_SEITENLEISTE:
        block = _nachbarn_block(page.file.src_uri)
        if block:
            markdown = markdown.rstrip() + "\n\n" + block + "\n"

    if kopf.get("type") == "Quellnotiz":
        return _einfuegen(markdown, _notizkopf(kopf, heute))

    if kopf.get("werkzeug"):
        block = _steckbrief(kopf["werkzeug"], _glossar(config))
        if block:
            return _einfuegen(markdown, block)

    return markdown
