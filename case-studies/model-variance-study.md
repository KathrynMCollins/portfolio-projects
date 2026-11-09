# One style standard, five AI models: a pre-registered test

**Type:** Evaluation design, editorial standards and AI-assisted content operations
**When:** November 2026
**Tools:** Claude Code (headless runs), Python, the house style scanner, a blind scoring page, Git
**Prepared for:** Content management and technical writing roles

## What this shows

How I check that a written content standard holds before a team relies on it: hypotheses written down before any run, results reported as they came out (including the ones that went against me), and limits stated next to every claim. In this test, the writers applying the standard were AI models. The results are also the source for a talk that explains model behavior to writers who don't work with models.

## The question

Our documentation team gives AI models a written house style standard as part of the prompt. I wanted to know three things before relying on it:

1. Do different models apply the same standard the same way?
2. Does one model give the same result from run to run?
3. What does the standard actually change, compared with no standard at all?

## How the test worked

- **Pre-registered.** Hypotheses, metrics and honesty rules were fixed and dated before the first call: no re-running for a better result, no exclusions, failed calls counted, and no ranking of models.
- **Trap passages.** Six short documentation passages, each built around a style rule that, followed too literally, removes something a reader needs: a caveat after a dash, a permission sentence addressed to the reader, a product name that is also a buzzword, a "just" that carries meaning, a procedure, and a code block with a review flag.
- **A review task.** A draft with 12 planted violations and 4 correct passages that look suspicious, to measure both what a model finds and what it wrongly flags.
- **Five models, five runs per model per passage,** run through Claude Code with no tools, no skills and an empty working folder. A replication repeated the runs for three of the models. A baseline then repeated the runs for all five with the standard replaced by one neutral line ("You edit technical documentation."), under its own pre-registration.
- **Three kinds of scoring:** the house style scanner, text checks for each passage's key facts, and my own blind scoring of meaning and naturalness on a fixed sample, with the model hidden.
- **Drafting and evaluation kept apart.** The drafting and review tasks ran in separate sessions from the scoring.

456 calls in all, none failed. One aborted call is kept and reported but not scored.

## What came back

**With the standard, the models agreed more than I predicted.** In the main and added-models runs, every model produced rewrites with no scanner blockers and no lost facts, and found all 12 planted problems without flagging correct text. The replication had two exceptions, described below. All four of my original hypotheses (H1 to H4), which predicted differences, came out false. One rule did not hold for any model: the standard says "just" is often legitimate, yet the meaningful "just" in one passage was removed in 38 of 40 guided runs (and in all 25 baseline runs).

**Without the standard, the scanner still found nothing.** The baseline rewrites also had zero blockers. The scanner could not show what the standard was doing.

**What changed between the two conditions:**

| Measure | With standard | Without |
| --- | --- | --- |
| Fact checks lost on the code-and-flag passage, per run | 0 | about 1, every model |
| Planted problems found in review, of 12 | 12 | 9.0 to 10.6 |
| Correct passages wrongly flagged, of 4 | 0 | 2.6 to 3.4 |
| Reads naturally, blind human score from 1 to 3 | 2.4 | 1.9 |
| Meaning preserved, blind human score (yes / partly / no, 60 rewrites each) | 41 / 17 / 2 | 46 / 12 / 2 |

On meaning, the baseline scored the same or slightly better. Most of that difference is one passage, where a product name is also a buzzword: guided rewrites scored 0 / 9 / 1 and baseline rewrites 9 / 1 / 0. On naturalness, the baseline scored lower overall but higher on that passage and on the procedure.

My blind notes on the baseline rewrites were mostly about structure: added headings, reordered information, extra bold. Nothing in the kit measured that, so I added a structure check after the runs. Its heading count matched my notes closely; its order measure caught 3 of the 6 rewrites I had marked for reordering.

**Two findings about the instruments themselves:**

- In two replication runs, one model returned the tool's own environment description instead of a rewrite. Those two outputs were the only lost facts in the guided runs. The tool that runs the model is part of the prompt.
- Two nearly identical sentences from the product-name passage, scored a day apart, got different meaning scores from me: partly in the guided set, yes in the baseline set. The baseline hypothesis my human scores supported (HB4) rests on that passage, so part of that 9-to-0 difference may be my scoring drifting between sessions rather than the models. I report it that way.

## Changes made along the way, and recorded

Each change after the first lock is recorded as a dated amendment, or for the baseline as its own pre-registration, written before the results it affected were scored: switching the runner from the API to Claude Code, adding two models, recording the replication, and scoring a fixed sample instead of every rewrite. A scorer quirk that hid some extra review flags was disclosed rather than fixed after the fact.

## Limitations

- Small numbers: six passages, one review draft, five runs per model per passage. These results describe these models on these inputs. They are not a benchmark and do not rank models.
- One human scorer, scoring two rewrites per model and passage. Enough to see the structure problem, not enough to compare models.
- The human scoring was blind to the model but not to the condition, and the baseline sheets were scored a day after the guided ones. The guided and baseline differences in human scores are confounded with that.
- 29 of the guided sheets were scored before the fixed sample was drawn, and all count toward it, so the guided sample is not a clean random draw.
- The two prompts differ in more than the rule list, so the comparison shows a difference, not which part of the prompt caused it.
- The text checks look for key phrases. They miss a fact that is kept but moved or weakened, which is what the human pass caught.
- Every call ran through Claude Code with its default settings, which add a small environment block to each call.
- The structure check was added after the runs, so its results are exploratory.

## Materials

- Kit, pre-registrations, raw logs, scorers and results: [`test-kit/model-variance-kit/`](../test-kit/model-variance-kit/)
- Talk built from the results: [`talks/same-standard-different-readers/`](../talks/same-standard-different-readers/)

Environment details that one model echoed back are redacted in the portfolio copy of the logs; see the kit's `PORTFOLIO-NOTE.md`.
