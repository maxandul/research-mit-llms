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
import re

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


def _steckbrief(werkzeug: dict) -> str:
    if not isinstance(werkzeug, dict):
        return ""
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

    for schluessel, label in (("kosten", "Kosten"), ("wofuer", "Wofür")):
        wert = werkzeug.get(schluessel)
        if not wert:
            continue
        zusatz = werkzeug.get(f"{schluessel}_zusatz")
        teile.append(
            '<div class="fl-steckbrief__feld">'
            f"<dt>{label}</dt><dd>{_e(str(wert).strip())}"
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


def on_page_markdown(markdown, page, config, files):
    kopf = page.meta or {}
    heute = dt.date.today()

    if kopf.get("type") in OHNE_SEITENLEISTE:
        verstecken = list(kopf.get("hide") or [])
        if "navigation" not in verstecken:
            verstecken.append("navigation")
        page.meta["hide"] = verstecken

    if kopf.get("type") == "Quellnotiz":
        return _einfuegen(markdown, _notizkopf(kopf, heute))

    if kopf.get("werkzeug"):
        block = _steckbrief(kopf["werkzeug"])
        if block:
            return _einfuegen(markdown, block)

    return markdown
