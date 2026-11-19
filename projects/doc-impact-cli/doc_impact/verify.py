"""Check every citation the model made against the docs. Deterministic: no model calls.

A quote that cannot be found is the cheapest hallucination to catch, so it is caught here
rather than by a reviewer. Impact items whose evidence all fails are moved to confirm.
"""

import re

from .models import Finding, Page


def _norm(text: str) -> str:
    text = re.sub(r"[`*_]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def verify(findings: list[Finding], pages: list[Page]) -> list[Finding]:
    by_path = {p.path: _norm(p.text) for p in pages}
    for f in findings:
        v = f.verdict
        if v.bucket != "impact":
            continue
        if not v.impacts:
            f.flags.append("[VERIFY] Impact with no page named.")
        verified = 0
        for imp in v.impacts:
            if v.action == "new_page" and not imp.stale_quote:
                verified += 1
                continue
            if imp.page_path not in by_path:
                f.flags.append(f"[VERIFY] {imp.page_path} is not in the docs folder.")
            elif not imp.stale_quote:
                f.flags.append(f"[VERIFY] No quote given for {imp.page_path}.")
            elif _norm(imp.stale_quote) not in by_path[imp.page_path]:
                f.flags.append(f"[VERIFY] Quote not found in {imp.page_path}: \"{imp.stale_quote[:80]}\"")
            else:
                verified += 1
        if v.impacts and verified == 0:
            v.bucket = "confirm"
            v.question = v.question or "The cited evidence did not check out. Is this page actually stale?"
            f.flags.append("Moved from impact to confirm: no citation could be verified.")
    return findings
