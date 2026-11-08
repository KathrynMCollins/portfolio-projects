# Doc impact digest: automated documentation triage from engineering work

**Type:** Documentation management, with process design and automation
**When:** September to October 2026
**Tools:** Linear, Confluence, Slack, Python, TypeScript, a serverless host, GitHub Actions, Claude (AI audit step), Architecture Decision Records
**Prepared for:** [Technical Editor, Editorial Publishing, Anthropic](https://job-boards.greenhouse.io/anthropic/jobs/5443997008)

## What this shows

Applied safety for a deployed AI agent, and writing about its own failures. The AI's role is limited in two places: by design it makes only three judgement calls, and token and repository permissions limit its writes to its own folder, so the limits hold even if the instructions are misread. Version 2 fixed four defects found in the digest's own run logs.

## The problem

Product changes reached the docs team too late, or not at all. Engineering work moved through the issue tracker in hundreds of tickets, and a writer could only find out what needed documenting by reading them by hand. Features were renamed partway through, and the old names stayed in page titles, tickets and CMS topics. Release-ready work shipped without docs review, and nobody owned the record of customer-visible bug fixes.

## What I did

### 1. Designed the digest as a process

- Defined two recurring passes: a **daily "started" pass** that flags work as it enters progress, so writers get lead time, and a **weekly "completed" pass** that catches anything that shipped without docs review.
- Planned project-first: tickets inside an unreleased project roll into that project's doc plan instead of being reviewed one by one, so the noise drops sharply.
- Defined a **stage ladder** for each project, from early prototype through beta to general availability. Each docs stage (Watch, Planned, Drafting, Review, Published) triggers a specific action: a ticket in the docs queue, a draft starter, or a Slack notice when a project becomes release-ready.
- Added a **monthly bug fix log**, so customer-visible fixes are recorded in one place.

### 2. Solved the naming problem

- Created a **feature name registry**: people own the published name, each feature has a fixed ID, and older names are kept as aliases.
- A rename is treated as an event: the digest flags every place the old name still appears and opens a "name drift" ticket, so nothing is silently retitled.

### 3. Made it safe and testable

- Separated rules from access. A deterministic pipeline holds every rule as testable code; the scheduled task supplies the access and performs the writes. AI is used only for three judgement calls: auditing an issue, writing bug-fix sentences and summarizing a project.
- Moved the working state into version control, with **one commit per run**. Write access is limited to the digest's own folder.
- Wrote **architecture decision records** for each major choice (access, where the digest runs, how state is stored, how content is published), and took them through **security review**.
- Ran the new hosted version alongside the original to check that both produce identical results.
- Wrote an operations runbook covering staged deploys, rollback and recovery drills.

### 4. Improved it from its own run logs

- Version 2 fixed four defects found in the digest's own logs: orphaned names after renames, dated milestones that were invisible inside larger projects, a release-ready gate that never fired, and inconsistent ticket naming. It also included a one-time backfill that gave every tracked project a docs ticket without creating duplicates.
- Version 3 replaced long ticket bodies with links to one stored overview per project, so tickets stay short and the reasoning stays in one place.

## Results

- Engineering work is **triaged for docs impact automatically**, at the project level, with tickets in the docs queue and a Slack notice only when a project becomes release-ready.
- A **single source of truth for feature names**, with renames flagged instead of left behind.
- **Every rule is covered by automated tests**, and each run leaves a commit and a report that can be audited.
- Security review of the design and a staged rollout.

## Limitations

- The digest flags work and opens tickets; a writer still decides what each change needs.
- [metrics] Reductions in missed or late docs are not yet measured.

## What I'd highlight

- **Docs as part of the release process:** writers hear about work when it starts, not after it ships.
- **Governance built in:** decision records, security review, people-owned names and AI kept to clearly defined judgement calls.
- **Treated as a product:** versioned releases fixed defects found in its own logs.

Details are generalized and identifiers removed. No internal tickets, project names, people or customer information are included.
