# Human blind scores (fixed sample)

97 sample rewrites scored blind by Kathryn Collins (2 per model, input and result set; one cell has 3). Joined to models after scoring finished. Not extrapolated: each cell describes 2 rewrites.

Meaning cells are yes/partly/no counts. Naturalness is the mean of 1 (stilted) to 3 (natural), with the range when the rewrites differ.

## Meaning preserved (yes/partly/no)

| Set | Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag | All |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main run (A/B) | claude-haiku-5-5 | 2/0/0 | 2/0/0 | 0/1/1 | 1/1/0 | 2/0/0 | 2/0/0 | 9/2/1 |
| Main run (A/B) | claude-opus-5-5 | 2/0/0 | 2/0/0 | 0/2/0 | 1/1/0 | 1/1/0 | 2/0/0 | 8/4/0 |
| Main run (A/B) | claude-sonnet-5-5 | 2/0/0 | 0/2/0 | 0/2/0 | 0/2/0 | 2/0/0 | 2/0/0 | 6/6/0 |
| Replication (C/D) | claude-haiku-5-5 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 1/1/0 | 2/0/0 | 7/5/0 |
| Replication (C/D) | claude-opus-5-5 | 2/0/0 | 0/1/1 | 0/2/0 | 1/1/0 | 2/0/0 | 2/0/0 | 7/4/1 |
| Replication (C/D) | claude-sonnet-5-5 | 2/0/0 | 1/1/0 | 2/1/0 | 1/1/0 | 2/0/0 | 2/0/0 | 10/3/0 |
| Added models (E/F) | claude-fable-5-1 | 2/0/0 | 1/1/0 | 0/2/0 | 2/0/0 | 2/0/0 | 2/0/0 | 9/3/0 |
| Added models (E/F) | claude-opus-4-7 | 2/0/0 | 1/0/1 | 0/2/0 | 2/0/0 | 2/0/0 | 2/0/0 | 9/2/1 |

## Reads naturally (1–3)

| Set | Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag | All |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main run (A/B) | claude-haiku-5-5 | 3.0 | 2.0 | 1.5 (1–2) | 3.0 | 2.5 (2–3) | 2.0 | 2.3 (1–3) |
| Main run (A/B) | claude-opus-5-5 | 2.0 | 2.5 (2–3) | 2.5 (2–3) | 3.0 | 3.0 | 2.5 (2–3) | 2.6 (2–3) |
| Main run (A/B) | claude-sonnet-5-5 | 3.0 | 1.0 | 3.0 | 2.5 (2–3) | 2.0 | 2.5 (2–3) | 2.3 (1–3) |
| Replication (C/D) | claude-haiku-5-5 | 2.5 (2–3) | 2.0 | 2.5 (2–3) | 2.5 (2–3) | 3.0 | 2.5 (2–3) | 2.5 (2–3) |
| Replication (C/D) | claude-opus-5-5 | 3.0 | 1.0 | 2.5 (2–3) | 3.0 | 3.0 | 2.5 (2–3) | 2.5 (1–3) |
| Replication (C/D) | claude-sonnet-5-5 | 2.5 (2–3) | 1.5 (1–2) | 2.3 (2–3) | 2.0 | 3.0 | 2.0 | 2.2 (1–3) |
| Added models (E/F) | claude-fable-5-1 | 2.5 (2–3) | 2.5 (2–3) | 2.0 | 3.0 | 2.0 | 3.0 | 2.5 (2–3) |
| Added models (E/F) | claude-opus-4-7 | 2.5 (2–3) | 1.5 (1–2) | 3.0 | 2.5 (2–3) | 2.5 (2–3) | 2.0 | 2.3 (1–3) |

## By input, all models

| Input | Meaning yes/partly/no | Naturalness |
| --- | --- | --- |
| 01-caveat-dash | 15/1/0 | 2.6 (2–3) |
| 02-you-and-permission | 8/6/2 | 1.8 (1–3) |
| 03-product-name | 3/13/1 | 2.4 (1–3) |
| 04-legit-just | 9/7/0 | 2.7 (2–3) |
| 05-procedure | 14/2/0 | 2.6 (2–3) |
| 06-code-and-flag | 16/0/0 | 2.4 (2–3) |

## Editor notes (0)


Rewrites scored beyond the sample: 0 (reported separately, not in these tables).
