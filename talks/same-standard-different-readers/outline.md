# Talk outline: one style standard, five models

Draft 2026-11-08 for the Write the Docs talk on content reuse when the reader is a model. Built from the model variance kit results in [`test-kit/model-variance-kit/`](../../test-kit/model-variance-kit/). Every number below comes from a file there; the source is named on each slide, relative to that folder. Examples were chosen after scoring and are shown with model, run and the aggregate for their cell, as PREREGISTRATION.md requires.

Working title: **Same standard, different readers: what five models did with one style guide**

Length: about 25 minutes, 18 slides.

## Claims this talk can make

- These models behaved differently, or alike, on these six passages and one review task.
- No ranking of models. No claim beyond these inputs. Human scores are two rewrites per cell and are described, not extrapolated.

---

## 1. Open: the reader changed

- We reuse a style standard across writers. Now the writer is often a model, and the standard is a prompt.
- Question: give five models the same standard and the same passages. How much do they differ from each other, and from run to run? What does the standard buy compared with no standard?
- Models: Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1, Opus 4.7.

## 2. How the test worked

- Pre-registered before any call: hypotheses, metrics, honesty rules (no re-runs for better results, no exclusions, blind human scoring).
- Six trap passages, each built around one rule that can cost substance: a caveat after a dash, a permission sentence with "you", a product name that is also a buzzword, a legitimate "just", a procedure, a code block with a review flag.
- One review task: a draft with 12 planted violations and 4 correct-but-suspicious distractors.
- Five runs per model per input, same settings. 456 calls, none failed: 455 scored, plus 1 aborted call kept but not scored.
- Scored three ways: the house scanner, substance checks, and blind human scoring (meaning preserved; reads naturally).
- Source: PREREGISTRATION.md, PREREGISTRATION-baseline.md, README.md.

## 3. With the standard, the models agreed

- Guided rewrites: 0 scanner blockers and 0 substance checks lost, every model, every input (main run and added models).
- Review task: 12 of 12 planted violations found and 0 distractors flagged, every model, every run in the main and added-models sets. (The replication had one exception; slide 4.)
- One rule did not hold. Rule 7 says "just" is often legitimate; input 04's "just" carries meaning. Guided rewrites removed it in 38 of 40 runs across all three guided sets.
- Source: results-combined/summary.md; info_just_kept in each set's scored/drafting_runs.csv.

**Example A (models agreeing).** Input 06, code block and review flag. Sonnet 5.5, main run, run 1:

> Original: "It's important to note that the alert can take up to 30 seconds to appear — this is expected."
> Rewrite: "The alert can take up to 30 seconds to appear; this is expected."

Code block and `[VERIFY: ...]` flag unchanged. Cell (Sonnet 5.5, input 06, 5 runs): 0 blockers, 0 substance lost. Across all five models on input 06, Kathryn scored all 10 sampled guided rewrites as meaning preserved.

## 4. Run to run, the same model was close to itself

- The replication repeated the first three models' runs a few minutes later. Blockers and substance checks matched the main run everywhere except one cell (slide 10).
- Review task: one replication cell moved, Haiku 5.5 at 11.8 planted found (11 to 12).
- Source: results-combined/summary.md.

## 5. Then we took the standard away

- Baseline: same models, same passages, one neutral line ("You edit technical documentation.") and no rules.
- Hypotheses, written before the run: more blockers without the standard (HB1); no more substance lost with it (HB2); distractors flagged without it (HB3); human meaning scores differ on the two hardest inputs (HB4).
- Source: PREREGISTRATION-baseline.md.

## 6. Surprise: no standard, still no blockers

- Baseline rewrites also had 0 blockers on every input. Checked against the raw text of all 150 rewrites: no dashes, buzzwords or flagged phrases.
- HB1 not supported. On these passages, asking for "clear technical documentation" removed what the scanner looks for.
- Point for the room: a scanner that passes everything cannot show what a standard is doing.
- Source: results-combined/baseline-vs-guided.md.

## 7. What the standard did buy: substance and review precision

- Substance: guided lost none; baseline lost about one check per run on input 06 for every model (HB2 supported).
- Review task without the standard: 9.0 to 10.6 of 12 planted violations found, and 2.6 to 3.4 of 4 distractors flagged (HB3 supported). With the standard: 12 of 12 and 0.
- In these runs, the prompt with the rule list kept reviewers off correct text; without it, they flagged it. The two prompts differ in more than the rule list, so this shows the difference, not which part caused it.
- Source: results-combined/baseline-vs-guided.md. Kathryn reviewed the baseline distractor hits and extra flags and accepted them as scored.

## 8. What the standard bought: shape

- Blind human scores, 60 guided and 60 baseline rewrites, same cells: reads naturally 2.4 guided, 1.9 baseline.
- Meaning went the other way: yes / partly / no 41 / 17 / 2 guided, 46 / 12 / 2 baseline. The standard bought shape, not meaning.
- Kathryn's notes on baseline sheets, written blind: "Way too many headers", "order of information changed", "Unecessary headings and unecessary bolding" [sic].
- The structure check, added after the runs to measure this: baseline rewrites added 0.5 to 2.1 headings per rewrite by model; guided added 0 to 0.3.
- Source: results-combined/human_scores_baseline.md, results-combined/structure.md.

**Example B (structure added).** Input 02, a four-sentence paragraph about maintenance plans. Opus 4.7, baseline, run 1: the rewrite has five headings ("Maintenance Plans", "Permissions", "Creating a Plan", "Stopping a Plan", "Recommended Practice"), one sentence under each. Kathryn: meaning preserved yes, reads naturally 1, "Way too many headers". Cell (Opus 4.7, input 02, baseline, 5 runs): 4.6 headings added per rewrite. Guided cell: 0.

**Example C (order changed).** Input 01, a caveat in the middle of the paragraph. Opus 5.5, baseline, run 2: the caveat moves to a Note after the "edit a pattern" heading. Kathryn: partly, 1, "Reordered information breaks continuity". Human cell (Opus 5.5, input 01): guided 2 yes, baseline 1 yes and 1 partly.

## 9. Automated checks miss what editors see

- Guided rewrites lost no substance checks on inputs 02, 03 and 04, yet Kathryn scored 29 of 49 sampled guided rewrites on those inputs "partly" or "no".
- The scanner never sees structure; the structure check's heading count tracked her notes closely (12 sheets noted for headings averaged 3.6 added, all at least one; the other 48 averaged 0.7). Its order measure caught 3 of the 6 sheets she noted for reordering.
- Source: results-combined/human_scores.md, results-combined/notes-for-write-up.md.

## 10. The harness is part of the prompt

**Example D.** Replication, Haiku 5.5, input 05, runs 3 and 4: instead of the rewritten procedure, the output is the Claude Code environment block (working directory, platform, scratchpad path). Runs 1, 2 and 5 of the same cell are clean four-step procedures.

- Those two runs are the only substance losses in the whole guided set (5 checks each). 2 of 455 scored calls; neither was in the human sample.
- The reader is a model, and it reads everything it is handed, including context nobody wrote for it.
- Source: results-haiku-exec/raw/, results-haiku-exec/scored/drafting_runs.csv.

## 11. Our own instruments wobbled too

- Scorer quirk: the review scorer credits a quote by string match, whatever rule the model cites, which hid at least three extra flags on one sentence. Kept as scored and disclosed.
- Rater drift, **Example E**: input 03, nearly identical sentences scored differently a day apart.
  - Guided, Opus 5.5, run 4: "Use it to include change data in root cause analysis and to link deployments to the incidents they cause." Scored partly.
  - Baseline, Opus 5.5, run 1: "Use these events to include change data in root cause analysis and to link deployments to the incidents they cause." Scored yes.
- HB4 came out supported on input 03 only (guided 0/9/1, baseline 9/1/0). With rewrites this close, that difference may be the scorer, not the models. Say so.
- Source: results-combined/notes-for-write-up.md, human_scores.csv, human_scores_baseline.csv.

## 12. Scoreboard

| Hypothesis | Result |
| --- | --- |
| H1 rule compliance costs substance on input 01 or 02 | Not supported: no substance check lost on 01 or 02 in any guided run |
| H2 run-to-run variation on at least 2 inputs | Not supported: one cell varied (replication Haiku 5.5, input 05), and that was the harness leak |
| H3 models differ on inputs 03 and 04 | Not supported: every model kept the product name on 03; on 04 the "just" was kept in only 2 of 40 runs, once each by Opus 5.5 (replication) and Fable 5.1 |
| H4 models differ in review, and a distractor is flagged | Not supported: no distractor flagged with the standard; planted found differed only in one replication cell |
| HB1 more blockers without the standard | Not supported |
| HB2 the standard costs no substance relative to none | Supported |
| HB3 a distractor flagged without the standard | Supported |
| HB4 human meaning differs on input 02 or 03 | Supported on 03 only; weak, possible rater drift |

The guided hypotheses all came out false: with the standard, the models agreed more than predicted. The baseline runs differed from the guided runs; differences between models within the baseline were not tested.

## 13. What to take back to your team

- If a model reads your standard, the standard is a prompt. Test it like one: same inputs, several runs, several models.
- Write rules that say what not to change, not only what to fix. In these runs, the guided prompt ("constrain phrasing, never substance", plus the rule list) lost no substance checks and flagged no correct text; the baseline did both.
- Check structure, not only words. The scanner found nothing in either condition; editors found plenty.
- Keep a blind human pass. Two rewrites per cell was enough to see the structure problem; it was not enough to rank anything.
- Log everything, including what the harness adds. Two of 455 scored outputs were the harness talking.

## 14. Close and materials

- Kit, raw logs, scorers and pre-registrations: [`test-kit/model-variance-kit/`](../../test-kit/model-variance-kit/).
- Limits: small n, six passages, one review draft, runs through Claude Code with its defaults, one human scorer.

