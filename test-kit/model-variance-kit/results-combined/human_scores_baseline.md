# Human blind scores: baseline vs guided

Baseline: 60 sample rewrites (2 per model and input), scored blind to model by Kathryn Collins. Guided: the matching cells of the guided sample (main run for Haiku, Sonnet and Opus 5.5; added-models run for Fable 5.1 and Opus 4.7), 60 rewrites. Each cell is 2 rewrites per condition; not extrapolated. Meaning is yes/partly/no counts; naturalness is the mean of 1 to 3.

## By input, all five models (guided → baseline)

| Input | Meaning | Naturalness |
| --- | --- | --- |
| 01-caveat-dash | 10/0/0 → 5/4/1 | 2.6 → 1.7 |
| 02-you-and-permission | 6/3/1 → 6/3/1 | 1.9 → 1.0 |
| 03-product-name | 0/9/1 → 9/1/0 | 2.4 → 2.6 |
| 04-legit-just | 6/4/0 → 9/1/0 | 2.8 → 1.6 |
| 05-procedure | 9/1/0 → 10/0/0 | 2.4 → 2.8 |
| 06-code-and-flag | 10/0/0 → 7/3/0 | 2.4 → 2.0 |
| All | 41/17/2 → 46/12/2 | 2.4 → 1.9 |

## Meaning by model and input (guided → baseline)

| Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag | All |
| --- | --- | --- | --- | --- | --- | --- | --- |
| claude-haiku-5-5 | 2/0/0 → 2/0/0 | 2/0/0 → 2/0/0 | 0/1/1 → 2/0/0 | 1/1/0 → 2/0/0 | 2/0/0 → 2/0/0 | 2/0/0 → 2/0/0 | 9/2/1 → 12/0/0 |
| claude-sonnet-5-5 | 2/0/0 → 1/0/1 | 0/2/0 → 1/0/1 | 0/2/0 → 1/1/0 | 0/2/0 → 2/0/0 | 2/0/0 → 2/0/0 | 2/0/0 → 2/0/0 | 6/6/0 → 9/1/2 |
| claude-opus-5-5 | 2/0/0 → 1/1/0 | 2/0/0 → 0/2/0 | 0/2/0 → 2/0/0 | 1/1/0 → 1/1/0 | 1/1/0 → 2/0/0 | 2/0/0 → 0/2/0 | 8/4/0 → 6/6/0 |
| claude-fable-5-1 | 2/0/0 → 1/1/0 | 1/1/0 → 2/0/0 | 0/2/0 → 2/0/0 | 2/0/0 → 2/0/0 | 2/0/0 → 2/0/0 | 2/0/0 → 1/1/0 | 9/3/0 → 10/2/0 |
| claude-opus-4-7 | 2/0/0 → 0/2/0 | 1/0/1 → 1/1/0 | 0/2/0 → 2/0/0 | 2/0/0 → 2/0/0 | 2/0/0 → 2/0/0 | 2/0/0 → 2/0/0 | 9/2/1 → 9/3/0 |

## Naturalness by model and input (guided → baseline)

| Model | 01-caveat-dash | 02-you-and-permission | 03-product-name | 04-legit-just | 05-procedure | 06-code-and-flag | All |
| --- | --- | --- | --- | --- | --- | --- | --- |
| claude-haiku-5-5 | 3.0 → 2.5 | 2.0 → 1.0 | 1.5 → 3.0 | 3.0 → 2.0 | 2.5 → 2.0 | 2.0 → 2.0 | 2.3 → 2.1 |
| claude-sonnet-5-5 | 3.0 → 2.5 | 1.0 → 1.0 | 3.0 → 2.0 | 2.5 → 2.5 | 2.0 → 3.0 | 2.5 → 2.0 | 2.3 → 2.2 |
| claude-opus-5-5 | 2.0 → 1.5 | 2.5 → 1.0 | 2.5 → 2.5 | 3.0 → 1.0 | 3.0 → 3.0 | 2.5 → 2.0 | 2.6 → 1.8 |
| claude-fable-5-1 | 2.5 → 1.0 | 2.5 → 1.0 | 2.0 → 3.0 | 3.0 → 1.0 | 2.0 → 3.0 | 3.0 → 2.0 | 2.5 → 1.8 |
| claude-opus-4-7 | 2.5 → 1.0 | 1.5 → 1.0 | 3.0 → 2.5 | 2.5 → 1.5 | 2.5 → 3.0 | 2.0 → 2.0 | 2.3 → 1.8 |

## HB4

HB4 (human meaning-preserved counts differ between baseline and guided on input 02 or 03): supported. Input 02 differs: no; input 03 differs: yes. The pre-registration did not set a size for "differ", so any difference in counts meets it; with 10 rewrites per input per condition, small differences are within what two runs per cell can show by chance.

## Baseline editor notes (20)

- B059 · claude-fable-5-1 · 02-you-and-permission: Way too many headers
- B062 · claude-fable-5-1 · 01-caveat-dash: The information order has changed - the last paragraph needs to be up higher
- B063 · claude-opus-5-5 · 02-you-and-permission: Way too many headers, order of information changed
- B075 · claude-opus-5-5 · 04-legit-just: Too many headers
- B078 · claude-opus-5-5 · 04-legit-just: Too many headers, risk losing context
- B082 · claude-opus-4-7 · 02-you-and-permission: Way too many headers
- B087 · claude-haiku-5-5 · 02-you-and-permission: Awkwardly broken up
- B089 · claude-opus-4-7 · 01-caveat-dash: Breaks standard format
- B091 · claude-sonnet-5-5 · 02-you-and-permission: Too many headers
- B097 · claude-haiku-5-5 · 02-you-and-permission: Added causal with no evidence. We do not include Prerequisite field
- B102 · claude-fable-5-1 · 01-caveat-dash: Unecessary break creates micro-paragraph
- B111 · claude-opus-5-5 · 01-caveat-dash: Reordered information breaks continuity
- B134 · claude-opus-5-5 · 02-you-and-permission: No prerequisite line or before you start, reordered information matters
- B141 · claude-opus-4-7 · 02-you-and-permission: Too many headings, reordered info is broken
- B142 · claude-fable-5-1 · 02-you-and-permission: Unecessary headings and unecessary bolding
- B143 · claude-sonnet-5-5 · 06-code-and-flag: Why verify at end so strange
- B145 · claude-fable-5-1 · 04-legit-just: Too many headings
- B146 · claude-fable-5-1 · 04-legit-just: Too many headings, too wordy
- B147 · claude-sonnet-5-5 · 02-you-and-permission: Too many headings, order has changed
- B148 · claude-opus-4-7 · 04-legit-just: Too many headings
