# Answer key for the Lanternfish sample

Lanternfish is a made-up log shipper. Its changelog and docs were written so each change tests
one rule. A correct run sorts them like this. Compare it with your report, or with
`findings.json` if you ran with `--json`.

| # | Change | Bucket | Page and action | Rule it tests |
|:--|:--|:--|:--|:--|
| S1 | `flush_interval_sec` renamed | impact, P2 | `configuration.md` and `troubleshooting.md`, update | A rename touches every page that names the key. The old key is an alias, so it is P2, not P1. |
| S2 | `batch_size` maximum raised to 2000 | impact, P2 | `configuration.md`, update | The stale text is a number in a table cell. |
| S3 | Send buffer refactored | none | none | Large engineering change, nothing a reader sees. |
| S4 | OAuth for the cloud sink | impact, P2 | `authentication.md`, update | The page says "one method", which is now wrong. |
| S5 | Windows on ARM, beta channel only | confirm | `getting-started.md` once stable | Not released to most users yet. Documenting it now would mislead. |
| S6 | `tail --follow` removed | impact, P1 | `cli-reference.md`, update | A published instruction now fails. Removals are the change teams forget. |
| S7 | Spelling fix in a log line | none | none | Not documented anywhere. |

The model's wording will differ from run to run. The buckets and pages are what to check.
Reasonable disagreement: S1 on `troubleshooting.md` can be P3, and S4 can be a new page
instead of an update.
