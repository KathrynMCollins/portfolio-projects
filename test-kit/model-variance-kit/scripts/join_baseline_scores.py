#!/usr/bin/env python3
"""Join blind baseline human scores and compare with guided. Usage: join_baseline_scores.py <scores_dir_of_json>."""
import csv, glob, json, pathlib, sys, collections, statistics as st
KIT = pathlib.Path(__file__).resolve().parent.parent; CM = KIT/"results-combined"
INPUTS = ["01-caveat-dash","02-you-and-permission","03-product-name","04-legit-just","05-procedure","06-code-and-flag"]
GUIDED = {"claude-haiku-5-5": "results", "claude-sonnet-5-5": "results", "claude-opus-5-5": "results",
          "claude-fable-5-1": "results-added-models", "claude-opus-4-7": "results-added-models"}
sc = {}
for f in glob.glob(sys.argv[1] + "/*.json"):
    d = json.load(open(f)); sc[pathlib.Path(f).stem] = d.get("data", d)
key = {r["code"]: r for r in csv.DictReader(open(KIT/"results-baseline/scored/blind_key.csv"))}
rows = []
for r in csv.DictReader(open(CM/"baseline-blind-review-map.csv")):
    v = sc.get(r["review_id"], {})
    if not (v.get("meaning") and v.get("natural")): continue
    k = key[r["blind_sheet"]]
    rows.append({"review_id": r["review_id"], "in_sample": r["in_sample"] == "True", "model": k["model"], "input": k["input"], "run": k["run"],
                 "meaning": v["meaning"], "natural": v["natural"], "note": v.get("note", "")})
with open(CM/"human_scores_baseline.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
B = [r for r in rows if r["in_sample"]]
G = [r for r in csv.DictReader(open(CM/"human_scores.csv")) if r["in_sample"] == "True" and GUIDED.get(r["model"]) == r["results_set"]]
def mc(rs):
    if not rs: return "–"
    c = collections.Counter(r["meaning"] for r in rs); return "/".join(str(c.get(x, 0)) for x in ("yes", "partly", "no"))
def nc(rs):
    if not rs: return "–"
    v = [int(r["natural"]) for r in rs]; return f"{st.mean(v):.1f}"
md = ["# Human blind scores: baseline vs guided", "",
      f"Baseline: {len(B)} sample rewrites (2 per model and input), scored blind to model by Kathryn Collins. Guided: the matching cells of the guided sample (main run for Haiku, Sonnet and Opus 5.5; added-models run for Fable 5.1 and Opus 4.7), {len(G)} rewrites. Each cell is 2 rewrites per condition; not extrapolated. Meaning is yes/partly/no counts; naturalness is the mean of 1 to 3.", "",
      "## By input, all five models (guided → baseline)", "", "| Input | Meaning | Naturalness |", "| --- | --- | --- |"]
for i in INPUTS:
    g = [r for r in G if r["input"] == i]; b = [r for r in B if r["input"] == i]
    md.append(f"| {i} | {mc(g)} → {mc(b)} | {nc(g)} → {nc(b)} |")
md.append(f"| All | {mc(G)} → {mc(B)} | {nc(G)} → {nc(B)} |")
md += ["", "## Meaning by model and input (guided → baseline)", "", "| Model | " + " | ".join(INPUTS) + " | All |", "| --- | " + " | ".join("---" for _ in INPUTS) + " | --- |"]
for m in GUIDED:
    gm = [r for r in G if r["model"] == m]; bm = [r for r in B if r["model"] == m]
    md.append(f"| {m} | " + " | ".join(f"{mc([r for r in gm if r['input']==i])} → {mc([r for r in bm if r['input']==i])}" for i in INPUTS) + f" | {mc(gm)} → {mc(bm)} |")
md += ["", "## Naturalness by model and input (guided → baseline)", "", "| Model | " + " | ".join(INPUTS) + " | All |", "| --- | " + " | ".join("---" for _ in INPUTS) + " | --- |"]
for m in GUIDED:
    gm = [r for r in G if r["model"] == m]; bm = [r for r in B if r["model"] == m]
    md.append(f"| {m} | " + " | ".join(f"{nc([r for r in gm if r['input']==i])} → {nc([r for r in bm if r['input']==i])}" for i in INPUTS) + f" | {nc(gm)} → {nc(bm)} |")
d02 = mc([r for r in G if r["input"] == INPUTS[1]]) != mc([r for r in B if r["input"] == INPUTS[1]])
d03 = mc([r for r in G if r["input"] == INPUTS[2]]) != mc([r for r in B if r["input"] == INPUTS[2]])
md += ["", "## HB4", "",
       f"HB4 (human meaning-preserved counts differ between baseline and guided on input 02 or 03): {'supported' if (d02 or d03) else 'not supported'}. Input 02 differs: {'yes' if d02 else 'no'}; input 03 differs: {'yes' if d03 else 'no'}. The pre-registration did not set a size for \"differ\", so any difference in counts meets it; with 10 rewrites per input per condition, small differences are within what two runs per cell can show by chance.", "",
       f"## Baseline editor notes ({sum(1 for r in B if r['note'])})", ""] + [f"- {r['review_id']} · {r['model']} · {r['input']}: {r['note']}" for r in B if r["note"]]
(CM/"human_scores_baseline.md").write_text("\n".join(md) + "\n")
print("\n".join(md))
