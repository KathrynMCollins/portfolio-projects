import json
from dataclasses import asdict

from .models import Finding

_ORDER = {"P1": 0, "P2": 1, "P3": 2, "n/a": 3}


def _cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def to_markdown(findings: list[Finding], *, source: str, docs: str, model: str) -> str:
    impact = sorted((f for f in findings if f.verdict.bucket == "impact"), key=lambda f: _ORDER[f.verdict.priority])
    confirm = [f for f in findings if f.verdict.bucket == "confirm"]
    none = [f for f in findings if f.verdict.bucket == "none"]
    counts = {p: sum(f.verdict.priority == p for f in impact) for p in ("P1", "P2", "P3")}
    served = sorted({f.model for f in findings if f.model and f.model != model})

    out = [
        f"# Documentation impact audit: {source}",
        "",
        f"**Verdict:** {len(impact)} changes need documentation work "
        f"({counts['P1']} P1, {counts['P2']} P2, {counts['P3']} P3). "
        f"{len(confirm)} need confirmation before they can be triaged.",
        "",
        "**Scope**",
        f"- Source: {source}",
        f"- Docs checked: {docs}",
        f"- Signals: {len(findings)} → {len(impact)} doc-impacting, {len(confirm)} needs confirmation, {len(none)} no action",
        "",
    ]
    if impact:
        out += ["## Proposed documentation changes", "",
                "| # | Change | Target page | Action | Priority | Effort |", "|:--|:--|:--|:--|:--|:--|"]
        for i, f in enumerate(impact, 1):
            pages = ", ".join(sorted({imp.page_path for imp in f.verdict.impacts})) or "[VERIFY]"
            out.append(f"| {i} | {_cell(f.signal.title)} | {pages} | {f.verdict.action} | {f.verdict.priority} | {f.verdict.effort} |")
        out.append("")
        for i, f in enumerate(impact, 1):
            out += [f"### {i}. {f.signal.title}", "", f"- **Why the docs are stale:** {f.verdict.reason}"]
            for imp in f.verdict.impacts:
                out.append(f"- **{imp.page_path} › {imp.section}:** {imp.proposed_edit}")
                if imp.stale_quote:
                    out.append(f"  - Currently says: \"{imp.stale_quote}\"")
            out.append(f"- **Evidence:** {f.signal.source} ({f.signal.id})")
            out += [f"- {flag}" for flag in f.flags]
            out.append("")
    if confirm:
        out += ["## Needs confirmation", "", "| Item | Question to answer | Why | Evidence |", "|:--|:--|:--|:--|"]
        for f in confirm:
            why = "; ".join([f.verdict.reason, *f.flags])
            out.append(f"| {_cell(f.signal.title)} | {_cell(f.verdict.question)} | {_cell(why)} | {f.signal.source} ({f.signal.id}) |")
        out.append("")
    if none:
        out += ["## No action", "", "| Item | Reason | Evidence |", "|:--|:--|:--|"]
        out += [f"| {_cell(f.signal.title)} | {_cell(f.verdict.reason)} | {f.signal.source} ({f.signal.id}) |" for f in none]
        out.append("")
    out += [
        "## Coverage and limits", "",
        f"- Model: {model}" + (f" (fallback served some items: {', '.join(served)})" if served else ""),
        "- Candidate pages were chosen by keyword overlap; the model also saw the full page index.",
        "- Every quoted passage was checked against the docs folder by script. Items marked [VERIFY] need a person.",
        "- This report proposes changes only. Nothing has been written or published.",
        "",
    ]
    return "\n".join(out)


def to_json(findings: list[Finding]) -> str:
    rows = [
        {"signal": asdict(f.signal), "verdict": f.verdict.model_dump(), "candidates": f.candidates,
         "flags": f.flags, "model": f.model}
        for f in findings
    ]
    return json.dumps(rows, indent=2)
