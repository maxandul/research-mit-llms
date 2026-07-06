# Forschungsstand: das Wiki hinter dieser Seite

Diese Sektion ist zwei Dinge zugleich: die **wissenschaftliche Grundlage**
der Empfehlungen auf dieser Website und ein **begehbares Fallbeispiel** für
den Workflow, den [Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md)
beschreibt. Was dort als Anleitung steht, wurde hier real durchgeführt.

!!! warning "Im Aufbau"
    Das Wiki wächst sprintweise, Thema für Thema. Bisher abgedeckt:
    KI-Nutzung deklarieren. Als Nächstes geplant: qualitatives Codieren,
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
   inhaltlichen Seiten.

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

## Wissensgraph

Die Verlinkungen zwischen Quellnotizen, Konzepten, Synthesen und
Website-Seiten bilden einen Graphen, der bei jedem Build automatisch aus
den Markdown-Links erzeugt wird. Ziehen, zoomen, klicken — jeder Knoten
führt zur jeweiligen Seite.

<div id="wiki-graph" style="width:100%;height:480px;"></div>
<p id="wiki-graph-legende" style="font-size:.8em;opacity:.75;"></p>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script>
(function () {
  function drawGraph() {
    var container = document.getElementById("wiki-graph");
    if (!container || container.dataset.rendered) return;
    container.dataset.rendered = "1";
    container.style.border = "1px solid var(--md-default-fg-color--lightest, #ddd)";
    container.style.borderRadius = "6px";
    var farben = { quelle: "#8da0cb", konzept: "#fc8d62", synthese: "#66c2a5", seite: "#b3b3b3" };
    var namen = { quelle: "Quellnotiz", konzept: "Konzept", synthese: "Synthese", seite: "Website-Seite" };
    var legende = document.getElementById("wiki-graph-legende");
    if (legende) legende.innerHTML = Object.keys(farben).map(function (k) {
      return '<span style="color:' + farben[k] + ';">&#9679;</span> ' + namen[k];
    }).join(" &nbsp; ");
    fetch("graph.json").then(function (r) { return r.json(); }).then(function (data) {
      var w = container.clientWidth, h = container.clientHeight;
      var svg = d3.select(container).append("svg").attr("width", w).attr("height", h);
      var g = svg.append("g");
      svg.call(d3.zoom().scaleExtent([0.3, 4]).on("zoom", function (ev) { g.attr("transform", ev.transform); }));
      var sim = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(function (d) { return d.id; }).distance(70))
        .force("charge", d3.forceManyBody().strength(-220))
        .force("center", d3.forceCenter(w / 2, h / 2))
        .force("collide", d3.forceCollide(18));
      var link = g.selectAll("line").data(data.links).join("line")
        .attr("stroke", "#999").attr("stroke-opacity", 0.5);
      var node = g.selectAll("circle").data(data.nodes).join("circle")
        .attr("r", function (d) { return d.layer === "konzept" ? 9 : 7; })
        .attr("fill", function (d) { return farben[d.layer] || "#b3b3b3"; })
        .style("cursor", "pointer")
        .call(d3.drag()
          .on("start", function (ev, d) { if (!ev.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
          .on("drag", function (ev, d) { d.fx = ev.x; d.fy = ev.y; })
          .on("end", function (ev, d) { if (!ev.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }))
        .on("click", function (ev, d) { window.location.href = d.url; });
      node.append("title").text(function (d) { return d.label; });
      var text = g.selectAll("text").data(data.nodes).join("text")
        .text(function (d) { return d.label; })
        .attr("font-size", "9px")
        .attr("fill", "var(--md-default-fg-color, #333)")
        .attr("pointer-events", "none");
      sim.on("tick", function () {
        link.attr("x1", function (d) { return d.source.x; }).attr("y1", function (d) { return d.source.y; })
            .attr("x2", function (d) { return d.target.x; }).attr("y2", function (d) { return d.target.y; });
        node.attr("cx", function (d) { return d.x; }).attr("cy", function (d) { return d.y; });
        text.attr("x", function (d) { return d.x + 11; }).attr("y", function (d) { return d.y + 3; });
      });
    }).catch(function () {
      container.innerHTML = '<p style="padding:1em;">Graph-Daten nicht gefunden (graph.json entsteht beim Build).</p>';
    });
  }
  if (window.document$) { window.document$.subscribe(drawGraph); } else { drawGraph(); }
})();
</script>

## Arbeitsweise

Pro Thema läuft ein Recherche-Sprint in zwei Phasen. **Sichten:** Suche
über Semantic Scholar und OpenAlex, DOI auflösen, Abstracts lesen,
Kandidaten priorisieren. **Vertiefen:** Volltext beschaffen (lokal in
`rohdaten/` abgelegt, nicht im Repo), lesen — erst auf dieser Basis
entstehen Quellnotiz, Konzeptnotizen und Synthese. Wo ausnahmsweise nur
das Abstract verfügbar ist, steht das ausdrücklich in der Notiz; solche
Notizen gelten als vorläufig. Jede inhaltliche Änderung ist im
[Changelog](../ressourcen/changelog.md) dokumentiert.

Die vollständigen Spielregeln — das **Schema** im Sinn von
[Eigenes Forschungs-Wiki aufbauen](../workflows/forschungs-wiki.md) — stehen
in der Datei
[CLAUDE.md im Repository](https://github.com/maxandul/research-mit-llms/blob/main/CLAUDE.md):
Sie sagt dem LLM-Agenten, wie Quellen verifiziert und eingepflegt werden,
welche Vorlagen gelten und was nach einem Sprint zu tun ist.

!!! note "Warum die Verifikation so betont wird"
    LLMs erfinden mitunter Referenzen, inklusive plausibler DOIs (siehe
    [LLMs verstehen](../grundlagen/llms-verstehen.md)). Eine Website über
    verantwortungsvolle LLM-Nutzung kann sich keine halluzinierte Quelle
    leisten. Deshalb wird jede Quelle von Hand gegen das Original geprüft,
    bevor sie hier erscheint.

!!! note "Grenzen dieser Recherche"
    Die Suche läuft über öffentlich zugängliche Korpora (Semantic Scholar,
    OpenAlex, Verlags- und Policy-Seiten). Sie ersetzt keine systematische
    Recherche in lizenzierten Fachdatenbanken — es kann also relevante
    Literatur geben, die hier fehlt. Und die Notizen ersetzen nicht die
    eigene Lektüre: Wer eine Quelle weiterverwenden will, liest das
    Original.
