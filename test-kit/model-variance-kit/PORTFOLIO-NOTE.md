# Portfolio copy of the model variance kit

This folder is a copy of the kit as it stood after every run was scored (November 2026). It differs from the working copy in three ways:

1. **Redacted environment details.** In two replication runs (Haiku 5.5, input 05, runs 3 and 4) the model returned the runner's environment description instead of a rewrite. In those two records of `results-haiku-exec/raw/drafting__claude-haiku-5-5__*.jsonl`, and in the two blind sheets that show them, the lines naming the working directory, scratchpad path, operating system and network proxy are replaced with one bracketed note. Each redacted record carries a `portfolio_redaction` field. Scores were computed from the unredacted originals and are unchanged: both outputs fail the same checks either way.
2. **Generalized repository references.** `HANDOFF.md` named the internal repository and branch the kit ran from; those names are replaced with a description.
3. **Talk files moved.** The talk outline and slide generator now live in [`talks/same-standard-different-readers/`](../../talks/same-standard-different-readers/).

Nothing else was changed: prompts, inputs, answer key, pre-registrations, scripts and every other result file are as run. The frozen-file hashes in each `kit_hashes.json` still match the files, except `PREREGISTRATION.md` in the guided result sets: that file carries dated amendments made after those sets began, by design.

One generated line is out of date: `results-combined/summary.md` says human blind scoring is pending. It was completed afterwards; see `results-combined/human_scores.md` and `human_scores_baseline.md`.
