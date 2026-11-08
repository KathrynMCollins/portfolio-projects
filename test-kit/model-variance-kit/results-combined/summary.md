# All models: combined results

Built from each set's `scored/drafting_runs.csv` and `scored/eval_runs.csv`. No new scoring. Sets are shown separately and are not pooled. Mean across 5 runs; a range in brackets means the runs differed. Small n: these models on these inputs, not a ranking.

Run times (UTC, 2026-11-07): main run 21:22, replication 21:35, added models 21:41 (eval) and 22:21 (drafting).

## Drafting: blockers (house scanner)

| Set | Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Main run (A/B) | claude-haiku-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Main run (A/B) | claude-opus-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Main run (A/B) | claude-sonnet-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Replication (C/D) | claude-haiku-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Replication (C/D) | claude-opus-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Replication (C/D) | claude-sonnet-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Added models (E/F) | claude-fable-5-1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Added models (E/F) | claude-opus-4-7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## Drafting: substance checks lost

| Set | Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Main run (A/B) | claude-haiku-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Main run (A/B) | claude-opus-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Main run (A/B) | claude-sonnet-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Replication (C/D) | claude-haiku-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 2.0 (0–5) | 0.0 |
| Replication (C/D) | claude-opus-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Replication (C/D) | claude-sonnet-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Added models (E/F) | claude-fable-5-1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Added models (E/F) | claude-opus-4-7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## Drafting: warnings

| Set | Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Main run (A/B) | claude-haiku-5-5 | 0.2 (0–1) | 1.8 (0–3) | 0.0 | 0.0 | 0.0 | 0.0 |
| Main run (A/B) | claude-opus-5-5 | 1.0 | 0.4 (0–1) | 0.0 | 0.0 | 0.0 | 0.0 |
| Main run (A/B) | claude-sonnet-5-5 | 0.6 (0–1) | 0.2 (0–1) | 0.0 | 0.0 | 0.0 | 0.0 |
| Replication (C/D) | claude-haiku-5-5 | 0.0 | 1.6 (1–2) | 0.0 | 0.0 | 0.2 (0–1) | 0.0 |
| Replication (C/D) | claude-opus-5-5 | 1.0 | 0.6 (0–1) | 0.0 | 0.2 (0–1) | 0.0 | 0.0 |
| Replication (C/D) | claude-sonnet-5-5 | 0.6 (0–1) | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Added models (E/F) | claude-fable-5-1 | 0.2 (0–1) | 0.6 (0–1) | 0.0 | 0.2 (0–1) | 0.0 | 0.0 |
| Added models (E/F) | claude-opus-4-7 | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## Drafting: calls

| Set | Model | Ok / total |
| --- | --- | --- |
| Main run (A/B) | claude-haiku-5-5 | 30/30 |
| Main run (A/B) | claude-opus-5-5 | 30/30 |
| Main run (A/B) | claude-sonnet-5-5 | 30/30 |
| Replication (C/D) | claude-haiku-5-5 | 30/30 |
| Replication (C/D) | claude-opus-5-5 | 30/30 |
| Replication (C/D) | claude-sonnet-5-5 | 30/30 |
| Added models (E/F) | claude-fable-5-1 | 30/30 |
| Added models (E/F) | claude-opus-4-7 | 30/30 |

## Evaluation (12 planted violations, 4 distractors)

| Set | Model | Ok / total | Unparseable | Planted found | Rule number correct | Distractor hits | Runs with unplanted flags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Main run (A/B) | claude-haiku-5-5 | 5/5 | 0 | 12.0 | 12.0 | 0.0 | 0 |
| Main run (A/B) | claude-opus-5-5 | 5/5 | 0 | 12.0 | 11.0 | 0.0 | 0 |
| Main run (A/B) | claude-sonnet-5-5 | 5/5 | 0 | 12.0 | 12.0 | 0.0 | 1 |
| Replication (C/D) | claude-haiku-5-5 | 5/5 | 0 | 11.8 (11–12) | 11.8 (11–12) | 0.0 | 0 |
| Replication (C/D) | claude-opus-5-5 | 5/5 | 0 | 12.0 | 11.0 | 0.0 | 0 |
| Replication (C/D) | claude-sonnet-5-5 | 5/5 | 0 | 12.0 | 11.6 (11–12) | 0.0 | 1 |
| Added models (E/F) | claude-fable-5-1 | 5/5 | 0 | 12.0 | 11.8 (11–12) | 0.0 | 0 |
| Added models (E/F) | claude-opus-4-7 | 5/5 | 0 | 12.0 | 12.0 | 0.0 | 0 |

## Not scored, reported

- `results-added-models/aborted-20261107T214106Z/`: 1 Chat E drafting call (Fable 5.1, input 01, run 1) from a run stopped on the expected PREREGISTRATION.md hash difference.
- Chat D's eval calls were made before Chat D was paused; they are the replication's eval set above.
- Added-models hashes match the main run except PREREGISTRATION.md (dated amendments).
- Human blind scoring is pending for all three sets.
