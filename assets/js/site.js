// Site behavior: theme toggle, heading anchors, scrollable tables, Mermaid diagrams.
(function () {
  "use strict";
  var root = document.documentElement;

  function effectiveTheme() {
    var set = root.getAttribute("data-theme");
    if (set === "light" || set === "dark") return set;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function syncToggle(btn) {
    var next = effectiveTheme() === "dark" ? "light" : "dark";
    btn.setAttribute("aria-label", "Switch to " + next + " theme");
  }

  function initTheme() {
    var btn = document.querySelector("[data-theme-toggle]");
    if (!btn) return;
    syncToggle(btn);
    btn.addEventListener("click", function () {
      var next = effectiveTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) { /* storage unavailable: theme lasts this page only */ }
      syncToggle(btn);
      document.dispatchEvent(new CustomEvent("themechange", { detail: next }));
    });
    if (window.matchMedia) {
      window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () { syncToggle(btn); });
    }
  }

  function initAnchors() {
    document.querySelectorAll(".prose h2[id], .prose h3[id]").forEach(function (h) {
      if (h.closest(".home-prose") && h.tagName === "H3") return;
      var a = document.createElement("a");
      a.className = "heading-anchor";
      a.href = "#" + h.id;
      a.textContent = "#";
      a.setAttribute("aria-label", "Link to section: " + h.textContent.trim());
      h.appendChild(a);
    });
  }

  function initTables() {
    document.querySelectorAll(".prose table").forEach(function (t) {
      if (t.parentElement.classList.contains("table-scroll")) return;
      var wrap = document.createElement("div");
      wrap.className = "table-scroll";
      wrap.setAttribute("role", "region");
      wrap.setAttribute("tabindex", "0");
      var label = t.previousElementSibling && /^H[2-4]$/.test(t.previousElementSibling.tagName)
        ? t.previousElementSibling.textContent.replace(/#$/, "").trim() : "Table";
      wrap.setAttribute("aria-label", label);
      t.parentNode.insertBefore(wrap, t);
      wrap.appendChild(t);
    });
  }

  function initMermaid() {
    var blocks = Array.prototype.slice.call(document.querySelectorAll("pre > code.language-mermaid"));
    if (!blocks.length) return;
    var s = document.createElement("script");
    s.src = "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js";
    // Only swap the code blocks for diagrams once the library has loaded; if it fails, the source stays readable.
    s.onload = function () {
      var divs = blocks.map(function (code) {
        var div = document.createElement("div");
        div.className = "mermaid";
        div.setAttribute("role", "img");
        div.setAttribute("aria-label", "Diagram. The same steps are described in the numbered list that follows.");
        div.textContent = code.textContent;
        code.parentNode.replaceWith(div);
        return { el: div, src: div.textContent };
      });
      function render() {
        divs.forEach(function (d) { d.el.removeAttribute("data-processed"); d.el.textContent = d.src; });
        window.mermaid.initialize({ startOnLoad: false, securityLevel: "strict", theme: effectiveTheme() === "dark" ? "dark" : "neutral" });
        window.mermaid.run({ nodes: divs.map(function (d) { return d.el; }) });
      }
      render();
      document.addEventListener("themechange", render);
    };
    document.head.appendChild(s);
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initAnchors();
    initTables();
    initMermaid();
  });
})();
