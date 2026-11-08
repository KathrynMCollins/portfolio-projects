# Pre-registration: no-standard baseline

Locked on: 2026-11-08
Locked by: Kathryn Collins

Companion to PREREGISTRATION.md. Plan and rationale: PLAN-baseline.md.

## Question

What do the same models produce on the same inputs when asked to edit technical documentation with no style standard and no skills, compared with the guided run?

## Design (frozen)

- Models: claude-haiku-5-5, claude-sonnet-5-5, claude-opus-5-5, claude-fable-5-1, claude-opus-4-7.
- Runs: 5 per model per input, through Claude Code headless with the same flags as the guided run (no tools, no MCP, no settings files, empty working directory). Temperature, thinking and output limit are Claude Code defaults; effort is logged per call.
- Prompts: prompt-baseline/ for every call. System prompt is one neutral line, "You edit technical documentation." No rules, no governing principle, no skills.
- Inputs: the same inputs/ passages and eval/planted_draft.md, unchanged.
- Drafting: rewrite each of six passages as clear technical documentation.
- Evaluation: list writing and style problems in eval/planted_draft.md as {quote, problem}. No rule numbers.
- Output: results-baseline/.

## Hypotheses (written before any run)

- HB1. For every model, baseline rewrites have more scanner blockers than that model's guided rewrites on at least 4 of the 6 inputs.
- HB2. Baseline rewrites lose at least as many substance checks as guided rewrites, for every model (the standard costs no substance relative to no standard).
- HB3. In evaluation, at least one model flags a distractor in at least one baseline run.
- HB4. Human meaning-preserved counts differ between baseline and guided rewrites on input 02 or input 03.

Any hypothesis may come out false and is reported as clearly as a true one. The guided comparison uses the main run (results/) for Haiku, Sonnet and Opus 5.5 and results-added-models/ for Fable 5.1 and Opus 4.7; the replication is reported alongside, not pooled.

## Metrics (fixed)

- Blockers, warnings, substance lost: the unmodified house scanner and inputs/checks.json, as in the guided run.
- Evaluation: planted found (of 12), distractor hits (of 4), unparseable output, by the same quote matching. Rule number correct does not apply. Unplanted flags go to human review. The overlapping-match-string quirk noted for the guided run applies here too.
- Spread: min and max across runs, with every mean.

## Human scoring (blind)

Fixed sample of 2 rewrites per model and input (60 sheets), drawn with seed 20261108 before scoring. Same rubric as the guided run. The scorer is blind to the model, not to the condition (every sheet is baseline). Human-score claims are per cell from two rewrites and are not extrapolated.

## Rules for honesty

Same as PREREGISTRATION.md: no exclusions, no re-running for better results, frozen files hashed at the first real call, blind scoring before opening any key, claims limited to "these models behaved differently on these inputs", no ranking.
