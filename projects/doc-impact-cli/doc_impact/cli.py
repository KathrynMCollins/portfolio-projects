import argparse
import sys
from pathlib import Path

import anthropic

from . import audit, harvest, report, retrieve, verify


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="doc-impact", description="Find the docs a set of product changes makes stale.")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--changes", type=Path, help="Markdown changelog or release notes; each bullet is one change.")
    src.add_argument("--git", type=Path, metavar="REPO", help="A local git repository; use with --range.")
    p.add_argument("--range", dest="rev_range", help="Commit range for --git, for example v2.3.0..v2.4.0.")
    p.add_argument("--docs", type=Path, required=True, help="Folder of Markdown docs to check against.")
    p.add_argument("--out", type=Path, help="Write the Markdown report here (default: print it).")
    p.add_argument("--json", type=Path, help="Also write machine-readable findings here.")
    p.add_argument("--model", default=audit.DEFAULT_MODEL)
    p.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--top-k", type=int, default=3, help="Candidate pages sent with each change (default 3).")
    p.add_argument("--dry-run", action="store_true", help="Show changes and candidate pages; make no API calls.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.git and not args.rev_range:
        _parser().error("--git needs --range")
    if not args.docs.is_dir():
        _parser().error(f"--docs {args.docs} is not a folder")

    signals = harvest.from_git(args.git, args.rev_range) if args.git else harvest.from_changelog(args.changes)
    pages = retrieve.load_docs(args.docs)
    source = f"{args.git} {args.rev_range}" if args.git else args.changes.name
    if not signals:
        print("No changes found in the source.", file=sys.stderr)
        return 1
    if not pages:
        print(f"No .md files under {args.docs}.", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"{len(signals)} changes, {len(pages)} pages. No API calls made.\n")
        for s in signals:
            cands = ", ".join(p.path for p in retrieve.rank(s, pages, args.top_k)) or "(none)"
            print(f"{s.id}  {s.title}\n    candidates: {cands}")
        return 0

    log = lambda msg: print(msg, file=sys.stderr)
    try:
        findings = audit.run(signals, pages, model=args.model, effort=args.effort, top_k=args.top_k, progress=log)
    except anthropic.AuthenticationError:
        log("Authentication failed. Set ANTHROPIC_API_KEY, or run with --dry-run to try it without a key.")
        return 2
    except anthropic.APIStatusError as e:
        log(f"API error {e.status_code}: {e.message}")
        return 2
    except anthropic.APIConnectionError:
        log("Could not reach the Claude API. Check your network and try again.")
        return 2

    verify.verify(findings, pages)
    md = report.to_markdown(findings, source=source, docs=str(args.docs), model=args.model)
    if args.out:
        args.out.write_text(md, encoding="utf-8")
        log(f"Report written to {args.out}")
    else:
        print(md)
    if args.json:
        args.json.write_text(report.to_json(findings), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
