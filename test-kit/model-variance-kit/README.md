# Model variance test kit

A small, pre-registered test of how different AI models, and repeated runs of one model, apply the same reused style standard. Built to produce honest examples for a Write the Docs talk on content reuse when the reader is a model.

## Layout

| Path | What it is | Frozen at first run |
| --- | --- | --- |
| PREREGISTRATION.md | Hypotheses, metrics, honesty rules | Yes |
| prompt/ | System prompt (the standard) and user templates | Yes |
| inputs/ | Six trap passages and their substance checks | Yes |
| eval/ | Planted-violation draft and answer key | Yes |
| scripts/run.py | Calls each model through Claude Code (`claude -p`) and logs every call | No |
| scripts/score.py | Deterministic scoring, summary, blind sheets | No |
| scripts/check_ai_tone.py | Copy of the house scanner, unmodified | No |
| scripts/check_structure.py | Structure check: headings, bold, lists, callouts, micro-paragraphs, sentence order, length (exploratory, added 2026-11-08) | No |
| results/ | Raw logs, kit hashes, scored output | Output |

## Run it

1. Claude Code must be installed and logged in (`claude --version`). No API key. The old API route is still there as `--runner api`.
2. Confirm the current model IDs on the Anthropic models documentation page. Edit them in PREREGISTRATION.md before locking if they differ.
3. Fill in `Locked on:` in PREREGISTRATION.md and commit.
4. Check the plumbing without API calls: `python3 scripts/run.py --task drafting --models fake --runs 1 --dry-run`, then `python3 scripts/score.py --raw results/raw-dryrun`.
5. Real runs: `python3 scripts/run.py --task drafting --models claude-haiku-5-5 claude-sonnet-5-5 claude-opus-5-5` and the same with `--task eval`.
6. Score: `python3 scripts/score.py`. Read results/scored/summary.md.
7. Human scoring: score results/scored/blind/ with the rubric in PREREGISTRATION.md before opening blind_key.csv.

Call volume at defaults: 90 drafting calls and 15 evaluation calls.

## Known limits

- Claude Code adds a small environment context block the flags cannot remove. It is constant across models and runs.
- Evaluation scoring credits a quote to a planted item by string match, whatever rule the model cites. Overlapping quotes can hide an unplanted flag. See results-combined/notes-for-write-up.md.
- The house scanner does not see structure. `scripts/check_structure.py` measures it; it was added after the runs, so it is exploratory for them. Adopt it in a pre-registration before using it as a fixed metric.
- Small n. Results illustrate behavior on these inputs; they are not a benchmark.
- Substance checks are string and regex tests. They can miss a caveat that was reworded beyond the pattern; the blind human pass is the backstop.
- Unplanted evaluation flags may be real violations the answer key missed. Review them before calling them errors.
- Temperature, thinking and output limits are Claude Code defaults, to match how the skills run. Run-to-run variation is part of what is being measured.
