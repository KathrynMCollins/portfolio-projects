# Plan: no-standard baseline run (draft, not locked)

Status: decisions settled and locked 2026-11-08 as PREREGISTRATION-baseline.md (one neutral system line, eval included, hypotheses HB1 to HB4 as below, blind to model only). That file governs; this plan is background.

## Question

What do the same models produce on the same inputs when they are asked to edit technical documentation with no style standard and no skills? The guided run (results/, results-added-models/) shows what the standard gets; this run shows what the models do without it.

## Design

| Item | Guided run (done) | Baseline run (proposed) |
| --- | --- | --- |
| Models | Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1, Opus 4.7 | Same five |
| Runs | 5 per model per input | Same |
| Inputs | inputs/ (6 passages), eval/planted_draft.md | Same files, unchanged |
| System prompt | prompt/system.md (the standard) | One neutral line: "You edit technical documentation." No rules, no governing principle |
| Drafting prompt | "...so it meets the standard..." | "Rewrite the passage below as clear technical documentation. Return only the rewritten passage in Markdown. Do not add commentary." |
| Eval prompt | List violations with rule numbers | List every writing or style problem as `{"quote", "problem"}`; no rule numbers exist |
| Skills and tools | None (`--tools ""`, no settings, empty cwd) | Same; nothing else is loaded |
| Runner | Claude Code headless, same flags | Same |
| Output | results/ etc. | results-baseline/ |
| Calls | | 150 drafting, 25 eval |

## Scoring

- Drafting: the same house scanner and substance checks. This measures the baseline output against a standard it never saw, which is the point.
- Eval: planted found and distractor hits by the same quote matching. "Rule number correct" does not apply. Unplanted flags go to human review as before; expect many more, since the model has no rule list.
- The scorer quirk (overlapping match strings) applies here too and is noted the same way.
- Human: a fixed blind sample, 2 per model and input (60 sheets), scored with the same rubric on the same kind of page. Sheets show no model. Condition is visible to the scorer (all are baseline); see limits.

## Comparison

A new combined table puts baseline and guided side by side per model and input: blockers, warnings, substance lost, eval results, human scores. Same rule as before: describe differences on these inputs, no ranking of models.

## Hypotheses (proposed; Kathryn to confirm or edit before locking)

- HB1. For every model, baseline rewrites have more scanner blockers than guided rewrites on at least 4 of the 6 inputs.
- HB2. Baseline rewrites lose at least as many substance checks as guided rewrites (the standard does not cost substance relative to no standard).
- HB3. In evaluation, at least one model flags a distractor in at least one baseline run (it was 0 in every guided run).
- HB4. Human meaning-preserved counts differ between baseline and guided on input 02 or 03, the two inputs where guided rewrites drew the most "partly" or "no".

## Work needed before running

1. Kathryn: settle the open decisions below and confirm the hypotheses.
2. Add `prompt-baseline/` (system, drafting, eval) and `PREREGISTRATION-baseline.md`; both are frozen and hashed into results-baseline/kit_hashes.json at the first call.
3. run.py: a `--prompts` option naming the prompt folder (default prompt/). score.py: accept the eval output without rule numbers. Dry-run both.
4. Two chats, as before: G (drafting) and H (eval, then scoring), both writing only to results-baseline/.
5. Blind page for the 60-sheet human sample; join; combined baseline-vs-guided table.

## Limits

- One neutral sentence is still a prompt. "No guidance" is not possible; the plan holds it to one line so it is the same for every model.
- The human scorer knows every sheet is baseline. Blinding covers the model, not the condition. Mixing baseline and guided sheets on one page would blind the condition too but means scoring guided sheets again.
- Claude Code adds its small environment block to every call, as in the guided run.
- Same time-of-run caveat: baseline runs happen days after the guided run.
