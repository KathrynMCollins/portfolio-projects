# Release guides consolidation: a content migration with nothing deleted

**Type:** Content migration and content management, with structural quality checks
**When:** September to October 2026
**Tools:** Confluence, Markdown, Python structural checker, a nightly sync to an internal site, redirect map, Linear, Claude Code (Claude Opus and Sonnet models)
**Prepared for:** Content management and technical writing roles

## What this shows

A large content migration run as an editorial operation: inventory first, a folder model readers can predict, merges into absorbing pages, nothing deleted, old links kept working and every result checked against written structural rules. Where sources disagreed, the disagreement stayed on the page for its owner to settle. Claude Code ran much of the migration under my direction: I set the rules, approved each step and reviewed the results.

## The problem

Technical release guides are the internal pages that tell sales, support and services teams what a feature is, where it stands and how to use it. Every audience page on the internal site is generated from them. A live read in mid-September found 77 guide pages. Many covered small slices of one capability, some described the same work with different statuses or owners, and one product area had no folder of its own. A reader could find several pages for one capability, and a fix in one guide could leave its siblings unchanged.

## What I did

### 1. Took inventory and set the target model

- Read the guide tree, recorded each page and what it held, and mapped every guide to one of seven product-area folders that match the product-area values the site and its validators already used.
- Added a missing product area to every place it was enforced (schema, validators, sync, checker and templates) before moving anything.

### 2. Moved and merged into absorbing pages

- Moved 28 pages into their folders, then merged 54 guides into 14 absorbing pages, some new, some retitled. The result was 38 guides in 7 folders, against a target of about 38.
- Placed each absorbed source as a subsection under the release plan, because the checker blocks non-standard top-level headings.
- Kept each page's identity table about its own headline feature. In the pilot, one page briefly took on the status of its most advanced part, so I reverted it.

### 3. Archived as pointers instead of deleting

- Every merged source was archived as a one-line pointer to the page that absorbed it, never deleted. Archive titles name the target and the old name, because titles must be unique in the space and the old suffix would have caused the guides to register again.
- Turned off the merged sources in the sync configuration and removed their resources and index entries, so the site stopped showing retired guides.

### 4. Kept old links working

- Added 40 redirects so old tile links and bookmarks land on the absorbing page, and taught the site's link checker to follow them.
- A follow-up pass on technical and sales enablement guides repointed 28 links on 13 pages, archived 17 more sources as pointers and relinked 48 feature tiles straight to their absorbing guides.

### 5. Checked structure against written rules

- Every absorbing page passed the release guide checker's first 13 structural checks. They cover required frontmatter, a product area from a fixed list, an audience label, a slug pattern, canonical section headings, the title suffix, no long dashes in prose and a summary that does not repeat the excerpt.
- Further checks cover the identity table: required rows, status values from fixed lists, a generally available feature that is not marked internal-only, and archive markers that agree with the page title.

### 6. Defined what each guide owes at each stage

- Each guide owes a fixed set of sections at each stage, and the stages are cumulative. A proof of concept owes a summary, a lead, a channel for questions and what works today. A design-partner stage adds a dated milestone, program status, who it is for and the problem. Release-ready adds, among other rows, prerequisites, demo setup, FAQs and a standard sales status. General availability adds, among other rows, customer docs, enablement material and commercial copy.
- The issue tracker decides the stage. Asking only for what a stage owes cut the first sweep to 60 asks across 25 in-development features, against 524 if every row were asked of every feature.

### 7. Kept contradictions visible

- Where sources disagreed, both versions stayed side by side with a `[VERIFY]` marker and the owner named. Examples include a project shown as canceled on one page and active on another, two different rollover dates, beta against general availability, and two different lead product managers.
- In the follow-up pass, one model drafted the merged pages and every source got a staleness verdict from a second model before it was folded in. One page the verdict marked as the only current home for a how-to was kept, not archived.

## Results

- **77 guide pages in mid-September, 38 guides in 7 product-area folders after the October consolidation**, with every source preserved as a pointer. [guide count on the day the restructure started]
- **40 redirects** plus a link sweep, so old tile links and bookmarks keep working.
- **Every absorbing page passed the structural checks**, and the nightly sync ran green with the merged guides on the site in the right product area.
- Open action items were listed in a run report with owners. They include three pages to archive that agent permissions blocked, inline comments left unanchored when their page became a pointer, statuses to confirm with product managers, docs tickets to file and page labels that could not be applied without a tool.

## Limitations

- The structural checks confirm shape, not truth. The `[VERIFY]` items wait on their owners.
- The keep-or-archive decision on the pointer pages is still open. A later staleness audit stopped spending effort on them by skipping the archive folders.
- [metrics] Reader time to find the right guide is not measured.

## What I'd highlight

- **Nothing deleted:** pointers and redirects meant the migration could be undone page by page and no reader hit a dead end.
- **Rules before moves:** the folder model, heading rules and checker were set first, so every merge was checked the same way.
- **Contradictions surfaced, not resolved by guesswork:** the person who owns the fact settles it.

Related: the [doc impact digest](../doc-impact-digest/README.md) reads these guides and flags what needs updating, and [feature name governance](../../case-studies/feature-name-governance.md) covers the naming rules applied during the merges.

Details are generalized and identifiers removed. No internal page IDs, tickets, channels, people other than the author, or unreleased feature details are included.
