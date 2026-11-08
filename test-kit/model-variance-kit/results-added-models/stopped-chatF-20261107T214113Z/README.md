# Stopped Chat F eval run (2026-11-07T21:41:13Z)

All 10 eval calls completed ok (claude-fable-5-1 x5, claude-opus-4-7 x5). Held here, unscored, pending Kathryn's decision.

- Reason: `kit_hashes.json` here differs from `results/kit_hashes.json` on `PREREGISTRATION.md` (`5baa5c5cd2155b9f` vs `3afb099bf34f2247`). Same cause as the aborted Chat E run: the amendments added in commits 9b062ad and fee04a4. All other hashes match. The handoff says to stop when they differ.
- Files moved unedited from `raw/`. Kept outside `raw/` so `score.py --raw results-added-models/raw` doesn't pick them up.
- Not scored: Chat E's drafting files are also not on the branch.
