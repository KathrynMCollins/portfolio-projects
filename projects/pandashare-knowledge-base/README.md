# Internal knowledge base designed as a catalog, not a warehouse

**Type:** Content management and information architecture, with governance and an internal site
**When:** June to November 2026
**Tools:** Markdown with YAML frontmatter (Open Knowledge Format), Git and GitHub, Confluence, Python and Node validators, a static site, Claude Code, Architecture Decision Records
**Prepared for:** Content management and technical writing roles

## What this shows

Information architecture for a company knowledge base where most of the knowledge lives somewhere else. The repository holds the map: where each topic lives, who may read it, how reliable the source is and who owns it. The canonical content stays in its source systems. Major design choices are written down as decision records, and the review process for product managers and product marketing is written as a guide a non-technical reviewer can follow.

## The problem

BigPanda knowledge was spread across documentation, Confluence, shared drives, Slack, the issue tracker and several AI tools. People and agents hunted across all of them. A sales engineering lead reported that AI search tools often got program, migration and deadline details wrong, because those updates were scattered across chat. Copying content into one place would have created drift, bloated the repository and pulled customer-sensitive material into git. There was also no single answer to "which systems does this pipeline read from, and under what rules?" Three separate configuration files named sources, with no shared key between them.

## What I did

### 1. Set the model: a catalog of pointers

- An engineering colleague proposed an open, vendor-neutral format: one Markdown file per concept, with YAML frontmatter (a metadata block at the top of the file), distributed through git. The decision record is still marked proposed, and the repository follows it. I was consulted on the format and owned most of the decisions that followed.
- The default concept is a reference: a pointer to the canonical source plus the access path to reach it, with only enough curated context to judge relevance. A distilled copy is cached only when the source is public and the copy earns its keep.
- Frontmatter carries `type`, `title`, `label`, `resource`, `access`, `materialized`, `provenance`, `freshness` and `reviewed_at`, so reviewers and scheduled checks can see where every concept came from and how recent it is.

### 2. Built a source registry with reliability tiers

- Made one registry file per source system, covering every system the pipeline touches, including publish targets, so the registry answers "where does this go" as well as "where does this come from".
- Ranked sources by reliability in three tiers: managed (curated), communal (communally edited sources of record) and raw (uncurated capture and system data).
- Split tiers inside a single system where the workflow called for it. In Confluence, the knowledge base section is managed and everything else is communal. In the shared drive, a review folder is communal, a ready-to-share folder is managed and the rest is raw.
- Added a machine-readable category taxonomy with stable slugs, so one vocabulary routes release guides, the site's hierarchy view and the public docs structure.

### 3. Classified every concept by audience

- Every governed concept carries a `label`: `public`, `internal` or `customer-facing`. Internal content never goes to a public store, and customer-facing content may include customer context but never reaches a public file.
- Each source also has a default label for content pulled from it. Raw capture sources default to `customer-facing`, so "never route raw customer data to the public" is a field, not folklore.
- A repository check runs in CI and again before the nightly sync commits. It fails on a likely secret in any file, and on a customer name in any `public`-labeled file, matched against a term list generated from the CRM. Customer names in internal files are allowed on purpose.
- Labels are migrated as a ratchet, a rule that only tightens: an unlabeled file raises a warning, and once a file is reviewed and mapped, a missing label is an error.

### 4. Made git the source of record, and kept the direction clear

- Git is the source of truth for what is authored in git. Search and graph indexes are derived and can be rebuilt from git at any time, so a wiped index is an inconvenience, not a loss.
- For release guides that product managers author in Confluence, I decided the opposite: Confluence is the source of record and git holds a mirror that the repository never writes back. The trigger was an early sync that damaged 70 files in git. They were restored from git history, and pushing that state back would have overwritten edits the product managers had made since.
- A later proposal moves pages into the repository one at a time, with a version check that skips any page someone edited by hand. It waits on security review.

### 5. Wrote decision records as documentation

- The repository holds 26 decision records, and I am the decider or a co-decider on 21. Each one states the context, the decision, its costs and the alternatives rejected. Records are reviewed in pull requests, not in meetings, and an accepted record is changed only by a new one that supersedes it.
- Planned records are listed as reserved slots with a scope, and the index says not to invent their content to satisfy a reference.

### 6. Wrote review guides for product and marketing reviewers

- The product manager release check asks two questions per feature: is it available to customers, and is it available to internal teams. It asks them only on features whose guides have something flagged, so a sheet stays short.
- The product marketing Field check asks whether the Field (the sales and customer-facing teams) is seeing the right thing, one sheet per product line, with each flag explained in plain words and the fix routed to where it lands.
- Both guides are walkthroughs for the knowledge team to run live with the reviewer. Nothing on the review pages edits the source; a "needs work" answer records the flag, and the edit still happens at the source.

### 7. Shipped a read-only internal site

- Built a static internal site organized by audience: sellers, technical sellers, account teams, support, product and engineering, leadership, and a content-health view for documentation managers.
- Set a definition of done for each hub: it answers its audience's question above the fold, every figure is traceable through a Method tab (a tab on each hub that states the rule behind each number), and missing data reads as a gap on the page rather than being hidden.
- Set the site to block search engine and AI crawler indexing, and made the HTML sanitizer fail closed.

## Results

- One registry answers source, tier, access and audience questions for people and agents.
- A catalog audit found that the site mirrored Confluence exactly and the errors were in the source guides: 21 of 59 guides marked a feature generally available and internal-only at once. The owner decision that generally available means sellable turned that into a specific correction list.
- A generated review list tracks 609 open content items across 77 features, grouped by how incomplete each feature is and by gap type.

## Limitations

- Several decision records, including the security review gate for real-data connectors, are still proposed rather than accepted.
- The category taxonomy is a working draft and its slugs may change.
- [metrics] Time saved for readers and reduced search effort are not measured.

## What I'd highlight

- **Catalog over warehouse:** content stays at its source, so there is less to drift and customer data stays out of the repository by default.
- **Audience as a field:** classification is enforced in frontmatter and in CI, not by convention.
- **Decisions written down:** the reasons behind the structure survive staff changes and can be challenged in review.

Related: [Doc impact digest](../doc-impact-digest/README.md) runs on this repository, and [feature name governance](../../case-studies/feature-name-governance.md) covers the naming registry the readiness check reads.

Details are generalized and identifiers removed. No internal page IDs, tickets, channels, people other than the author, customer information or unreleased feature details are included.
