"""Load a docs folder and pick the pages most likely to be affected by a signal.

Keyword overlap keeps the prompt small and the choice inspectable. It can miss a page that
shares no words with the change; that page is still in the index the model sees.
"""

import math
import re
from collections import Counter
from pathlib import Path

from .models import Page, Signal

_WORD = re.compile(r"[a-z0-9_]+(?:-[a-z0-9_]+)*")
_STOP = set(
    "a an and are as at be by for from has have in is it its not now of on or that the this to "
    "was were will with you your can no new use used when which".split()
)


def load_docs(root: Path) -> list[Page]:
    pages = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        title = next((l.lstrip("# ").strip() for l in text.splitlines() if l.startswith("# ")), path.stem)
        pages.append(Page(str(path.relative_to(root)), title, text))
    return pages


def _terms(text: str) -> list[str]:
    return [w for w in _WORD.findall(text.lower()) if w not in _STOP and len(w) > 2]


def rank(signal: Signal, pages: list[Page], top_k: int = 3) -> list[Page]:
    docs = [Counter(_terms(p.title + " " + p.text)) for p in pages]
    df = Counter(term for d in docs for term in d)
    query = set(_terms(signal.title + " " + signal.body))
    scored = []
    for page, counts in zip(pages, docs):
        score = sum((1 + math.log(counts[t])) * math.log(1 + len(pages) / df[t]) for t in query if counts[t])
        if score > 0:
            scored.append((score, page.path, page))
    scored.sort(key=lambda s: (-s[0], s[1]))
    return [page for _, _, page in scored[:top_k]]
