#!/usr/bin/env python3
"""Scan a BigPanda doc draft for AI-tone artifacts.

Usage:
    python3 scripts/check_ai_tone.py draft.md
    cat draft.md | python3 scripts/check_ai_tone.py -

Checks the countable tells defined in references/anti-ai-tone.md:
  1. Em/en dashes in prose
  2. Second-person density and "you" inside procedure steps
  3. Buzzwords and marketing phrases
  4. Repeated sentence/bullet openers

Code blocks, inline code, URLs, and content flags ([VERIFY] etc.) are
excluded from scanning so real technical strings aren't flagged.

Exit code 0 = clean, 1 = findings to resolve.
"""

import re
import sys

# Capitalized product names whose lowercase form is a buzzword. "Harness" the
# feature-flag service is fine; "harness the power of" is not.
PRODUCT_NAME_COLLISIONS = {"harness", "harnesses"}

BUZZWORDS = [
    "leverage", "leverages", "leveraging", "utilize", "utilizes", "utilizing",
    "seamless", "seamlessly", "robust", "powerful", "comprehensive", "holistic",
    "streamline", "streamlines", "streamlining", "empower", "empowers",
    "empowering", "unlock", "unlocks", "unlocking", "harness", "harnesses",
    "elevate", "elevates", "supercharge", "supercharges", "revolutionize",
    "revolutionizes", "cutting-edge", "state-of-the-art", "game-changing",
    "best-in-class", "world-class", "next-generation", "delve", "delves",
    "delving", "crucial", "vital", "significantly", "dramatically",
    "effortlessly", "easily", "intuitive", "myriad",
    "plethora", "realm", "synergy", "unparalleled", "paradigm", "ecosystem",
    "landscape", "journey", "foster", "fosters", "facilitate", "facilitates",
]

# Warn-only: frequently correct in real technical prose. Flagged for a
# judgment call, never blocking.
SOFT_WORDS = ["simply", "just", "ensure", "ensures", "ensuring"]

PHRASES = [
    r"in today'?s [a-z\- ]*(world|environment|landscape|era)",
    r"it'?s (important|worth) (to )?not(e|ing) that",
    r"whether you'?re an? ",
    r"not only .{0,60}? but also",
    r"isn'?t just .{0,40}?,? it'?s",
    r"it'?s not about .{0,40}?\.? it'?s about",
    r"by following these steps",
    r"in conclusion",
    r"to summarize",
    r"let'?s (take a look|explore|dive)",
    r"dive into",
    r"as (mentioned|discussed) (above|previously|earlier)",
    r"at its core",
    r"under the hood",
    r"navigate the complexit",
    r"the key is",
    r"actionable insights",
    r"single pane of glass",
    r"is designed to",
    r"helps? you to",
    r"can be used to",
    r"serves as a",
    r"acts as a",
    r"why does this matter",
]

SECOND_PERSON = re.compile(r"\byou(?:'ll|'re|'ve|'d|r|rs)?\b", re.I)
YOU_CAN = re.compile(r"\byou (can|will|may|might|should|could|are able to)\b", re.I)


def strip_noise(text):
    """Blank out code, URLs, and flags while preserving line numbering."""
    lines = text.split("\n")
    out, in_fence = [], False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence or re.match(r"^(\s{4,}|\t)\S", line):
            out.append("")
            continue
        line = re.sub(r"`[^`]*`", " ", line)                 # inline code
        line = re.sub(r"\]\([^)]*\)", "] ", line)            # md link targets
        line = re.sub(r'href="[^"]*"', " ", line)            # html hrefs
        line = re.sub(r"https?://\S+", " ", line)            # bare URLs
        line = re.sub(r"\[[A-Z\-]+\??\]", " ", line)         # [VERIFY] etc.
        line = re.sub(r"^\s*\|?\s*:?-{2,}:?\s*(\|.*)?$", "", line)  # table rules
        out.append(line)
    return out


def sentences(line):
    body = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", line)
    body = body.lstrip("*_ ")  # bold/italic label markers aren't the opener
    return [s.strip() for s in re.split(r"(?<=[.:!?])\s+", body) if s.strip()]


_CLAUSE_VERB = re.compile(r"^\s*(?:the|this|that|it|they|you|we|which|a|an|each|every|all|no)?\s*"
                          r"[\w`'\"-]+\s+(?:is|are|was|were|has|have|had|does|do|did|can|will|"
                          r"runs?|applies|sees?|uses?|sends?|returns?|shows?|creates?|"
                          r"flags?|becomes?|remains?|takes?|stays?|starts?|stops?)\b", re.I)
_LIST_AFTER = re.compile(r"^\s*(?:[`\w-]+\s*(?:,|and|or)\s*)+[`\w-]+\s*[.;]?\s*$")
_STEP_LINE = re.compile(r"^\s*(?:\d+\.|[-*])\s+")
_IMPERATIVE_BEFORE = re.compile(r"\b(?:click|select|open|save|enter|go to|run|set|choose|type|"
                                r"navigate|apply|enable|disable|add|remove|delete)\b", re.I)


def dash_hint(line, pos):
    """Classify what a dash is joining and suggest the grammatical replacement.

    Mirrors the decision table in references/style-core.md. A hint, not a verdict.
    """
    before, after = line[:pos], line[pos + 1:]
    # paired dashes → aside
    if re.search(r"[—–]", after):
        return "aside: commas/parentheses, or cut"
    if (_LIST_AFTER.match(after)
            or re.match(r"\s*(?:for example|e\.g\.|such as|including)\b", after, re.I)
            or (len(after.split()) <= 8 and re.search(r"\b(?:and|or)\b|,", after)
                and not _CLAUSE_VERB.match(after))):
        return "introduces list/example: colon"
    if _CLAUSE_VERB.match(after):
        if _STEP_LINE.match(line) or _IMPERATIVE_BEFORE.search(before[-60:]):
            return "clause after procedural text: period (new sentence)"
        return "second clause, same thought: semicolon (or period)"
    if re.match(r"\s*\d", after) or len(after.split()) <= 3:
        return "appositive/short rename: comma"
    return "colon if it explains, period if it shifts"


def check(text):
    lines = strip_noise(text)
    findings = {"dashes": [], "you_in_step": [], "you_density": [],
                "buzzwords": [], "phrases": [], "openers": [],
                "soft_words": []}

    para, para_start = [], 0
    openers = []

    for i, line in enumerate(lines, 1):
        raw = line.strip()

        for m in re.finditer(r"[—–]", line):
            findings["dashes"].append((i, f"col {m.start() + 1} → {dash_hint(line, m.start())}",
                                       line.strip()[:90]))

        is_step = bool(re.match(r"^\s*\d+\.\s+", line))
        if is_step and SECOND_PERSON.search(line):
            findings["you_in_step"].append((i, raw[:90]))

        for m in YOU_CAN.finditer(line):
            findings["you_density"].append((i, m.group(0), raw[:90]))

        low = line.lower()
        for w in BUZZWORDS:
            # Product names that collide with buzzwords: skip the capitalized form only.
            if w in PRODUCT_NAME_COLLISIONS and not re.search(r"\b" + w + r"\b", line):
                continue
            for m in re.finditer(r"\b" + re.escape(w) + r"\b", low):
                findings["buzzwords"].append((i, w, raw[:90]))
        for w in SOFT_WORDS:
            for m in re.finditer(r"\b" + re.escape(w) + r"\b", low):
                findings["soft_words"].append((i, w, raw[:90]))
        for p in PHRASES:
            m = re.search(p, low)
            if m:
                findings["phrases"].append((i, m.group(0), raw[:90]))

        # paragraph-level "you" density
        if raw:
            if not para:
                para_start = i
            para.append(line)
        else:
            if para:
                blob = " ".join(para)
                n = len(SECOND_PERSON.findall(blob))
                if n > 1 and not blob.lstrip().startswith(("|", "#")):
                    findings["you_density"].append(
                        (para_start, f"{n} second-person refs in paragraph", ""))
                para = []

        # repeated openers across consecutive lines/sentences
        first = None
        if raw.startswith(("<", "|", "#", ">")):
            openers = []
            continue
        for s in sentences(line):
            first = s.split()[0].lower().strip(",.:;") if s.split() else None
            break
        if first and len(first) > 1:
            if openers and openers[-1][1] == first:
                openers.append((i, first))
            else:
                openers = [(i, first)]
            if len(openers) >= 3:
                for ln, w in (openers if len(openers) == 3 else openers[-1:]):
                    findings["openers"].append(
                        (ln, f'3+ lines start with "{w}"', ""))
        else:
            openers = []

    if para:
        blob = " ".join(para)
        n = len(SECOND_PERSON.findall(blob))
        if n > 1:
            findings["you_density"].append(
                (para_start, f"{n} second-person refs in paragraph", ""))
    return findings


LABELS = {
    "dashes": "Em/en dashes in prose (target: 0)",
    "buzzwords": "Buzzwords and filler adverbs",
    "phrases": "AI-tell phrases and hedged capability verbs",
    "openers": "Repeated sentence openers",
    "you_in_step": '"you" inside a numbered procedure step',
    "you_density": 'Second-person density ("you can/will/may", >1 per paragraph)',
    "soft_words": '"simply" / "just" / "ensure" (often legitimate)',
}

BLOCKERS = ["dashes", "buzzwords", "phrases", "openers"]
WARNINGS = ["you_in_step", "you_density", "soft_words"]


def report(f, keys):
    total = 0
    for key in keys:
        items = f[key]
        total += len(items)
        print(f"\n{LABELS[key]}: {len(items)}")
        seen = set()
        for item in items[:25]:
            line_no, term = item[0], item[1]
            ctx = item[2] if len(item) > 2 else ""
            if (line_no, term) in seen:
                continue
            seen.add((line_no, term))
            print(f"  L{line_no}: {term}" + (f"  |  {ctx}" if ctx else ""))
        if len(items) > 25:
            print(f"  ... and {len(items) - 25} more")
    return total


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = sys.stdin.read() if sys.argv[1] == "-" else open(
        sys.argv[1], encoding="utf-8").read()

    f = check(src)

    print(f"AI-tone check: {sys.argv[1]}")
    print("=" * 60)
    print("\nBLOCKERS (fix before delivering)")
    print("-" * 60)
    blocking = report(f, BLOCKERS)

    print("\n\nWARNINGS (judgment call, do not block delivery)")
    print("-" * 60)
    warning = report(f, WARNINGS)

    print("\n" + "=" * 60)
    if blocking == 0:
        print(f"PASS. 0 blockers, {warning} warnings.")
    else:
        print(f"FAIL. {blocking} blockers, {warning} warnings.")
    print("Rules: references/anti-ai-tone.md")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
