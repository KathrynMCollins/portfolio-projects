# Feature name governance across docs, product and marketing

**Type:** Case study: naming decisions, disclosure and cross-team ownership
**When:** November 2026
**Author:** Kathryn Collins
**Prepared for:** Content management and technical writing roles

## What this shows

A name is the smallest unit of disclosure. Calling a capability by the wrong name, or by an internal name too early, tells customers something the company did not decide to say. The registry treats naming the way a publishing team treats any public claim: one owner per stage, a record of every change, and no automated step that can put words in front of readers without a person deciding.

## Summary

A feature's published name is a public statement, and it changes more often than most teams expect. I designed a Feature Name Registry that keeps one record per feature, keyed on an ID that never changes, and separates the name engineering uses from the name customers read. A rename becomes a tracked event with a checklist instead of a silent edit, and only a person can set the published name: docs before general availability, product marketing at it.

Portfolio note: feature names, page IDs and internal paths are generalized.

## The problem

Our issue tracker follows a feature through any rename because it matches on an ID. Almost nothing else does: wiki page titles, digest headings, docs ticket titles, CMS topics and URL slugs all match on the name.

In September 2026 one internal feature was renamed mid-development. One tracking row updated correctly. Four artifacts that referred to the old name were orphaned, and nothing reported it. No one had made a mistake; the system simply had no way to notice that a name had changed.

## Design

The registry is one row per feature, joined on the tracker's ID. Its columns are split by who may write them, so an automation (a scheduled job that reads the issue tracker) can keep it current without ever deciding what customers see.

| Column | Written by | Purpose |
| --- | --- | --- |
| Tracker ID | Automation | The only join key; never blank |
| Published name | **People only** | The name docs publish. Blank means "use the tracker name for now" and stays visibly blank. |
| Tracker name | Automation | What engineering currently calls it; may differ from the published name |
| Former names | Automation appends; people may add | Every name the feature has had; never deleted |
| Slug | Automation, once | URL-safe identifier, set at first sight and never changed |
| Publishing surface | People | Public docs, internal wiki, or both |
| Last renamed | Automation | Date of the most recent detected rename |
| Lead PM | People | Routes review of registry changes to the owning product manager |

The registry is kept apart from the automation's own records on purpose. The automation's records are machine-owned; the registry's human columns change only through a reviewed pull request, and the automation refuses to write a registry whose human columns differ from what it last read.

## Rules

1. **A rename is an event, not an edit.** When the tracker name changes, the automation records the new name, appends the old one to former names, dates it, and opens one docs ticket titled with the old and new names. The ticket carries a checklist of every place the name must change. Nothing is reconciled silently.
2. **A stable difference is not a rename.** If engineering's name and the published name differ and neither moves, that is the registry working as intended.
3. **Only a person sets the published name.** This is enforced in code: the automation raises an error if it tries. It never copies the tracker name into the published-name column.
4. **Ownership follows the release stage.** Docs set the published name before general availability. At general availability, the automation opens a ticket asking product marketing to confirm or set it, and changes nothing itself.
5. **Slugs never change and former names are never deleted.** A changed slug breaks links and can make a rename look like a new feature. Former names keep old searches landing in the right place.

## How other tools use it

The registry is read by every tool that names a feature, so a name decision is made once and followed everywhere.

- **Ticket and digest titles** use the registry's slug and published name, so a rename does not create a duplicate ticket.
- **The staleness audit**, a scheduled check that flags wiki pages likely to be out of date, treats "renamed after this page was last edited" as its strongest signal that a page is out of date, because the title or text almost certainly carries the old name.
- **The release-readiness check**, which tells product managers what a release still owes before launch, joins each feature's roadmap entry to its tracker project through the registry. It reads the registry and never edits it; renames belong to the automation that detects them.

## Trade-offs and limits

- **The published name can lag engineering on purpose.** Customers see a name only after a person sets it, which can mean a short period where internal and public names differ.
- **Propagation is still manual.** The rename ticket lists every place to update; a person makes the changes. Automating the edits would be faster, but it would also let a tracker rename rewrite public text with no review.
- **It only covers tracked work.** A feature that never had a tracker project has no row, so its name is governed only by the style guide.
- **It depends on review.** Pull requests to the human columns need a reviewer. A row with no lead PM gets no PM review, and the run report says so.
