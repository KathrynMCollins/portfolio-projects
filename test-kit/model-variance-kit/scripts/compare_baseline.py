#!/usr/bin/env python3
"""Baseline vs guided, from scored CSVs only (no rescoring). Writes results-combined/baseline-vs-guided.md."""
import csv, pathlib, statistics as st
KIT = pathlib.Path(__file__).resolve().parent.parent
INPUTS = ["01-caveat-dash","02-you-and-permission","03-product-name","04-legit-just","05-procedure","06-code-and-flag"]
GUIDED = {"claude-haiku-5-5": "results", "claude-sonnet-5-5": "results", "claude-opus-5-5": "results",
          "claude-fable-5-1": "results-added-models", "claude-opus-4-7": "results-added-models"}
def rd(folder, f): return list(csv.DictReader(open(KIT/folder/"scored"/f)))
gd = {f: rd(f, "drafting_runs.csv") for f in set(GUIDED.values())}; ge = {f: rd(f, "eval_runs.csv") for f in set(GUIDED.values())}
bd = rd("results-baseline", "drafting_runs.csv"); be = rd("results-baseline", "eval_runs.csv")
def vals(rows, m, i, col): return [float(r[col]) for r in rows if r["model"] == m and r["input"] == i and r["ok"] == "True"]
def cell(v):
    if not v: return "–"
    m = st.mean(v); return f"{m:.1f}" if min(v) == max(v) else f"{m:.1f} ({min(v):g}–{max(v):g})"
out = ["# Baseline (no standard) vs guided", "",
       "From each set's scored CSVs; nothing re-scored. Guided = results/ for Haiku, Sonnet and Opus 5.5 and results-added-models/ for Fable 5.1 and Opus 4.7, per PREREGISTRATION-baseline.md. Each cell: guided → baseline, mean of 5 runs, range when runs differ. These models on these inputs; not a ranking.", ""]
hb = {}
for col, title in [("blockers", "Scanner blockers"), ("warnings", "Scanner warnings"), ("substance_lost", "Substance checks lost")]:
    out += [f"## {title} (guided → baseline)", "", "| Model | " + " | ".join(INPUTS) + " |", "| --- | " + " | ".join("---" for _ in INPUTS) + " |"]
    for m, g in GUIDED.items():
        cells = []
        for i in INPUTS:
            a, b = vals(gd[g], m, i, col), vals(bd, m, i, col); cells.append(f"{cell(a)} → {cell(b)}")
            hb.setdefault((col, m), []).append((st.mean(a) if a else None, st.mean(b) if b else None))
        out.append(f"| {m} | " + " | ".join(cells) + " |")
    out.append("")
out += ["## Evaluation (guided → baseline)", "", "| Model | Planted found (of 12) | Distractor hits (of 4) | Runs with unplanted flags |", "| --- | --- | --- | --- |"]
ev = {}
for m, g in GUIDED.items():
    def ec(rows, col): return [float(r[col]) for r in rows if r["model"] == m and r["ok"] == "True" and r["parsed"] == "True"]
    def un(rows): return sum(1 for r in rows if r["model"] == m and r["ok"] == "True" and r["unplanted_for_review"])
    ev[m] = ec(be, "distractor_hits")
    out.append(f"| {m} | {cell(ec(ge[g],'planted_found'))} → {cell(ec(be,'planted_found'))} | {cell(ec(ge[g],'distractor_hits'))} → {cell(ec(be,'distractor_hits'))} | {un(ge[g])} → {un(be)} |")
out += ["", "## Pre-registered hypotheses (automated part)", ""]
hb1 = {m: sum(1 for a, b in hb[("blockers", m)] if a is not None and b is not None and b > a) for m in GUIDED}
out.append(f"- HB1 (baseline has more blockers on at least 4 of 6 inputs, every model): {'supported' if all(v >= 4 for v in hb1.values()) else 'not supported'}. Inputs with more blockers per model: " + ", ".join(f"{m} {v}/6" for m, v in hb1.items()) + ".")
hb2 = {m: (sum(b for a, b in hb[("substance_lost", m)]), sum(a for a, b in hb[("substance_lost", m)])) for m in GUIDED}
out.append(f"- HB2 (baseline loses at least as many substance checks as guided, every model): {'supported' if all(b >= a for b, a in hb2.values()) else 'not supported'}. Sum of per-input means, baseline vs guided: " + ", ".join(f"{m} {b:.1f} vs {a:.1f}" for m, (b, a) in hb2.items()) + ".")
out.append(f"- HB3 (at least one model flags a distractor in at least one baseline run): {'supported' if any(any(v > 0 for v in vs) for vs in ev.values()) else 'not supported'}.")
out.append("- HB4 (human meaning scores differ on input 02 or 03): see results-combined/human_scores_baseline.md." if (KIT/"results-combined"/"human_scores_baseline.md").exists() else "- HB4 (human meaning scores differ on input 02 or 03): pending the blind baseline sample.")
out += ["", "## Caveats", "",
        "- Baseline evaluation has no rule numbers, so a quote is matched to planted items and distractors by text only. The overlapping-match-string quirk (results-combined/notes-for-write-up.md) can credit a planted item or a distractor to a quote flagged for another reason. Distractor hits here need the same human review as unplanted flags.",
        "- Baseline runs were made on 2026-11-08, a day after the guided runs.",
        "- Scanner and substance checks measure the baseline against a standard it never saw; that is the design, not a fault in the baseline."]
(KIT/"results-combined"/"baseline-vs-guided.md").write_text("\n".join(out) + "\n")
print("\n".join(out))
