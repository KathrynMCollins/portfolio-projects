import json, re, sys, pathlib, csv
kit = pathlib.Path(sys.argv[1]); tmpl = pathlib.Path(sys.argv[2]).read_text(); out = pathlib.Path(sys.argv[3])
cm = kit/"results-combined"
def sheet(folder, name):
    t = (kit/folder/"scored"/"blind"/f"{name}.md").read_text()
    m = re.search(r"^## Original\n(.*?)^## Rewrite\n(.*)\Z", t, re.S | re.M); return m.group(1).strip(), m.group(2).strip()
originals, items = {}, []
def add(rid, folder, name):
    o, r = sheet(folder, name); items.append({"id": rid, "o": originals.setdefault(o, len(originals)), "r": r})
g = list(csv.DictReader(open(cm/"blind-review-map.csv")))
b = list(csv.DictReader(open(cm/"baseline-blind-review-map.csv")))
for row in b: add(row["review_id"], row["results_set"], row["blind_sheet"])
for row in g: add(row["review_id"], row["results_set"], row["blind_sheet"])
gs = [l.strip() for l in open(cm/"human-sample.csv") if l.strip() and l.strip() != "review_id"]
bs = [row["review_id"] for row in b if row["in_sample"] == "True"]
# keep each set's page order: shuffled review-ID order
views = [{"name": "Baseline sample", "ids": sorted(bs)},
         {"name": "Guided sample", "ids": sorted(gs)},
         {"name": "All baseline", "ids": sorted(bs) + sorted(r["review_id"] for r in b if r["in_sample"] != "True")},
         {"name": "All guided", "ids": sorted(gs) + sorted(r["review_id"] for r in g if r["review_id"] not in set(gs))}]
data = {"views": views, "originals": [o for o, _ in sorted(originals.items(), key=lambda x: x[1])], "items": items}
js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
out.write_text(tmpl.replace("__TITLE__", "Blind Rewrite Scoring").replace("__MAPNAME__", "the review maps").replace("__DATA__", js))
print(len(items), "items;", [(v["name"], len(v["ids"])) for v in views])
