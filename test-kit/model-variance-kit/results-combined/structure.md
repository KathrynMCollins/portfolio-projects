# Structure check (exploratory)

Deterministic, from raw drafting outputs; see scripts/check_structure.py for definitions. Not a pre-registered metric for these runs. Mean per rewrite across 5 runs.

## By set and model (all inputs)

| Set | Model | headings_added | bold_added | list_items_added | callouts_added | micro_paragraphs | order_inversions | sentences_unmatched | word_ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main run | claude-haiku-5-5 | 0.3 | 0.0 | 0.0 | 0.0 | 0.2 | 0.0 | 0.0 | 0.9 |
| Main run | claude-opus-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0.0 | 0.2 | 0.9 |
| Main run | claude-sonnet-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0.0 | 0.2 | 0.9 |
| Replication | claude-haiku-5-5 | 0.2 | 0.0 | 0.2 | 0.0 | 0.1 | 0.0 | 0.4 | 1.1 |
| Replication | claude-opus-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0.0 | 0.2 | 0.9 |
| Replication | claude-sonnet-5-5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0.0 | 0.2 | 0.9 |
| Added models | claude-fable-5-1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0.0 | 0.2 | 0.9 |
| Added models | claude-opus-4-7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0.0 | 0.2 | 0.9 |
| Baseline | claude-fable-5-1 | 1.4 | 0.4 | 0.7 | 0.1 | 0.5 | 0.2 | 0.3 | 1.1 |
| Baseline | claude-haiku-5-5 | 0.5 | 0.3 | 0.0 | 0.0 | 0.3 | 0.0 | 0.3 | 1.0 |
| Baseline | claude-opus-4-7 | 2.1 | 0.7 | 1.3 | 0.1 | 0.3 | 0.0 | 0.3 | 1.1 |
| Baseline | claude-opus-5-5 | 1.3 | 0.6 | 0.8 | 0.4 | 0.4 | 0.3 | 0.2 | 1.1 |
| Baseline | claude-sonnet-5-5 | 1.3 | 0.1 | 1.3 | 0.1 | 0.5 | 0.3 | 0.2 | 1.1 |

## headings_added by input (main/added guided → baseline)

| Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- |
| claude-haiku-5-5 | 0.0 → 0.0 | 0.8 → 1.0 | 0.4 → 1.0 | 0.0 → 0.0 | 0.4 → 1.0 | 0.0 → 0.2 |
| claude-sonnet-5-5 | 0.0 → 1.8 | 0.0 → 3.8 | 0.0 → 0.8 | 0.0 → 1.0 | 0.0 → 0.0 | 0.0 → 0.6 |
| claude-opus-5-5 | 0.0 → 1.2 | 0.0 → 3.4 | 0.0 → 0.0 | 0.0 → 3.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-fable-5-1 | 0.0 → 2.0 | 0.0 → 2.2 | 0.0 → 0.0 | 0.0 → 3.0 | 0.0 → 0.6 | 0.0 → 0.8 |
| claude-opus-4-7 | 0.0 → 1.4 | 0.0 → 4.6 | 0.0 → 1.0 | 0.0 → 3.0 | 0.0 → 1.0 | 0.0 → 1.4 |

## order_inversions by input (main/added guided → baseline)

| Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag |
| --- | --- | --- | --- | --- | --- | --- |
| claude-haiku-5-5 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-sonnet-5-5 | 0.0 → 1.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 1.0 |
| claude-opus-5-5 | 0.0 → 1.0 | 0.0 → 0.6 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
| claude-fable-5-1 | 0.0 → 1.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.4 |
| claude-opus-4-7 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 | 0.0 → 0.0 |
