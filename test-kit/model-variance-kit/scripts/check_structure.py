#!/usr/bin/env python3
"""Structure check: how a rewrite changes the shape of the original passage.

Deterministic, no model calls. Exploratory: not one of the pre-registered metrics for the runs
already made; a future pre-registration can adopt it. Code blocks are ignored.

Per rewrite, against its original:
  headings_added     markdown headings in the rewrite minus the original
  bold_added         bold spans in the rewrite minus the original
  list_items_added   list items (bulleted or numbered) minus the original
  callouts_added     blockquote/callout blocks minus the original
  micro_paragraphs   prose paragraphs under 8 words in the rewrite
  order_inversions   pairs of original sentences whose order is swapped in the rewrite
  sentences_unmatched original sentences with no close match in the rewrite (reworded or dropped)
  word_ratio         rewrite words / original words

Usage:
  check_structure.py                       all result sets -> results-combined/structure_runs.csv, structure.md
  check_structure.py ORIGINAL REWRITE      one pair of files, printed as JSON
"""
import csv, glob, json, pathlib, re, statistics as st, sys

KIT = pathlib.Path(__file__).resolve().parent.parent
CODE = re.compile(r"```.*?```", re.S)
STOP = set("a an the to of and or in on for with is are be it its this that you your can if when at by from as do not".split())


def prose(md):
    return CODE.sub("", md)


def blocks(md):
    return [b.strip() for b in re.split(r"\n\s*\n", prose(md)) if b.strip()]


def plain(s):
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"[*_#>\[\]()]", " ", s)
    return re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", " ", s, flags=re.M)


def sentences(md):
    out = []
    for line in prose(md).splitlines():
        line = line.strip()
        if not line or re.match(r"^#{1,6}\s", line):
            continue
        out += [x.strip() for x in re.split(r"(?<=[.!?:])\s+", plain(line)) if len(x.split()) >= 3]
    return out


def words(s):
    return {w for w in re.findall(r"[a-z0-9']+", s.lower()) if w not in STOP}


def measure(orig, rew):
    def count(pat, md):
        return len(re.findall(pat, prose(md), re.M))
    h = r"^#{1,6}\s"
    li = r"^\s*(?:[-*+]|\d+\.)\s+"
    co = r"^>\s?"
    out = {
        "headings_added": max(0, count(h, rew) - count(h, orig)),
        "bold_added": max(0, len(re.findall(r"\*\*[^*]+\*\*", prose(rew))) - len(re.findall(r"\*\*[^*]+\*\*", prose(orig)))),
        "list_items_added": max(0, count(li, rew) - count(li, orig)),
        "callouts_added": max(0, sum(1 for b in blocks(rew) if b.startswith(">")) - sum(1 for b in blocks(orig) if b.startswith(">"))),
        "micro_paragraphs": sum(1 for b in blocks(rew) if not re.match(r"^(#|>|\s*(?:[-*+]|\d+\.)\s)", b) and len(plain(b).split()) < 8),
    }
    os_, rs = sentences(orig), sentences(rew)
    pos, unmatched = [], 0
    for s in os_:
        ws = words(s)
        best, bi = 0.0, None
        for j, r in enumerate(rs):
            wr = words(r)
            if ws and wr:
                sc = len(ws & wr) / len(ws | wr)
                if sc > best:
                    best, bi = sc, j
        if best >= 0.3:
            pos.append(bi)
        else:
            unmatched += 1
    out["order_inversions"] = sum(1 for i in range(len(pos)) for j in range(i + 1, len(pos)) if pos[i] > pos[j])
    out["sentences_unmatched"] = unmatched
    ow, rw = len(plain(prose(orig)).split()), len(plain(prose(rew)).split())
    out["word_ratio"] = round(rw / ow, 2) if ow else None
    return out


def strip_fences(s):
    s = s.strip()
    s = re.sub(r"^```(?:markdown|md)?\s*\n", "", s)
    return re.sub(r"\n```\s*$", "", s)


SETS = [("results", "Main run"), ("results-haiku-exec", "Replication"), ("results-added-models", "Added models"), ("results-baseline", "Baseline")]
METRICS = ["headings_added", "bold_added", "list_items_added", "callouts_added", "micro_paragraphs", "order_inversions", "sentences_unmatched", "word_ratio"]
INPUTS = ["01-caveat-dash", "02-you-and-permission", "03-product-name", "04-legit-just", "05-procedure", "06-code-and-flag"]


def run_all():
    rows = []
    for folder, label in SETS:
        for p in sorted(glob.glob(str(KIT / folder / "raw" / "drafting__*.jsonl"))):
            for line in open(p):
                r = json.loads(line)
                if not r.get("ok"):
                    continue
                orig = (KIT / "inputs" / f"{r['input_id']}.md").read_text()
                rows.append({"set": label, "model": r["model_requested"], "input": r["input_id"], "run": r["run"],
                             **measure(orig, strip_fences(r["text"]))})
    cm = KIT / "results-combined"
    with open(cm / "structure_runs.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

    def mean(rs, k):
        v = [x[k] for x in rs if x[k] is not None]
        return f"{st.mean(v):.1f}" if v else "–"
    md = ["# Structure check (exploratory)", "",
          "Deterministic, from raw drafting outputs; see scripts/check_structure.py for definitions. Not a pre-registered metric for these runs. Mean per rewrite across 5 runs.", ""]
    md += ["## By set and model (all inputs)", "", "| Set | Model | " + " | ".join(METRICS) + " |", "| --- | --- | " + " | ".join("---" for _ in METRICS) + " |"]
    for _, label in SETS:
        for m in sorted({x["model"] for x in rows if x["set"] == label}):
            g = [x for x in rows if x["set"] == label and x["model"] == m]
            md.append(f"| {label} | {m} | " + " | ".join(mean(g, k) for k in METRICS) + " |")
    for k in ["headings_added", "order_inversions"]:
        md += ["", f"## {k} by input (main/added guided → baseline)", "", "| Model | " + " | ".join(INPUTS) + " |", "| --- | " + " | ".join("---" for _ in INPUTS) + " |"]
        guided = {"claude-fable-5-1": "Added models", "claude-opus-4-7": "Added models"}
        for m in ["claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5", "claude-fable-5-1", "claude-opus-4-7"]:
            gs = guided.get(m, "Main run")
            md.append(f"| {m} | " + " | ".join(
                f"{mean([x for x in rows if x['set']==gs and x['model']==m and x['input']==i], k)} → {mean([x for x in rows if x['set']=='Baseline' and x['model']==m and x['input']==i], k)}"
                for i in INPUTS) + " |")
    (cm / "structure.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(json.dumps(measure(open(sys.argv[1]).read(), open(sys.argv[2]).read()), indent=2))
    else:
        run_all()
