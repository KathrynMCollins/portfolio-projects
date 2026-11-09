#!/usr/bin/env python3
"""Build explorer/data.json from the model variance kit. Run from the repo root:

    python3 _tools/build_explorer_data.py

Joins every drafting rewrite to its automated scores (house scanner, substance
checks), its structure metrics and, where it was in a blind sample, the human
scores and editor note. Reads only files in test-kit/; changes nothing there.
"""
import csv, glob, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "test-kit" / "model-variance-kit"
SETS = [  # folder, id, label, condition
    ("results", "main", "Main run", "guided"),
    ("results-haiku-exec", "replication", "Replication", "guided"),
    ("results-added-models", "added", "Added models", "guided"),
    ("results-baseline", "baseline", "Baseline", "baseline"),
]
MODEL_LABELS = {
    "claude-haiku-5-5": "Haiku 5.5", "claude-sonnet-5-5": "Sonnet 5.5", "claude-opus-5-5": "Opus 5.5",
    "claude-fable-5-1": "Fable 5.1", "claude-opus-4-7": "Opus 4.7",
}
INPUT_LABELS = {
    "01-caveat-dash": "Caveat after a dash", "02-you-and-permission": "Permission sentence",
    "03-product-name": "Product name that is also a buzzword", "04-legit-just": "A “just” that carries meaning",
    "05-procedure": "Procedure", "06-code-and-flag": "Code block and review flag",
}


def strip_fences(s):
    s = s.strip()
    s = re.sub(r"^```(?:markdown|md)?\s*\n", "", s)
    return re.sub(r"\n```\s*$", "", s)


def key(model, inp, run):
    return (model, inp, str(run))


structure = {}
label_to_id = {label: sid for _, sid, label, _ in SETS}
for r in csv.DictReader(open(KIT / "results-combined" / "structure_runs.csv")):
    structure[(label_to_id[r["set"]],) + key(r["model"], r["input"], r["run"])] = r

human = {}
folder_to_id = {folder: sid for folder, sid, _, _ in SETS}
for r in csv.DictReader(open(KIT / "results-combined" / "human_scores.csv")):
    human[(folder_to_id[r["results_set"]],) + key(r["model"], r["input"], r["run"])] = r
for r in csv.DictReader(open(KIT / "results-combined" / "human_scores_baseline.csv")):
    human[("baseline",) + key(r["model"], r["input"], r["run"])] = r

rows = []
for folder, sid, label, condition in SETS:
    scored = {key(r["model"], r["input"], r["run"]): r
              for r in csv.DictReader(open(KIT / folder / "scored" / "drafting_runs.csv"))}
    for path in sorted(glob.glob(str(KIT / folder / "raw" / "drafting__*.jsonl"))):
        for line in open(path):
            rec = json.loads(line)
            if not rec.get("ok"):
                continue
            k = key(rec["model_requested"], rec["input_id"], rec["run"])
            s, st, h = scored.get(k, {}), structure.get((sid,) + k, {}), human.get((sid,) + k)
            row = {
                "set": sid, "condition": condition, "model": rec["model_requested"],
                "input": rec["input_id"], "run": rec["run"], "text": strip_fences(rec["text"]),
                "blockers": int(s.get("blockers") or 0), "warnings": int(s.get("warnings") or 0),
                "substanceLost": int(s.get("substance_lost") or 0),
                "headingsAdded": int(st.get("headings_added") or 0),
                "orderInversions": int(st.get("order_inversions") or 0),
                "wordRatio": float(st["word_ratio"]) if st.get("word_ratio") else None,
                "redacted": "portfolio_redaction" in rec,
            }
            if h:
                row["human"] = {"meaning": h["meaning"], "natural": int(h["natural"]),
                                "note": h.get("note", ""), "inSample": h.get("in_sample") == "True"}
            rows.append(row)

data = {
    "sets": [{"id": sid, "label": label, "condition": cond} for _, sid, label, cond in SETS],
    "models": [{"id": m, "label": l} for m, l in MODEL_LABELS.items()],
    "inputs": [{"id": i, "label": l, "original": (KIT / "inputs" / f"{i}.md").read_text().strip()}
               for i, l in INPUT_LABELS.items()],
    "rewrites": rows,
}
out = ROOT / "explorer" / "data.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
print(f"{len(rows)} rewrites, {sum(1 for r in rows if 'human' in r)} human-scored -> {out.relative_to(ROOT)}")
