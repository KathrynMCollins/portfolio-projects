import csv, sys, pathlib, statistics as st
kit = pathlib.Path(sys.argv[1])
SETS = [("Main run (A/B)", "results"), ("Replication (C/D)", "results-haiku-exec"), ("Added models (E/F)", "results-added-models")]
INPUTS = ["01-caveat-dash","02-you-and-permission","03-product-name","04-legit-just","05-procedure","06-code-and-flag"]
def rd(p): return list(csv.DictReader(open(p)))
def cell(vals):
    vals=[float(v) for v in vals]
    if not vals: return "–"
    m=st.mean(vals); lo,hi=min(vals),max(vals)
    return f"{m:.1f}" if lo==hi else f"{m:.1f} ({lo:g}–{hi:g})"
out=["# All models: combined results","",
"Built from each set's `scored/drafting_runs.csv` and `scored/eval_runs.csv`. No new scoring. Sets are shown separately and are not pooled. Mean across 5 runs; a range in brackets means the runs differed. Small n: these models on these inputs, not a ranking.","",
"Run times (UTC, 2026-11-07): main run 21:22, replication 21:35, added models 21:41 (eval) and 22:21 (drafting).",""]
dr={}; ev={}
for name,folder in SETS:
    d=kit/folder/"scored"
    dr[name]=rd(d/"drafting_runs.csv"); ev[name]=rd(d/"eval_runs.csv")
def models(rows): return sorted({r["model"] for r in rows})
for title,col in [("Drafting: blockers (house scanner)","blockers"),("Drafting: substance checks lost","substance_lost"),("Drafting: warnings","warnings")]:
    out+=[f"## {title}","","| Set | Model | "+" | ".join(INPUTS)+" |","| --- | --- | "+" | ".join("---" for _ in INPUTS)+" |"]
    for name,_ in SETS:
        for m in models(dr[name]):
            rows=[r for r in dr[name] if r["model"]==m and r["ok"]=="True"]
            out.append(f"| {name} | {m} | "+" | ".join(cell([r[col] for r in rows if r["input"]==i]) for i in INPUTS)+" |")
    out.append("")
out+=["## Drafting: calls","","| Set | Model | Ok / total |","| --- | --- | --- |"]
for name,_ in SETS:
    for m in models(dr[name]):
        rows=[r for r in dr[name] if r["model"]==m]
        out.append(f"| {name} | {m} | {sum(r['ok']=='True' for r in rows)}/{len(rows)} |")
out+=["","## Evaluation (12 planted violations, 4 distractors)","","| Set | Model | Ok / total | Unparseable | Planted found | Rule number correct | Distractor hits | Runs with unplanted flags |","| --- | --- | --- | --- | --- | --- | --- | --- |"]
for name,_ in SETS:
    for m in models(ev[name]):
        rows=[r for r in ev[name] if r["model"]==m]; ok=[r for r in rows if r["ok"]=="True" and r["parsed"]=="True"]
        out.append(f"| {name} | {m} | {sum(r['ok']=='True' for r in rows)}/{len(rows)} | {sum(r['ok']=='True' and r['parsed']!='True' for r in rows)} | {cell([r['planted_found'] for r in ok])} | {cell([r['rule_number_correct'] for r in ok])} | {cell([r['distractor_hits'] for r in ok])} | {sum(bool(r['unplanted_for_review']) for r in ok)} |")
out+=["","## Not scored, reported","","- `results-added-models/aborted-20261107T214106Z/`: 1 Chat E drafting call (Fable 5.1, input 01, run 1) from a run stopped on the expected PREREGISTRATION.md hash difference.","- Chat D's eval calls were made before Chat D was paused; they are the replication's eval set above.","- Added-models hashes match the main run except PREREGISTRATION.md (dated amendments).","- Human blind scoring is pending for all three sets."]
(kit/"results-combined").mkdir(exist_ok=True)
(kit/"results-combined"/"summary.md").write_text("\n".join(out)+"\n")
print("\n".join(out))
