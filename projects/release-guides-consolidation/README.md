# Release guides consolidation: a content migration with nothing deleted

**Type:** Content migration and content management, with structural quality checks
**When:** September to October 2026
**Tools:** Confluence, Markdown, Python structural checker, a nightly sync to an internal site, redirect map, Linear, Claude Code (Claude Opus and Sonnet models)
**Prepared for:** Content management and technical writing roles

## What this shows

A large content migration run as an editorial operation: inventory first, a folder model readers can predict, merges into absorbing pages (the one page that takes over the content of several others), nothing deleted, old links kept working and every result checked against written structural rules. Where sources disagreed, the disagreement stayed on the page for its owner to settle. Claude Code ran much of the migration under my direction: I set the target structure and rules in a written handoff and reviewed the results.

## The problem

Technical release guides are the internal pages that tell sales, support and services teams what a feature is, where it stands and how to use it. The internal site keeps one record per feature, called a tile, and each tile follows its guide, so the site's audience pages draw on the guides through the tiles. A live read in mid-September found 77 guide pages. Many covered small slices of one capability, some described the same work with different statuses or owners, and one product area had no folder of its own. A reader could find several pages for one capability, and a fix in one guide could leave its siblings unchanged.

## What I did

### 1. Took inventory and set the target model

- Read the guide tree, recorded each page and what it held, and mapped every guide to one of seven product-area folders: the six existing product areas plus one new one.
- Added the new product area to every place product areas were enforced (schema, validators, sync, checker and templates) before moving anything.

### 2. Moved and merged into absorbing pages

- Moved 28 pages into their folders, then merged 54 guides into 14 absorbing pages. Six of the 14 were new pages and several others were retitled. When the work was done, the seven folders held 38 guides.
- Placed each absorbed source as a subsection under the page's release plan (the section that lists milestones and what each one delivers), because the checker blocks non-standard top-level headings.
- Kept each page's identity table (the summary table at the top that states status, sales status, owner and access) about its own headline feature. In the pilot, one page briefly took on the status of its most advanced part, so I reverted it.

### 3. Archived as pointers instead of deleting

- Each of the 54 merged sources was archived as a one-line pointer to the page that absorbed it, never deleted.
- Archive titles start with "MERGED", then the absorbing page and the old name. Confluence requires unique titles, and dropping the old guide suffix stops the pipeline from picking the pointers up as new guides.
- Turned off the merged sources in the sync configuration and removed their resources and index entries, so the site stopped showing retired guides.

### 4. Kept old links working

- Added 40 redirects so old tile links and bookmarks land on the absorbing page, and taught the site's link checker to follow them.
- A follow-up pass on technical and sales enablement guides archived 17 more sources as pointers, repointed 28 links on 13 pages and relinked 48 tiles straight to their absorbing guides.

### 5. Checked structure against written rules

- Every absorbing page passed the release guide checker's first 13 structural checks. They block retired section headings, a summary that repeats the excerpt, FAQ answers that restate the page, a date in the frontmatter (the metadata block at the top of the file) that disagrees with the identity table, program status values outside the agreed list, non-standard top-level headings and long dashes in prose. They also require frontmatter, a product area from a fixed list, an audience label, a slug pattern, a stage from nine labels and a sales status from five values.
- Further checks cover the identity table's required rows, the title suffix, a generally available feature marked internal-only, a document owner named as the product lead and archive markers that disagree with the page title.

### 6. Defined what each guide owes at each stage

- Each stage owes more sections than the one before, from a summary and a lead at proof of concept to customer docs and enablement material at general availability. The issue tracker decides the stage.
- Asking only for what a stage owes cut the first sweep to 60 asks across 25 in-development features, against 524 if every row were asked of every feature.

### 7. Kept contradictions visible

- Where sources disagreed, both versions stayed side by side with a `[VERIFY]` marker and the owner named. Examples: one project shown as canceled on one page and active on another, two different dates for the same rollover, two different release stages for the same feature, and two different lead product managers for the same product.
- In the follow-up pass, one model drafted the merged pages and every source got a staleness verdict from a second model before it was folded in. One page the verdict marked as the only current home for a how-to was kept, not archived.

## Results

- **38 guides in 7 product-area folders** after the October consolidation, with each merged source kept as a pointer.
- **40 redirects** plus a link sweep, so old tile links and bookmarks keep working.
- **Every absorbing page passed the structural checks**, and the nightly sync ran green with the merged guides on the site in the right product area.
- Open action items were listed in a run report with owners. They include three pages still to archive by hand (agent permissions blocked them), page comments no longer attached to text because their page became a pointer, statuses to confirm with product managers, docs tickets to file and page labels still to apply.

## Limitations

- The structural checks confirm shape, not truth. The `[VERIFY]` items wait on their owners.
- The keep-or-archive decision on the pointer pages is still open. A later staleness audit stopped spending effort on them by skipping the archive folders.
- [metrics] Reader time to find the right guide is not measured.

## What I'd highlight

- **Nothing deleted:** every source stayed recoverable as a pointer, and redirects kept old links working.
- **Rules before moves:** the folder model, heading rules and checker were set first, so every merge was checked the same way.
- **Contradictions surfaced, not resolved by guesswork:** the person who owns the fact settles it.

Related: the [doc impact digest](../doc-impact-digest/README.md) reads these guides and flags what needs updating, and [feature name governance](../../case-studies/feature-name-governance.md) covers the naming rules applied during the merges.

Details are generalized and identifiers removed. No internal page IDs, tickets, channels, people other than the author, customer information or unreleased feature details are included.
