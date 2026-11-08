#!/usr/bin/env python3
"""Run the model-variance test and log every call.

Usage:
  python3 scripts/run.py --task drafting --models claude-haiku-5-5 claude-sonnet-5-5 claude-opus-5-5
  python3 scripts/run.py --task eval --models claude-sonnet-5-5 --runs 5
  python3 scripts/run.py --task drafting --models fake --dry-run      # no API calls

Every call, including failures, is appended to results/raw/<task>__<model>__<timestamp>.jsonl.
Nothing is filtered or retried silently. Re-running never overwrites earlier files.
Default runner is Claude Code headless (`claude -p`, the user's own login).
--runner api uses the Anthropic SDK and needs ANTHROPIC_API_KEY.
"""
import argparse, datetime as dt, hashlib, json, os, pathlib, re, subprocess, sys, tempfile, time

KIT = pathlib.Path(__file__).resolve().parent.parent
def frozen(prompts, prereg):
    return [f"{prompts}/system.md", f"{prompts}/drafting_user.md", f"{prompts}/eval_user.md",
            "eval/planted_draft.md", "eval/answer_key.json", "inputs/checks.json",
            prereg] + sorted(f"inputs/{p.name}" for p in (KIT / "inputs").glob("*.md"))


def sha(path):
    return hashlib.sha256((KIT / path).read_bytes()).hexdigest()[:16]


def preflight(dry, results, prompts, prereg_name):
    prereg = (KIT / prereg_name).read_text()
    m = re.search(r"^Locked on:\s*(\S.*)$", prereg, re.M)
    if not m or "YYYY" in m.group(1):
        if not dry:
            sys.exit(f"{prereg_name} is not locked. Fill in 'Locked on:' and commit it before any real run.")
    hashes = {p: sha(p) for p in frozen(prompts, prereg_name)}
    lock = results / "kit_hashes.json"
    if lock.exists():
        old = json.loads(lock.read_text())
        changed = [p for p in hashes if old.get(p) != hashes[p]]
        if changed and not dry:
            sys.exit(f"Frozen kit files changed since the first run: {changed}. "
                     "Revert them, or start a new results folder and say so in the write-up.")
    elif not dry:
        lock.parent.mkdir(parents=True, exist_ok=True)
        lock.write_text(json.dumps(hashes, indent=2))
    return hashes


def jobs(task, prompts):
    if task == "drafting":
        tmpl = (KIT / prompts / "drafting_user.md").read_text()
        for p in sorted((KIT / "inputs").glob("*.md")):
            yield p.stem, tmpl.replace("{passage}", p.read_text().strip())
    else:
        tmpl = (KIT / prompts / "eval_user.md").read_text()
        yield "planted_draft", tmpl.replace("{draft}", (KIT / "eval/planted_draft.md").read_text().strip())


def call(client, model, system, user, max_tokens):
    for attempt in range(4):
        try:
            r = client.messages.create(model=model, max_tokens=max_tokens, system=system,
                                       messages=[{"role": "user", "content": user}])
            text = "".join(b.text for b in r.content if getattr(b, "type", "") == "text")
            return {"ok": True, "text": text, "model_returned": r.model, "stop_reason": r.stop_reason,
                    "usage": {"input_tokens": r.usage.input_tokens, "output_tokens": r.usage.output_tokens},
                    "attempts": attempt + 1}
        except Exception as e:  # logged, never dropped
            err = f"{type(e).__name__}: {e}"
            time.sleep(2 ** attempt * 3)
    return {"ok": False, "error": err, "attempts": 4}


# No tools, no MCP, no settings files, empty cwd (no CLAUDE.md), kit system prompt replaces the default.
CC_FLAGS = ["--tools", "", "--strict-mcp-config", "--setting-sources", "",
            "--exclude-dynamic-system-prompt-sections", "--no-session-persistence", "--output-format", "json"]


def call_cc(model, system, user, workdir):
    err = "no attempt"
    for attempt in range(4):
        try:
            p = subprocess.run(["claude", "-p", "--model", model, "--system-prompt", system, *CC_FLAGS],
                               input=user, capture_output=True, text=True, timeout=600, cwd=workdir)
            d = json.loads(p.stdout)
            if d.get("is_error") or p.returncode != 0:
                raise RuntimeError(f"rc={p.returncode} {d.get('subtype')} {d.get('api_error_status')} "
                                   f"{str(d.get('result'))[:300]}")
            u = d.get("usage", {})
            return {"ok": True, "text": d.get("result", ""), "model_returned": ",".join(d.get("modelUsage", {})),
                    "stop_reason": d.get("stop_reason"),
                    "usage": {"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                              "thinking_tokens": (u.get("output_tokens_details") or {}).get("thinking_tokens")},
                    "attempts": attempt + 1}
        except Exception as e:  # logged, never dropped
            err = f"{type(e).__name__}: {e}"
            time.sleep(2 ** attempt * 3)
    return {"ok": False, "error": err, "attempts": 4}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", choices=["drafting", "eval"], required=True)
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--max-tokens", type=int, default=2000)
    ap.add_argument("--dry-run", action="store_true", help="echo the input instead of calling a model")
    ap.add_argument("--results", default="results", help="results folder, relative to the kit")
    ap.add_argument("--prompts", default="prompt", help="prompt folder, relative to the kit")
    ap.add_argument("--prereg", default="PREREGISTRATION.md", help="pre-registration file that must be locked")
    ap.add_argument("--runner", choices=["claude-code", "api"], default="claude-code")
    a = ap.parse_args()

    results = KIT / a.results
    hashes = preflight(a.dry_run, results, a.prompts, a.prereg)
    system = (KIT / a.prompts / "system.md").read_text()
    client = None
    workdir = tempfile.mkdtemp(prefix="mvk-empty-")
    if not a.dry_run and a.runner == "api":
        import anthropic  # pip install anthropic
        client = anthropic.Anthropic()
    if a.runner == "claude-code":
        cc_version = subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
        params = {"runner": "claude-code", "claude_version": cc_version, "flags": CC_FLAGS,
                  "effort": os.environ.get("CLAUDE_EFFORT", "CLI default"),
                  "max_tokens": "CLI default", "temperature": "CLI default"}
    else:
        params = {"runner": "api", "max_tokens": a.max_tokens, "temperature": "API default"}
    params["prompts"] = a.prompts

    out_dir = results / ("raw-dryrun" if a.dry_run else "raw")
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    for model in a.models:
        path = out_dir / f"{a.task}__{model}__{stamp}.jsonl"
        with path.open("a") as f:
            for input_id, user in jobs(a.task, a.prompts):
                for run in range(1, a.runs + 1):
                    rec = {"task": a.task, "model_requested": model, "input_id": input_id, "run": run,
                           "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
                           "params": params,
                           "kit_hashes": hashes, "dry_run": a.dry_run}
                    if a.dry_run:
                        body = user.split("<passage>")[-1].split("</passage>")[0].strip() if a.task == "drafting" \
                            else '[{"quote": "robust", "rule": 2}, {"quote": "Harness", "rule": 2}]'
                        rec.update({"ok": True, "text": body, "model_returned": "dry-run"})
                    elif a.runner == "claude-code":
                        rec.update(call_cc(model, system, user, workdir))
                    else:
                        rec.update(call(client, model, system, user, a.max_tokens))
                    f.write(json.dumps(rec) + "\n")
                    f.flush()
                    print(f"{model} {input_id} run {run}: {'ok' if rec['ok'] else 'FAILED'}")
        print(f"wrote {path.relative_to(KIT)}")


if __name__ == "__main__":
    main()
