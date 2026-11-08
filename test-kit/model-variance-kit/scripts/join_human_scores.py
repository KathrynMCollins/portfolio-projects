#!/usr/bin/env python3
"""Join blind human scores to models. Usage: join_human_scores.py <scores_dir_of_json> ; writes results-combined/human_scores*.{csv,md}."""
import csv, glob, json, pathlib, sys, collections, statistics as st
KIT = pathlib.Path(__file__).resolve().parent.parent
SETS = [("results", "Main run (A/B)"), ("results-haiku-exec", "Replication (C/D)"), ("results-added-models", "Added models (E/F)")]
INPUTS = ["01-caveat-dash","02-you-and-permission","03-product-name","04-legit-just","05-procedure","06-code-and-flag"]
scores = {}
for f in glob.glob(sys.argv[1] + "/*.json"):
    d = json.load(open(f)); d = d.get("data", d); scores[pathlib.Path(f).stem] = d
mp = {r["review_id"]: (r["results_set"], r["blind_sheet"]) for r in csv.DictReader(open(KIT/"results-combined/blind-review-map.csv"))}
sample = {l.strip() for l in open(KIT/"results-combined/human-sample.csv") if l.strip() and l.strip() != "review_id"}
keys = {}
for s, _ in SETS:
    for r in csv.DictReader(open(KIT/s/"scored/blind_key.csv")): keys[(s, r["code"])] = r
rows = []
for rid, (s, sh) in sorted(mp.items()):
    v = scores.get(rid, {}); k = keys[(s, sh)]
    if not (v.get("meaning") and v.get("natural")): continue
    rows.append({"review_id": rid, "in_sample": rid in sample, "results_set": s, "blind_sheet": sh, "model": k["model"], "input": k["input"], "run": k["run"],
                 "meaning": v["meaning"], "natural": v["natural"], "note": v.get("note", "")})
out = KIT/"results-combined"
with open(out/"human_scores.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
S = [r for r in rows if r["in_sample"]]
label = dict(SETS)
def mcell(rs):
    if not rs: return "–"
    c = collections.Counter(r["meaning"] for r in rs); return "/".join(str(c.get(x, 0)) for x in ("yes","partly","no"))
def ncell(rs):
    if not rs: return "–"
    v = [int(r["natural"]) for r in rs]; return f"{st.mean(v):.1f}" if min(v)==max(v) else f"{st.mean(v):.1f} ({min(v)}–{max(v)})"
groups = sorted({(r["results_set"], r["model"]) for r in S}, key=lambda g: ([s for s,_ in SETS].index(g[0]), g[1]))
md = ["# Human blind scores (fixed sample)", "",
      f"{len(S)} sample rewrites scored blind by Kathryn Collins (2 per model, input and result set; one cell has 3). Joined to models after scoring finished. Not extrapolated: each cell describes 2 rewrites.", "",
      "Meaning cells are yes/partly/no counts. Naturalness is the mean of 1 (stilted) to 3 (natural), with the range when the rewrites differ.", "",
      "## Meaning preserved (yes/partly/no)", "", "| Set | Model | " + " | ".join(INPUTS) + " | All |", "| --- | --- | " + " | ".join("---" for _ in INPUTS) + " | --- |"]
for s, m in groups:
    g = [r for r in S if r["results_set"] == s and r["model"] == m]
    md.append(f"| {label[s]} | {m} | " + " | ".join(mcell([r for r in g if r["input"] == i]) for i in INPUTS) + f" | {mcell(g)} |")
md += ["", "## Reads naturally (1–3)", "", "| Set | Model | " + " | ".join(INPUTS) + " | All |", "| --- | --- | " + " | ".join("---" for _ in INPUTS) + " | --- |"]
for s, m in groups:
    g = [r for r in S if r["results_set"] == s and r["model"] == m]
    md.append(f"| {label[s]} | {m} | " + " | ".join(ncell([r for r in g if r["input"] == i]) for i in INPUTS) + f" | {ncell(g)} |")
md += ["", "## By input, all models", "", "| Input | Meaning yes/partly/no | Naturalness |", "| --- | --- | --- |"]
for i in INPUTS:
    g = [r for r in S if r["input"] == i]; md.append(f"| {i} | {mcell(g)} | {ncell(g)} |")
notes = [r for r in S if r["note"]]
md += ["", f"## Editor notes ({len(notes)})", ""] + [f"- {r['review_id']} · {r['model']} · {r['input']} · {label[r['results_set']]}: {r['note']}" for r in notes]
extra = [r for r in rows if not r["in_sample"]]
md += ["", f"Rewrites scored beyond the sample: {len(extra)} (reported separately, not in these tables)."]
(out/"human_scores.md").write_text("\n".join(md) + "\n")
print("\n".join(md))
