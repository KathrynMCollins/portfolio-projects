# Notes for the write-up

Items the write-up must state. Decided by Kathryn Collins, 2026-11-07.

## Scorer quirk: overlapping match strings (not re-scored)

`score.py` credits a reported quote to a planted violation if the quote contains any of that violation's match strings, whatever rule number the model cites.

Step 3 of `eval/planted_draft.md` reads: "Enter a tag name and a match condition. The rule takes effect in 5–10 minutes." The answer key plants only the en dash (V08, rule 1) on that line. Sonnet 5.5 also flagged the second sentence under rule 8 (numbered steps are single imperative sentences).

- When the model's quote included "5–10", the rule 8 flag was credited to V08 and did not go to human review.
- When the quote stopped before the dash ("The rule takes effect in"), it was listed as unplanted: main run run 2, replication run 3.
- At least five Sonnet 5.5 eval runs flagged this sentence under rule 8; the summaries show two.
- Effect: "Runs with unplanted flags" undercounts this sentence, and "Rule number correct" can be off by one in the affected runs. Planted found and distractor hits are unaffected.
- Results were not re-scored. The numbers are reported as scored.

## Possible answer-key gap

The rule 8 flag on step 3 may be a real violation the answer key missed. It is a human-review item under the pre-registration, not counted as a model error.

## Other items to report

- Chat D's eval calls ran before Chat D was paused; they are the replication's eval set.
- One aborted Chat E drafting call is kept in `results-added-models/aborted-20261107T214106Z/` and not scored.
- Chat F's 10 eval calls were moved unchanged into `results-added-models/raw/`, not re-run.
- PREREGISTRATION.md carries three dated amendments (runner, added models, replication); it is the only frozen file whose hash differs across result sets.
- Runs were made through Claude Code headless; temperature, thinking and output limits are Claude Code defaults, and a small environment context block was present in every call.
- Run times differ by set: 21:22, 21:35, 21:41 and 22:21 UTC.

## Baseline run (2026-11-08)

- HB1 is not supported: guided and baseline rewrites both had 0 scanner blockers on every input. Checked against the raw text of all 150 baseline rewrites, not only the scored CSV.
- HB4 is supported on input 03 only. PREREGISTRATION-baseline.md did not set a size for "differ", so any difference in counts meets it. With 10 rewrites per input per condition this is weak evidence; state it that way.
- The scanner does not check structure. Kathryn's baseline editor notes (20 of 60) are mostly about added headings, reordered information and over-bolding, which no automated metric in the kit measures.
- Baseline distractor hits use text-only matching (no rule numbers) and need human review before they are quoted.
- The separate baseline scoring page was deleted on 2026-11-08 before any score was saved to it; all baseline scores are in the single blind scoring page.

## Structure check (added 2026-11-08, exploratory)

- scripts/check_structure.py measures what the scanner cannot: headings, bold, list items and callouts added, micro-paragraphs, sentence-order inversions, unmatched sentences and length. Results: results-combined/structure.md and structure_runs.csv.
- Added after every run, so it is exploratory for this study, not a pre-registered metric.
- Checked against Kathryn's blind baseline notes: the 12 sheets she noted for headings averaged 3.6 headings added (all 12 had at least one); the other 48 averaged 0.7. The 6 sheets she noted for reordering averaged 0.5 order inversions (3 of 6 detected) against 0.13 for the rest. The heading measure tracks her judgment closely; the order measure catches about half, because heavily restructured rewrites leave fewer sentences to align.

## Kathryn's review of evaluation flags (2026-11-08)

- Kathryn reviewed the baseline distractor hits and the unplanted flags and accepted them as scored. They can be quoted as reported.
