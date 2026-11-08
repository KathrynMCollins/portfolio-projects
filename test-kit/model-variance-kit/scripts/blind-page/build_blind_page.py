import json, random, re, sys, pathlib, csv
kit = pathlib.Path(sys.argv[1]); tmpl = pathlib.Path(sys.argv[2]).read_text(); out = pathlib.Path(sys.argv[3])
sets = ["results", "results-haiku-exec", "results-added-models"]
items, originals = [], {}
for s in sets:
    for f in sorted((kit/s/"scored"/"blind").glob("S*.md")):
        t = f.read_text()
        m = re.search(r"^## Original\n(.*?)^## Rewrite\n(.*)\Z", t, re.S | re.M)
        orig, rew = m.group(1).strip(), m.group(2).strip()
        oi = originals.setdefault(orig, len(originals))
        items.append({"set": s, "sheet": f.stem, "o": oi, "r": rew})
rng = random.Random(20261107)
rng.shuffle(items)
rows = []
for i, it in enumerate(items, 1):
    it["id"] = f"R{i:03d}"; rows.append((it["id"], it["set"], it["sheet"]))
# Optional fixed human-scoring sample: shown first, IDs unchanged.
sample = set(json.load(open(sys.argv[4]))) if len(sys.argv) > 4 else set()
items = [it for it in items if it["id"] in sample] + [it for it in items if it["id"] not in sample]
with open(kit/"results-combined"/"blind-review-map.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["review_id", "results_set", "blind_sheet"]); w.writerows(rows)
data = {"sampleSize": len(sample), "originals": [o for o, _ in sorted(originals.items(), key=lambda x: x[1])],
        "items": [{"id": it["id"], "o": it["o"], "r": it["r"]} for it in items]}
js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
out.write_text(tmpl.replace("__TITLE__", "Blind Rewrite Scoring").replace("__MAPNAME__", "blind-review-map.csv").replace("__SAMPLEDESC__", "two per model, input and result set").replace("__DATA__", js))
print(len(items), "items,", len(originals), "originals")
