import json, random, re, sys, pathlib, csv, collections
kit = pathlib.Path(sys.argv[1]); tmpl = pathlib.Path(sys.argv[2]).read_text(); out = pathlib.Path(sys.argv[3])
folder = kit/"results-baseline"/"scored"
key = {r["code"]: r for r in csv.DictReader(open(folder/"blind_key.csv"))}
items, originals = [], {}
for f in sorted((folder/"blind").glob("S*.md")):
    t = f.read_text(); m = re.search(r"^## Original\n(.*?)^## Rewrite\n(.*)\Z", t, re.S | re.M)
    orig, rew = m.group(1).strip(), m.group(2).strip()
    items.append({"sheet": f.stem, "o": originals.setdefault(orig, len(originals)), "r": rew})
rng = random.Random(20261108); rng.shuffle(items)
for i, it in enumerate(items, 1): it["id"] = f"B{i:03d}"
cells = collections.defaultdict(list)
for it in sorted(items, key=lambda x: x["id"]):
    k = key[it["sheet"]]; cells[(k["model"], k["input"])].append(it["id"])
srng = random.Random(20261108); sample = set()
for c in sorted(cells):
    ids = cells[c][:]; srng.shuffle(ids); sample.update(ids[:2])
items = [it for it in items if it["id"] in sample] + [it for it in items if it["id"] not in sample]
cm = kit/"results-combined"
with open(cm/"baseline-blind-review-map.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["review_id", "results_set", "blind_sheet", "in_sample"])
    for it in sorted(items, key=lambda x: x["id"]): w.writerow([it["id"], "results-baseline", it["sheet"], it["id"] in sample])
data = {"sampleSize": len(sample), "originals": [o for o, _ in sorted(originals.items(), key=lambda x: x[1])],
        "items": [{"id": it["id"], "o": it["o"], "r": it["r"]} for it in items]}
js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
out.write_text(tmpl.replace("__TITLE__", "Baseline Rewrite Scoring").replace("__MAPNAME__", "baseline-blind-review-map.csv").replace("__SAMPLEDESC__", "two per model and input").replace("__DATA__", js))
print(len(items), "items,", len(sample), "in sample,", len(cells), "cells")
