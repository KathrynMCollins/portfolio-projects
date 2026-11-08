# Baseline (no standard) vs guided

From each set's scored CSVs; nothing re-scored. Guided = results/ for Haiku, Sonnet and Opus 5.5 and results-added-models/ for Fable 5.1 and Opus 4.7, per PREREGISTRATION-baseline.md. Each cell: guided → baseline, mean of 5 runs, range when runs differ. These models on these inputs; not a ranking.

## Scanner blockers (guided → baseline)

| Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- |
| claude-haiku-5-5 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-sonnet-5-5 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-opus-5-5 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-fable-5-1 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-opus-4-7 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |

## Scanner warnings (guided → baseline)

| Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- |
| claude-haiku-5-5 | 0.2 (0–1) → 0.2 (0–1) | 1.8 (0–3) → 2.4 (0–4) | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-sonnet-5-5 | 0.6 (0–1) → 1.0 | 0.2 (0–1) → 2.0 (1–3) | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-opus-5-5 | 1.0 → 1.0 | 0.4 (0–1) → 1.6 (1–2) | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-fable-5-1 | 0.2 (0–1) → 1.0 | 0.6 (0–1) → 0.2 (0–1) | 0.0 → 0.0 | 0.2 (0–1) → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-opus-4-7 | 0.0 → 1.0 | 1.0 → 1.0 (0–2) | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |

## Substance checks lost (guided → baseline)

| Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- |
| claude-haiku-5-5 | 0.0 → 0.0 | 0.0 → 0.2 (0–1) | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 1.0 |
| claude-sonnet-5-5 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 1.0 |
| claude-opus-5-5 | 0.0 → 0.0 | 0.0 → 0.6 (0–1) | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 1.0 |
| claude-fable-5-1 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 1.2 (1–2) |
| claude-opus-4-7 | 0.0 → 0.0 | 0.0 → 0.2 (0–1) | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 1.4 (1–2) |

## Evaluation (guided → baseline)

| Model | Planted found (of 12) | Distractor hits (of 4) | Runs with unplanted flags |
| --- | --- | --- | --- |
| claude-haiku-5-5 | 12.0 → 9.4 (9–10) | 0.0 → 2.6 (2–3) | 0 → 2 |
| claude-sonnet-5-5 | 12.0 → 9.0 (8–10) | 0.0 → 2.8 (2–4) | 1 → 4 |
| claude-opus-5-5 | 12.0 → 10.2 (9–11) | 0.0 → 3.4 (3–4) | 0 → 5 |
| claude-fable-5-1 | 12.0 → 9.2 (9–10) | 0.0 → 3.4 (2–4) | 0 → 5 |
| claude-opus-4-7 | 12.0 → 10.6 (9–12) | 0.0 → 3.0 (2–4) | 0 → 5 |

## Pre-registered hypotheses (automated part)

- HB1 (baseline has more blockers on at least 4 of 6 inputs, every model): not supported. Inputs with more blockers per model: claude-haiku-5-5 0/6, claude-sonnet-5-5 0/6, claude-opus-5-5 0/6, claude-fable-5-1 0/6, claude-opus-4-7 0/6.
- HB2 (baseline loses at least as many substance checks as guided, every model): supported. Sum of per-input means, baseline vs guided: claude-haiku-5-5 1.2 vs 0.0, claude-sonnet-5-5 1.0 vs 0.0, claude-opus-5-5 1.6 vs 0.0, claude-fable-5-1 1.2 vs 0.0, claude-opus-4-7 1.6 vs 0.0.
- HB3 (at least one model flags a distractor in at least one baseline run): supported.
- HB4 (human meaning scores differ on input 02 or 03): see results-combined/human_scores_baseline.md.

## Caveats

- Baseline evaluation has no rule numbers, so a quote is matched to planted items and distractors by text only. The overlapping-match-string quirk (results-combined/notes-for-write-up.md) can credit a planted item or a distractor to a quote flagged for another reason. Distractor hits here need the same human review as unplanted flags.
- Baseline runs were made on 2026-11-08, a day after the guided runs.
- Scanner and substance checks measure the baseline against a standard it never saw; that is the design, not a fault in the baseline.
