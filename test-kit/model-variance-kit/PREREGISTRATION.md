# Pre-registration: model variance under one reused style standard

Locked on: 2026-11-07
Locked by: Kathryn Collins
Amended: 2026-11-07, before any real run. Runner changed from the Anthropic API to Claude Code headless (`claude -p`) on the runner's own login. No hypothesis, metric, input or rubric changed.
Amended: 2026-11-07, after the first three models' raw runs were committed and before any scored result was read. Added models: claude-fable-5-1 and claude-opus-4-7. Their runs use the same frozen prompts, inputs, runner and flags, write to results-added-models/, and are reported alongside the first three, with the run dates stated. No hypothesis, metric, input or rubric changed. H3 and H4 ("models differ") are tested across all five models.
Amended: 2026-11-07. Replication: Chats C and D repeat the drafting and evaluation runs for the first three models, run by a Claude Code session on claude-haiku-5-5 instead of claude-opus-5-5, into results-haiku-exec/. The tested models, prompts, inputs, runner and flags are identical. C and D were paused partway and then resumed; every file from before and after the pause is kept. The replication is reported alongside the main run as a check on run-to-run variation, not pooled into it.
Amended: 2026-11-08, after 29 of 240 rewrites were blind-scored and before any human score was joined to a model. Human scoring uses a fixed stratified sample instead of all 240: two rewrites per model, input and result set (48 cells), 97 sheets in total (one cell holds three already-scored sheets). Already-scored sheets count toward their cell; the rest were drawn with seed 20261108. The sample is listed in results-combined/human-sample.csv and shown first on the scoring page. Human-score claims are per cell from two rewrites and are not extrapolated beyond them. Sheets scored beyond the sample are reported separately.

## Question

Given one fixed style standard and fixed inputs, how do different models, and repeated runs of one model, differ in ways that matter to a writer?

## Design (frozen)

- Models: claude-haiku-5-5, claude-sonnet-5-5, claude-opus-5-5. Optional older model: none.
- Runs: 5 per model per input, through Claude Code headless (`claude -p --model <id>`), with the kit system prompt replacing the default, no tools, no MCP, no settings files and an empty working directory. Temperature, thinking and output limit are Claude Code defaults; effort is the runner's `CLAUDE_EFFORT` and is logged with every call.
- All runs use the same environment type (Claude Code cloud sessions). That environment adds a small context block (environment and user details) that the flags cannot remove; it is the same for every model and run, and is noted in the write-up.
- Prompt: prompt/system.md for every call. User templates in prompt/.
- Drafting task: rewrite each of six passages in inputs/ to the standard.
- Evaluation task: list violations in eval/planted_draft.md (12 planted, 4 distractors; answer key in eval/answer_key.json).

## Hypotheses (written before any run)

- H1. Rule compliance can cost substance: at least one model loses a substance check in at least one run on input 01 (caveat after a dash) or 02 (permission sentence).
- H2. Run-to-run variation: for at least 2 of the 6 inputs, a single model's 5 runs differ in blocker count or in which substance checks pass.
- H3. Between-model variation: models differ in handling the product-name collision (input 03) and in keeping the legitimate "just" (input 04).
- H4. Evaluation: models differ in planted violations found, and at least one model flags a distractor (correct text) in at least one run.

Any hypothesis may come out false. A false result is reported as clearly as a true one.

## Metrics (fixed)

- Blockers: count from scripts/check_ai_tone.py (unmodified house scanner).
- Substance lost: count of failed substance checks in inputs/checks.json.
- Evaluation: planted found (of 12), distractor hits (of 4), unparseable output. Unplanted flags go to human review; they are not counted as errors automatically.
- Spread: min and max across runs, reported alongside every mean.

## Rules for honesty

- No exclusions. Failed and unparseable calls are reported in the totals.
- No re-running to get a better result. If a run must be repeated (for example, an outage), the new file is kept alongside the old one and both are reported.
- Frozen files are hashed at the first real run. Changing any of them means a new results folder and a note in the write-up.
- Human-judged items are scored blind from results/scored/blind/ before opening blind_key.csv.
- Examples for slides are chosen only after scoring. Each is shown with its model, run number, and the aggregate for that cell. At least one example shows models agreeing.
- Claims are limited to "these models behaved differently on these inputs". No ranking of models as better or worse.

## Human scoring rubric (blind)

For each rewrite: meaning preserved (yes / partly / no) and reads naturally (1 = stilted, 2 = acceptable, 3 = natural). Note any change you would reject as an editor.
