# Aborted Chat E run (2026-11-07T21:41:06Z)

Stopped after 1 of 30 drafting calls. Quarantined here on purpose: not a valid result. Do not score.

- Reason: `kit_hashes.json` here differs from `results/kit_hashes.json` on `PREREGISTRATION.md` (`5baa5c5cd2155b9f` vs `3afb099bf34f2247`), caused by the added-models amendment in commit 9b062ad. The handoff says to stop when they differ.
- Contents: the partial raw file (1 ok record, claude-fable-5-1, input 01-caveat-dash, run 1) and the hashes run.py wrote.
- Kept outside `raw/` so `score.py --raw results-added-models/raw` and the Chat F hash check don't pick it up.
- Re-run Chat E after Kathryn decides on the hash mismatch.
