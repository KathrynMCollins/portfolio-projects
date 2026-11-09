// Results explorer: a chart comparing conditions per model, and a filterable set of rewrites.
// Data: explorer/data.json, built from the test kit by _tools/build_explorer_data.py.
(function () {
  "use strict";
  var $ = function (id) { return document.getElementById(id); };
  var PAGE = 24;
  var data, shown = PAGE;

  // Guided comparison uses the main and added-models runs, as the pre-registration defines it.
  var GUIDED_SETS = { main: true, added: true };
  var METRICS = [
    { id: "natural", label: "Reads naturally (human score, 1 to 3)", human: true, fmt: 1,
      get: function (r) { return r.human && r.human.inSample ? r.human.natural : null; } },
    { id: "meaning", label: "Meaning fully preserved (human score, % of rewrites)", human: true, pct: true,
      get: function (r) { return r.human && r.human.inSample ? (r.human.meaning === "yes" ? 1 : 0) : null; } },
    { id: "headingsAdded", label: "Headings added per rewrite", fmt: 1, get: function (r) { return r.headingsAdded; } },
    { id: "warnings", label: "Scanner warnings per rewrite", fmt: 1, get: function (r) { return r.warnings; } },
    { id: "substanceLost", label: "Substance checks lost per rewrite", fmt: 2, get: function (r) { return r.substanceLost; } },
    { id: "wordRatio", label: "Length compared with the original (1.0 = same)", fmt: 2, get: function (r) { return r.wordRatio; } }
  ];

  function el(tag, attrs, children) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "text") n.textContent = attrs[k];
      else if (k === "class") n.className = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { if (c) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return n;
  }
  function svg(tag, attrs) {
    var n = document.createElementNS("http://www.w3.org/2000/svg", tag);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    return n;
  }
  function modelLabel(id) { return data.models.filter(function (m) { return m.id === id; })[0].label; }
  function setLabel(id) { return data.sets.filter(function (s) { return s.id === id; })[0].label; }
  function mean(a) { return a.length ? a.reduce(function (s, x) { return s + x; }, 0) / a.length : null; }
  function format(v, m) {
    if (v === null) return "no data";
    return m.pct ? Math.round(v * 100) + "%" : v.toFixed(m.fmt);
  }

  /* ---------- Chart ---------- */
  function summarize(metric) {
    return data.models.map(function (m) {
      function vals(cond) {
        return data.rewrites.filter(function (r) {
          return r.model === m.id && (cond === "guided" ? GUIDED_SETS[r.set] : r.set === "baseline");
        }).map(metric.get).filter(function (v) { return v !== null && v !== undefined; });
      }
      var w = vals("guided"), wo = vals("baseline");
      return { model: m, with: mean(w), without: mean(wo), nWith: w.length, nWithout: wo.length };
    });
  }

  function drawChart() {
    var metric = METRICS.filter(function (m) { return m.id === $("metric").value; })[0];
    var rows = summarize(metric);
    var chart = $("chart");
    while (chart.firstChild) chart.removeChild(chart.firstChild);

    var W = Math.max(320, $("chart-wrap").clientWidth), rowH = 46, top = 28, bottom = 34;
    var left = W < 520 ? 92 : 120, right = 28, H = top + rows.length * rowH + bottom;
    chart.setAttribute("viewBox", "0 0 " + W + " " + H);
    chart.setAttribute("height", H);

    var maxV = 0;
    rows.forEach(function (r) { [r.with, r.without].forEach(function (v) { if (v !== null && v > maxV) maxV = v; }); });
    var lo = 0, hi;
    if (metric.id === "natural") { lo = 1; hi = 3; }
    else if (metric.pct) hi = 1;
    else hi = maxV <= 1 ? 1 : Math.ceil(maxV * 2) / 2;
    if (metric.id === "wordRatio") { lo = 0.5; hi = Math.max(1.5, Math.ceil(maxV * 10) / 10); }
    var x = function (v) { return left + (v - lo) / (hi - lo) * (W - left - right); };

    var ticks = 4, i, t;
    for (i = 0; i <= ticks; i++) {
      t = lo + (hi - lo) * i / ticks;
      chart.appendChild(svg("line", { class: "grid", x1: x(t), x2: x(t), y1: top - 8, y2: H - bottom + 4 }));
      var lab = svg("text", { class: "axis-label", x: x(t), y: H - 12, "text-anchor": "middle" });
      lab.textContent = metric.pct ? Math.round(t * 100) + "%" : (Math.round(t * 100) / 100).toString();
      chart.appendChild(lab);
    }

    rows.forEach(function (r, idx) {
      var cy = top + idx * rowH + rowH / 2;
      var name = svg("text", { class: "model-label", x: 0, y: cy + 5 });
      name.textContent = r.model.label;
      chart.appendChild(name);
      if (r.with !== null && r.without !== null) {
        chart.appendChild(svg("line", { class: "link", x1: x(r.with), x2: x(r.without), y1: cy, y2: cy }));
      }
      [["with", "With the standard", r.with, r.nWith], ["without", "Without the standard", r.without, r.nWithout]].forEach(function (d) {
        if (d[2] === null) return;
        var c = svg("circle", { class: "dot dot-" + d[0], cx: x(d[2]), cy: cy, r: 7, tabindex: 0, role: "img",
          "aria-label": r.model.label + ", " + d[1].toLowerCase() + ": " + format(d[2], metric) + " (" + d[3] + " rewrites)" });
        c.addEventListener("mouseenter", function () { showTip(c, r.model.label, d[1], format(d[2], metric), d[3]); });
        c.addEventListener("focus", function () { showTip(c, r.model.label, d[1], format(d[2], metric), d[3]); });
        c.addEventListener("mouseleave", hideTip);
        c.addEventListener("blur", hideTip);
        chart.appendChild(c);
        if (idx === 0) {
          var dl = svg("text", { class: "direct-label", x: x(d[2]), y: cy - 13, "text-anchor": "middle" });
          dl.textContent = d[0] === "with" ? "With" : "Without";
          chart.appendChild(dl);
        }
      });
    });

    var note = metric.human
      ? "Human scores come from the blind sample: two rewrites per model and passage in each condition. They describe what one editor saw; they cannot rank the models."
      : "Averages over every rewrite: 30 per model in each condition. With the standard means the main and added-models runs; the replication is in the compare view below.";
    $("chart-desc").textContent = metric.label + ". " + note;
    drawTable(rows, metric);
  }

  function drawTable(rows, metric) {
    var t = $("chart-table");
    t.textContent = "";
    var head = el("thead", null, [el("tr", null, [
      el("th", { scope: "col", text: "Model" }), el("th", { scope: "col", text: "With the standard" }),
      el("th", { scope: "col", text: "Without the standard" }), el("th", { scope: "col", text: "Rewrites (with / without)" })])]);
    var body = el("tbody");
    rows.forEach(function (r) {
      body.appendChild(el("tr", null, [el("th", { scope: "row", text: r.model.label }),
        el("td", { text: format(r.with, metric) }), el("td", { text: format(r.without, metric) }),
        el("td", { text: r.nWith + " / " + r.nWithout })]));
    });
    t.appendChild(el("caption", { class: "visually-hidden", text: metric.label }));
    t.appendChild(head); t.appendChild(body);
  }

  function showTip(target, model, cond, value, n) {
    var tip = $("tooltip"), wrap = $("chart-wrap");
    tip.textContent = "";
    tip.appendChild(el("strong", { text: model }));
    tip.appendChild(document.createTextNode(cond + ": " + value));
    tip.appendChild(el("br"));
    tip.appendChild(document.createTextNode(n + " rewrites"));
    tip.hidden = false;
    var b = target.getBoundingClientRect(), w = wrap.getBoundingClientRect();
    var left = Math.min(Math.max(0, b.left - w.left - 90), w.width - tip.offsetWidth);
    tip.style.left = left + "px";
    tip.style.top = (b.top - w.top - tip.offsetHeight - 10) + "px";
    target.classList.add("is-active");
  }
  function hideTip() {
    $("tooltip").hidden = true;
    document.querySelectorAll(".dot.is-active").forEach(function (d) { d.classList.remove("is-active"); });
  }

  /* ---------- Word diff ---------- */
  // Words keep their trailing whitespace, so removed and added runs keep their spacing.
  function tokens(s) {
    return (s.match(/\S+\s*/g) || []).map(function (t) { return { w: t.trim(), t: t }; });
  }
  function diff(a, b) {
    var lead = (b.match(/^\s*/) || [""])[0];
    var A = tokens(a), B = tokens(b), n = A.length, m = B.length, i, j;
    var L = [];
    for (i = 0; i <= n; i++) { L.push(new Uint16Array(m + 1)); }
    for (i = n - 1; i >= 0; i--) for (j = m - 1; j >= 0; j--) {
      L[i][j] = A[i].w === B[j].w ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
    }
    var out = lead ? [{ type: "same", text: lead }] : [], push = function (type, text) {
      var last = out[out.length - 1];
      if (last && last.type === type) last.text += text; else out.push({ type: type, text: text });
    };
    i = 0; j = 0;
    while (i < n && j < m) {
      if (A[i].w === B[j].w) { push("same", B[j].t); i++; j++; }
      else if (L[i + 1][j] >= L[i][j + 1]) { push("del", A[i].t); i++; }
      else { push("ins", B[j].t); j++; }
    }
    while (i < n) { push("del", A[i].t); i++; }
    while (j < m) { push("ins", B[j].t); j++; }
    return out;
  }
  function renderText(target, original, text, marked) {
    target.textContent = "";
    if (!marked) { target.textContent = text; return; }
    diff(original, text).forEach(function (p) {
      if (p.type === "same") target.appendChild(document.createTextNode(p.text));
      else {
        target.appendChild(el(p.type, { text: p.text }));
      }
    });
  }

  /* ---------- Filters ---------- */
  function chip(group, value, label, checked) {
    var id = "f-" + group + "-" + value;
    return el("label", { class: "chip", for: id }, [
      el("input", checked ? { type: "checkbox", id: id, name: group, value: value, checked: "" } : { type: "checkbox", id: id, name: group, value: value }),
      el("span", { text: label })]);
  }
  function checked(group) {
    return Array.prototype.map.call(document.querySelectorAll('input[name="' + group + '"]:checked'), function (i) { return i.value; });
  }

  function readState() {
    var p = new URLSearchParams(location.search);
    return {
      input: p.get("input"), run: p.get("run"), q: p.get("q"),
      condition: p.get("condition"), model: p.get("model"), set: p.get("set"),
      human: p.get("human") === "1", diff: p.get("diff") !== "0", metric: p.get("metric")
    };
  }
  function writeState() {
    var p = new URLSearchParams();
    p.set("input", $("f-input").value);
    p.set("run", $("f-run").value);
    if ($("f-q").value) p.set("q", $("f-q").value);
    p.set("condition", checked("condition").join(","));
    p.set("model", checked("model").join(","));
    p.set("set", checked("set").join(","));
    if ($("f-human").checked) p.set("human", "1");
    if (!$("f-diff").checked) p.set("diff", "0");
    p.set("metric", $("metric").value);
    try { history.replaceState(null, "", "?" + p.toString() + location.hash); } catch (e) { /* not essential */ }
  }

  function filtered() {
    var input = $("f-input").value, run = $("f-run").value, q = $("f-q").value.trim().toLowerCase();
    var cond = checked("condition"), models = checked("model"), sets = checked("set"), humanOnly = $("f-human").checked;
    return data.rewrites.filter(function (r) {
      return r.input === input && (run === "all" || String(r.run) === run) && cond.indexOf(r.condition) > -1 &&
        models.indexOf(r.model) > -1 && sets.indexOf(r.set) > -1 && (!humanOnly || r.human) &&
        (!q || r.text.toLowerCase().indexOf(q) > -1);
    }).sort(function (a, b) {
      var mo = data.models.map(function (m) { return m.id; });
      var so = data.sets.map(function (s) { return s.id; });
      return so.indexOf(a.set) - so.indexOf(b.set) || mo.indexOf(a.model) - mo.indexOf(b.model) || a.run - b.run;
    });
  }

  function card(r, original, marked) {
    var isWith = r.condition === "guided";
    var text = el("p", { class: "text-block" });
    renderText(text, original, r.text, marked);
    var metrics = el("dl", { class: "metrics" }, [
      ["Blockers", r.blockers], ["Warnings", r.warnings], ["Substance lost", r.substanceLost],
      ["Headings added", r.headingsAdded], ["Order changes", r.orderInversions],
      ["Length", r.wordRatio === null ? "n/a" : r.wordRatio.toFixed(2) + "×"]
    ].map(function (m) { return el("div", null, [el("dt", { text: m[0] }), el("dd", { text: String(m[1]) })]); }));
    var human = null;
    if (r.human) {
      human = el("p", { class: "human" }, [
        el("strong", { text: "Editor score: " }),
        "meaning " + r.human.meaning + ", reads naturally " + r.human.natural + " of 3" + (r.human.inSample ? "" : " (scored beyond the sample)")
      ]);
      if (r.human.note) human.appendChild(el("q", { text: r.human.note }));
    }
    var tags = [
      el("span", { class: "tag " + (isWith ? "tag-with" : "tag-without"), text: isWith ? "With standard" : "Without standard" }),
      el("span", { class: "tag tag-plain", text: setLabel(r.set) + ", run " + r.run })
    ];
    if (r.redacted) tags.push(el("span", { class: "tag tag-plain", text: "Environment details redacted" }));
    return el("li", { class: "card" }, [
      el("div", { class: "card-head" }, [el("h3", { class: "card-title", text: modelLabel(r.model) })].concat(tags)),
      metrics, human, text
    ]);
  }

  function renderCards(reset) {
    if (reset) shown = PAGE;
    var input = data.inputs.filter(function (i) { return i.id === $("f-input").value; })[0];
    $("original-text").textContent = input.original;
    var rows = filtered(), list = $("cards"), marked = $("f-diff").checked;
    list.textContent = "";
    if (!rows.length) {
      list.appendChild(el("li", { class: "empty", text: "No rewrites match these filters." }));
    }
    rows.slice(0, shown).forEach(function (r) { list.appendChild(card(r, input.original, marked)); });
    $("status").textContent = "Showing " + Math.min(shown, rows.length) + " of " + rows.length + " rewrites for “" + input.label + "”.";
    var more = $("more");
    more.hidden = rows.length <= shown;
    more.textContent = "Show " + Math.min(PAGE, rows.length - shown) + " more";
    writeState();
  }

  function init(d) {
    data = d;
    var st = readState();
    METRICS.forEach(function (m) { $("metric").appendChild(el("option", { value: m.id, text: m.label })); });
    if (st.metric && METRICS.some(function (m) { return m.id === st.metric; })) $("metric").value = st.metric;

    data.inputs.forEach(function (i) { $("f-input").appendChild(el("option", { value: i.id, text: i.label })); });
    $("f-input").value = st.input && data.inputs.some(function (i) { return i.id === st.input; }) ? st.input : "02-you-and-permission";
    $("f-run").value = st.run && $("f-run").querySelector('option[value="' + st.run + '"]') ? st.run : "1";
    $("f-q").value = st.q || "";
    $("f-human").checked = st.human;
    $("f-diff").checked = st.diff;

    function pick(param, all) { return param ? param.split(",") : all; }
    var conds = pick(st.condition, ["guided", "baseline"]);
    [["guided", "With standard"], ["baseline", "Without standard"]].forEach(function (c) {
      $("f-condition").appendChild(chip("condition", c[0], c[1], conds.indexOf(c[0]) > -1));
    });
    var models = pick(st.model, data.models.map(function (m) { return m.id; }));
    data.models.forEach(function (m) { $("f-model").appendChild(chip("model", m.id, m.label, models.indexOf(m.id) > -1)); });
    var sets = pick(st.set, ["main", "added", "baseline"]);
    data.sets.forEach(function (s) { $("f-set").appendChild(chip("set", s.id, s.label, sets.indexOf(s.id) > -1)); });

    $("metric").addEventListener("change", function () { drawChart(); writeState(); });
    $("filters").addEventListener("change", function () { renderCards(true); });
    var timer;
    $("f-q").addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(function () { renderCards(true); }, 200); });
    $("more").addEventListener("click", function () {
      var before = shown;
      shown += PAGE; renderCards(false);
      var next = $("cards").children[before];
      if (next) { next.setAttribute("tabindex", "-1"); next.focus(); }
    });
    var rt;
    window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(drawChart, 150); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") hideTip(); });

    drawChart();
    renderCards(true);
  }

  document.addEventListener("DOMContentLoaded", function () {
    fetch("data.json").then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    }).then(init).catch(function () {
      $("status").textContent = "The results data could not be loaded. The same data is in the test kit's CSV files.";
    });
  });
})();
