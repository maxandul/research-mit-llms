---
icon: material/microscope
description: >-
  Die wissenschaftliche Grundlage der Empfehlungen dieser Website und
  zugleich ein begehbares Fallbeispiel für ein LLM-gepflegtes Wiki.
---

# Forschungsstand: das Wiki hinter dieser Seite

Diese Sektion ist zwei Dinge zugleich: die **wissenschaftliche Grundlage**
der Empfehlungen auf dieser Website und ein **begehbares Fallbeispiel** für
den Workflow, den [Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md)
beschreibt. Was dort als Anleitung steht, wurde hier real durchgeführt.

!!! randnotiz "Im Aufbau"
    Das Wiki wächst sprintweise, Thema für Thema. Bisher abgedeckt:
    KI-Nutzung deklarieren, qualitatives Codieren. Als Nächstes geplant:
    Transkription, Funktionsweise von LLMs. Der Stand jeder Notiz ist an
    ihrem Prüfdatum erkennbar; Änderungen stehen im
    [Changelog](../ressourcen/changelog.md).

## Wie das Wiki aufgebaut ist

Das Wiki folgt der Idee des [LLM-Wikis nach Karpathy](../werkzeuge/sammeln/llm-wiki.md)
(LLM pflegt die Wissensbasis; ingest/query/lint; Schema als Spielregeln)
und übernimmt von der [Umsetzung nach Goekce](https://github.com/mehmetgoekce/llm-wiki)
die Schichtung in Quellnotizen (L1) und Konzeptnotizen (L2). Drei Dinge
sind bewusst anders: MkDocs statt Obsidian (normale Markdown-Links statt
Wikilinks, der Graph entsteht beim Build), eine zusätzliche
**Synthese-Schicht** als Brücke zu den Website-Seiten, und
wissenschaftsspezifische Zutaten — Evidenzstufen, Verifikationsvermerke,
Changelog. Es besteht aus vier Schichten:

1. **Rohquellen** (PDFs, Volltexte): bleiben aus urheberrechtlichen Gründen
   lokal und sind nicht Teil dieses Repositories.
2. **[Quellnotizen](quellen/index.md)**: eine Notiz pro Quelle, in eigenen
   Worten. Kernaussagen, Einordnung, Evidenzstufe, Verifikationsvermerk.
   Sie tragen die Provenienz: Wer sagt was, und wie gut ist es belegt?
3. **[Konzeptnotizen](konzepte/index.md)**: atomare Themen,
   quellenübergreifend gepflegt. Ein Konzept bündelt, was mehrere Quellen
   zu einem Sachverhalt sagen, und verlinkt verwandte Konzepte — auch über
   Themen-Sprints hinweg. Hier entsteht das eigentliche Netz.
4. **Synthesen**: der verdichtete Forschungsstand pro Website-Thema,
   zusammengesetzt aus Konzepten. Aus ihnen fliessen die Belege in die
   inhaltlichen Seiten. Der Einfluss geht dabei in beide Richtungen: Meist
   stützen die Synthesen bestehende Seiten, aber die Evidenz führt. Drängt
   sich eine Synthese auf, die den Aufbau der Website verändern würde,
   darf und soll sich die Website ändern.

### Was sich im Juli 2026 geändert hat

Jede Notiz trägt seither einen kleinen Datenblock am Dateianfang
(YAML-Frontmatter) nach dem **[Open Knowledge Format](../werkzeuge/sammeln/llm-wiki.md#ein-standard-zeichnet-sich-ab-das-open-knowledge-format)**,
einer offenen Spezifikation für LLM-Wikis. Für Lesende ändert sich am Text
nichts: Der Block ist auf der Website nicht sichtbar und die Notizen sind
dieselben geblieben. Sichtbar sind zwei Nebenwirkungen. Notizen, die noch
vorläufig sind oder als überholt gelten, tragen in der Navigation eine
**Statusmarke**. Und im Wissensgraphen unten zeigt der Tooltip eines Knotens
jetzt zusätzlich die Evidenzstufe.

Hinter den Kulissen ändert sich mehr: Was vorher als Fliesstext in den
Notizen stand (Evidenzstufe, Prüfdatum, Prüfumfang, verwendete Modelle),
ist jetzt maschinell abfragbar. Das Skript
`tools/wiki_lint.py` meldet damit selbständig, welche Notiz nur auf einem
Abstract beruht, welche Policy zur Nachprüfung fällig ist und welche Notiz
verwaist. Vorher war das Handarbeit, und Handarbeit unterbleibt.

## Evidenzstufen

Nicht jede Quelle trägt gleich viel. Jede Quellnotiz und jeder Beleg auf den
inhaltlichen Seiten ist deshalb gekennzeichnet:

| Stufe | Bedeutung |
|-------|-----------|
| **Peer-reviewed** | Begutachtete Publikation in Journal oder Konferenzband |
| **Preprint** | Wissenschaftliche Arbeit ohne (abgeschlossene) Begutachtung |
| **Policy** | Offizielle Richtlinie (Verlage, ICMJE, COPE, Hochschulen) |
| **Doku** | Offizielle technische Dokumentation eines Herstellers |
| **Praxis** | Erfahrungsberichte, Blogposts, Community-Wissen |

Das Feld bewegt sich schnell: Manches ist bei Publikation schon überholt,
zu manchen Praxisfragen existiert schlicht noch keine belastbare Forschung.
Wo die Evidenz dünn ist, steht das dabei.

Aus demselben Grund gilt hier ein zweiter Prüfblick neben der
Evidenzstufe: **Welche Modelle wurden wie eingesetzt, und wann?** Ob eine
Studie GPT-3.5 im Web-Chat oder ein aktuelles Reasoning-Modell per API
getestet hat, entscheidet darüber, was ihre Ergebnisse heute noch
bedeuten. Jede Quellnotiz hält diese Angaben deshalb fest; die
Begründung steht im Konzept
[Modell und Einsatzart bestimmen das Ergebnis](konzepte/modell-und-einsatzart.md).

## Wissensgraph

Die Verlinkungen zwischen Quellnotizen, Konzepten, Synthesen und
Website-Seiten bilden einen Graphen, der bei jedem Build automatisch aus
den Markdown-Links erzeugt wird. Ziehen, zoomen, klicken — jeder Knoten
führt zur jeweiligen Seite.

<div class="fl-graph">
  <div class="fl-graph__steuerung" id="wiki-graph-filter"></div>
  <div id="wiki-graph" role="img"
       aria-label="Interaktiver Wissensgraph. Dieselben Verbindungen stehen darunter als Liste."></div>
  <p class="fl-graph__hinweis">
    Ziehen, zoomen, klicken. Beim Zeigen auf einen Knoten wird seine
    Nachbarschaft hervorgehoben; Beschriftungen erscheinen ab mittlerer
    Zoomstufe.
  </p>
</div>

{{ werkzeuge:graphliste }}

<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script>
(function () {
  function stil(name) {
    return getComputedStyle(document.body).getPropertyValue(name).trim();
  }

  function drawGraph() {
    var container = document.getElementById("wiki-graph");
    if (!container || !window.d3) return;
    // Neu zeichnen, wenn schon etwas dasteht: Beim Wechsel zwischen
    // hellem und dunklem Modus aendern sich die Token-Farben, und der
    // Graph liest sie nur beim Zeichnen.
    container.innerHTML = "";
    var alteLeiste = document.getElementById("wiki-graph-filter");
    if (alteLeiste) alteLeiste.innerHTML = "";

    var namen = { quelle: "Quellnotiz", konzept: "Konzept",
                  synthese: "Synthese", seite: "Website-Seite" };
    // Farben aus den Design-Tokens, damit der Graph im dunklen Modus stimmt.
    var farben = {
      quelle:   stil("--fl-ev-preprint-linie"),
      konzept:  stil("--fl-accent"),
      synthese: stil("--fl-ev-peer-linie"),
      seite:    stil("--fl-text-leise")
    };
    var aus = {};

    fetch("graph.json").then(function (r) { return r.json(); }).then(function (data) {
      // Die Breite kommt aus dem Layout. Steht das noch nicht (mit
      // navigation.instant feuert document$ vorher), waere sie 0 und der
      // Graph unsichtbar. Deshalb messen wir defensiv und zeichnen bei
      // Groessenaenderung neu.
      var w = Math.round(container.getBoundingClientRect().width)
              || (container.parentElement && container.parentElement.clientWidth)
              || 800;
      var h = container.clientHeight || 480;
      var svg = d3.select(container).append("svg")
        .attr("width", "100%").attr("height", h)
        .attr("viewBox", [0, 0, w, h])
        .attr("preserveAspectRatio", "xMidYMid meet");
      var g = svg.append("g");

      // Knotengroesse nach Anzahl Verbindungen: was viel verknuepft
      // ist, ist im Wiki auch zentral.
      var grad = {};
      data.links.forEach(function (l) {
        grad[l.source] = (grad[l.source] || 0) + 1;
        grad[l.target] = (grad[l.target] || 0) + 1;
      });
      var radius = function (d) { return 5 + Math.min(7, (grad[d.id] || 0) * 0.9); };

      var zoomstufe = 1;
      var zoom = d3.zoom().scaleExtent([0.3, 4]).on("zoom", function (ev) {
        g.attr("transform", ev.transform);
        zoomstufe = ev.transform.k;
        text.attr("display", zoomstufe >= 1.4 ? null : "none");
      });
      svg.call(zoom);

      var sim = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(function (d) { return d.id; }).distance(70))
        .force("charge", d3.forceManyBody().strength(-240))
        .force("center", d3.forceCenter(w / 2, h / 2))
        .force("collide", d3.forceCollide(20));

      var link = g.selectAll("line").data(data.links).join("line")
        .attr("stroke", stil("--fl-linie-stark")).attr("stroke-opacity", 0.6);

      var node = g.selectAll("circle").data(data.nodes).join("circle")
        .attr("r", radius)
        .attr("fill", function (d) { return farben[d.layer] || farben.seite; })
        .style("cursor", "pointer")
        .call(d3.drag()
          .on("start", function (ev, d) { if (!ev.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
          .on("drag", function (ev, d) { d.fx = ev.x; d.fy = ev.y; })
          .on("end", function (ev, d) { if (!ev.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }))
        .on("click", function (ev, d) { window.location.href = d.url; });

      node.append("title").text(function (d) {
        var zusatz = [namen[d.layer] || ""];
        if (d.evidenzstufe) zusatz.push(d.evidenzstufe);
        if (d.status === "draft") zusatz.push("vorläufig");
        if (d.status === "deprecated") zusatz.push("überholt");
        return d.label + " (" + zusatz.filter(Boolean).join(", ") + ")";
      });

      var text = g.selectAll("text").data(data.nodes).join("text")
        .text(function (d) { return d.label.length > 34 ? d.label.slice(0, 33) + "…" : d.label; })
        .attr("font-size", "9px")
        .attr("fill", stil("--fl-text-sekundaer"))
        .attr("pointer-events", "none")
        .attr("display", "none");

      // Nachbarschaft beim Zeigen hervorheben, den Rest daempfen.
      var nachbarn = {};
      data.links.forEach(function (l) {
        var s = l.source.id || l.source, t = l.target.id || l.target;
        (nachbarn[s] = nachbarn[s] || {})[t] = 1;
        (nachbarn[t] = nachbarn[t] || {})[s] = 1;
      });
      node.on("mouseenter", function (ev, d) {
        node.attr("opacity", function (o) {
          return o.id === d.id || (nachbarn[d.id] || {})[o.id] ? 1 : 0.15;
        });
        link.attr("stroke-opacity", function (l) {
          var s = l.source.id || l.source, t = l.target.id || l.target;
          return s === d.id || t === d.id ? 0.9 : 0.05;
        });
        text.attr("display", function (o) {
          return o.id === d.id || (nachbarn[d.id] || {})[o.id] ? null : "none";
        });
      }).on("mouseleave", function () {
        node.attr("opacity", function (o) { return aus[o.layer] ? 0.12 : 1; });
        link.attr("stroke-opacity", 0.6);
        text.attr("display", zoomstufe >= 1.4 ? null : "none");
      });

      // Filter nach Schicht.
      var leiste = d3.select("#wiki-graph-filter");
      Object.keys(namen).forEach(function (k) {
        leiste.append("button")
          .attr("class", "fl-graph__chip")
          .attr("type", "button")
          .attr("aria-pressed", "true")
          .html('<span class="fl-graph__punkt" style="background:' + farben[k] + '"></span>' + namen[k])
          .on("click", function () {
            aus[k] = !aus[k];
            d3.select(this).attr("aria-pressed", aus[k] ? "false" : "true");
            node.attr("opacity", function (o) { return aus[o.layer] ? 0.12 : 1; });
            text.attr("opacity", function (o) { return aus[o.layer] ? 0.12 : 1; });
          });
      });

      sim.on("tick", function () {
        link.attr("x1", function (d) { return d.source.x; }).attr("y1", function (d) { return d.source.y; })
            .attr("x2", function (d) { return d.target.x; }).attr("y2", function (d) { return d.target.y; });
        node.attr("cx", function (d) { return d.x; }).attr("cy", function (d) { return d.y; });
        text.attr("x", function (d) { return d.x + radius(d) + 3; }).attr("y", function (d) { return d.y + 3; });
      });
    }).catch(function () {
      container.innerHTML = '<p style="padding:1em;">Graph-Daten nicht gefunden (graph.json entsteht beim Build).</p>';
    });
  }
  var beobachter = null;
  var groessenbeobachter = null;
  var letzteBreite = 0;
  var warteUhr = null;

  // Mit navigation.instant tauscht Material den Seiteninhalt aus, ohne
  // neu zu laden. Dann kann dieser Code vor d3 laufen; ohne d3 wirft das
  // Zeichnen und der Graph bleibt leer. Also kurz warten statt scheitern.
  // Kommt d3 gar nicht, bleibt die Liste darunter als Ersatz stehen.
  function mitD3(weiter) {
    if (window.d3) { weiter(); return; }
    var versuche = 0;
    warteUhr = setInterval(function () {
      if (window.d3) { clearInterval(warteUhr); warteUhr = null; weiter(); }
      else if (++versuche > 100) { clearInterval(warteUhr); warteUhr = null; }
    }, 100);
  }

  function start() {
    var container = document.getElementById("wiki-graph");
    // Beobachter abbauen, wenn wir den Graphen verlassen haben. Mit
    // navigation.instant laeuft dieselbe Seite weiter, sonst wuerden
    // sich die Beobachter bei jedem Seitenwechsel anhaeufen.
    if (beobachter) { beobachter.disconnect(); beobachter = null; }
    if (groessenbeobachter) { groessenbeobachter.disconnect(); groessenbeobachter = null; }
    if (warteUhr) { clearInterval(warteUhr); warteUhr = null; }
    if (!container) return;

    // Zeichnet, sobald der Container eine echte Breite hat, und erneut
    // bei nennenswerter Aenderung (Fenster, Seitenleiste, Drehung).
    letzteBreite = 0;
    groessenbeobachter = new ResizeObserver(function (eintraege) {
      var breite = Math.round(eintraege[0].contentRect.width);
      if (breite > 0 && Math.abs(breite - letzteBreite) > 40) {
        letzteBreite = breite;
        drawGraph();
      }
    });
    groessenbeobachter.observe(container);
    mitD3(drawGraph);
    // Material setzt beim Umschalten das Attribut data-md-color-scheme
    // auf <body>. Darauf hoeren, statt die Farben fest zu verdrahten.
    beobachter = new MutationObserver(function () { drawGraph(); });
    beobachter.observe(document.body,
      { attributes: true, attributeFilter: ["data-md-color-scheme"] });
  }
  if (window.document$) { window.document$.subscribe(start); } else { start(); }
})();
</script>
## Arbeitsweise

Pro Thema läuft ein Recherche-Sprint in zwei Phasen. **Sichten:** Suche
über Semantic Scholar und OpenAlex, DOI auflösen, Abstracts lesen,
Kandidaten priorisieren. **Vertiefen:** Volltext beschaffen (lokal in
`rohdaten/` abgelegt, nicht im Repo), lesen — erst auf dieser Basis
entstehen Quellnotiz, Konzeptnotizen und Synthese. Wo ausnahmsweise nur
das Abstract verfügbar ist, steht das ausdrücklich in der Notiz; solche
Notizen gelten als vorläufig. Parallel wird jede Quelle in einer
Zotero-Sammlung abgelegt, per MCP direkt vom LLM (Referenz plus PDF, siehe
[Zotero](../werkzeuge/sammeln/zotero.md)), damit die Belege zitierfähig
bleiben. Jede inhaltliche Änderung ist im
[Changelog](../ressourcen/changelog.md) dokumentiert.

Die vollständigen Spielregeln — das **Schema** im Sinn von
[Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md) — stehen
in der Datei
[CLAUDE.md im Repository](https://github.com/maxandul/research-mit-llms/blob/main/CLAUDE.md):
Sie sagt dem LLM-Agenten, wie Quellen verifiziert und eingepflegt werden,
welche Vorlagen gelten und was nach einem Sprint zu tun ist.

!!! randnotiz "Warum die Verifikation so betont wird"
    LLMs erfinden mitunter Referenzen, inklusive plausibler DOIs (siehe
    [LLMs verstehen](../grundlagen/llms-verstehen.md)). Eine Website über
    verantwortungsvolle LLM-Nutzung kann sich keine halluzinierte Quelle
    leisten. Deshalb wird jede Quelle von Hand gegen das Original geprüft,
    bevor sie hier erscheint.

!!! randnotiz "Grenzen dieser Recherche"
    Die Suche läuft über öffentlich zugängliche Korpora (Semantic Scholar,
    OpenAlex, Verlags- und Policy-Seiten). Sie ersetzt keine systematische
    Recherche in lizenzierten Fachdatenbanken — es kann also relevante
    Literatur geben, die hier fehlt. Und die Notizen ersetzen nicht die
    eigene Lektüre: Wer eine Quelle weiterverwenden will, liest das
    Original.
