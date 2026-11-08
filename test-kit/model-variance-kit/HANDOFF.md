# Handoff: run the model variance test

Two Claude Code chats run this kit in parallel. Each is an executor: run, log, score. Neither interprets results or drafts the write-up.

## Setup for both chats (added 2026-11-07)

- The kit lived in a folder on a working branch of the author's documentation repository. Work from that folder. The lock (2026-11-07) is committed.
- Real runs go through Claude Code headless (`claude -p`, the default `--runner claude-code`) on the chat's own login. No API key. Run both chats as Claude Code cloud sessions so the environment is the same. If `claude -p` fails to authenticate, stop and report it as a blocking action item. Do not switch to `--runner api` or another route.
- Calls run one at a time; expect roughly 30 to 60 minutes for Chat A. Run it in the background if the chat allows it.
- Results are shared through git, because separate chats do not share a filesystem. After a run, commit `results/raw/*.jsonl` and `results/kit_hashes.json` to that branch and push. Pull before you start and before you push.
- `kit_hashes.json`: whichever chat pushes first owns it. If the other chat's copy conflicts and the hashes are identical, keep the committed one. If they differ, stop and report it; a frozen file changed.
- Chat B: pull Chat A's raw files before `score.py`, then commit `results/scored/`.

## Chats C and D: replication (added 2026-11-07)

Same as Chats A and B, run by a Claude Code session on claude-haiku-5-5, with every output in `results-haiku-exec/` (`--results results-haiku-exec` on run.py, `--raw results-haiku-exec/raw` on score.py). Do not touch `results/`. Both chats were paused once and resumed. Keep and commit any partial file from before the pause alongside the new one; never delete or edit one.

## Chats E and F: added models (added 2026-11-07)

Same as Chats A and B, for claude-fable-5-1 and claude-opus-4-7 only, with every output in `results-added-models/`. Do not touch `results/`.

- Chat E: `python3 scripts/run.py --task drafting --models claude-fable-5-1 claude-opus-4-7 --results results-added-models`. Commit and push `results-added-models/raw/*.jsonl` and `results-added-models/kit_hashes.json`. Done when two drafting files exist and the failure count is reported.
- Chat F: `python3 scripts/run.py --task eval --models claude-fable-5-1 claude-opus-4-7 --results results-added-models`, commit and push the same way. When Chat E's two drafting files are on the branch, `python3 scripts/score.py --raw results-added-models/raw`, then commit `results-added-models/scored/`. Report the summary.md tables as they are, with no commentary. If Chat E's files are not there yet, stop and report it.
- Both chats: every hash in `results-added-models/kit_hashes.json` must match `results/kit_hashes.json` except `PREREGISTRATION.md`, which differs because of the dated amendments in that file. Any other difference: stop and report it.
- Order: Chat E runs first, so run.py writes `results-added-models/kit_hashes.json`. Chat F's eval runs from 21:41 UTC are already done (`stopped-chatF-20261107T214113Z/`). Do not re-run them: `git mv` the two eval .jsonl files, unchanged, into `results-added-models/raw/`, and leave that folder's README and kit_hashes.json where they are. The one-call aborted Chat E file stays in `aborted-20261107T214106Z/`, is not scored, and is reported.

## Chats G and H: no-standard baseline (added 2026-11-08)

Governed by PREREGISTRATION-baseline.md (locked 2026-11-08). Every run.py command takes `--prompts prompt-baseline --prereg PREREGISTRATION-baseline.md --results results-baseline`. Write only to `results-baseline/`; do not touch any other results folder. Do not edit prompt-baseline/ or PREREGISTRATION-baseline.md.

- Chat G: `python3 scripts/run.py --task drafting --models claude-haiku-5-5 claude-sonnet-5-5 claude-opus-5-5 claude-fable-5-1 claude-opus-4-7 --prompts prompt-baseline --prereg PREREGISTRATION-baseline.md --results results-baseline`. Commit and push `results-baseline/raw/*.jsonl` and `results-baseline/kit_hashes.json`. Done when five drafting files exist and the failure count is reported.
- Chat H: the same command with `--task eval`. Wait until Chat G's five drafting files and `results-baseline/kit_hashes.json` are on the branch (pull every few minutes), then commit and push your five eval files. Run `python3 scripts/score.py --raw results-baseline/raw`, commit `results-baseline/scored/`, push, and report the summary.md tables as they are, with no commentary. "Rule number correct" is 0 by design (the baseline eval has no rule numbers).
- Hash check: every hash in your call records must match `results-baseline/kit_hashes.json`. Any difference: stop and report it.
- Chat G runs first so run.py writes `results-baseline/kit_hashes.json` once. If Chat H's run.py stops on a kit_hashes mismatch, stop and report.

## Shared constraints (both chats)

- Do not edit anything in prompt/, inputs/, eval/, or PREREGISTRATION.md. If something looks wrong, stop and report it as an action item.
- Do not re-run calls to improve results. Never delete or edit a results/raw file.
- Do not change scripts/check_ai_tone.py.
- If you commit the kit to a repo, use a new folder on the working branch. No other branch.
- Model routing: these chats only execute. Any later drafting of the write-up uses an Opus-class model; any evaluation uses Sonnet, in a separate call.
- End with a summary and an explicit action-items list (owner, action, blocking or non-blocking).

## Chat A: drafting runs

1. Confirm PREREGISTRATION.md has a `Locked on:` date. If not, stop and ask Kathryn.
2. Run the dry-run check in README step 4. Fix only scripts/run.py or scripts/score.py if they break, and list every change.
3. `python3 scripts/run.py --task drafting --models claude-haiku-5-5 claude-sonnet-5-5 claude-opus-5-5`
4. Report: files written, calls ok, calls failed with errors.

Done when: three drafting files exist in results/raw/ and the failure count is reported.

## Chat B: evaluation runs, then scoring

1. Same lock check as Chat A.
2. `python3 scripts/run.py --task eval --models claude-haiku-5-5 claude-sonnet-5-5 claude-opus-5-5`
3. When Chat A's files are in results/raw/ too, run `python3 scripts/score.py`.
4. Report the summary.md tables as they are, with no commentary on which model is better.

Done when: results/scored/ holds drafting_runs.csv, eval_runs.csv, summary.md, blind/ and blind_key.csv, and the action items include "Kathryn: blind human scoring".
