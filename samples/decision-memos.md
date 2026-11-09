# Decision memos

**Type:** Sample: four one-page decision memos
**When:** September to October 2026
**Author:** Kathryn Collins

These memos are rewritten from real records: an investment proposal I wrote for leadership and three architecture decision records where I was the decider for an internal knowledge base. They are generalized for a public portfolio, with people, customers, internal names and identifiers removed. Each one shows a different kind of judgment: team structure, process, platform and risk. Options are reconstructed from each record's context where the record does not list them. Where the outcome is not in the record, the memo says so.

## 1. Which capability to staff first

**Status:** partly resolved
**Kind of judgment:** organization and team

**Context.** Documentation was learning about product changes after they shipped. Release coordination had no owner and was being absorbed by me, alongside the AI tooling work the team was measured on. Several major launches were due in the same window. The proposal asked for two new capabilities: product-area documentation with an engineering lean, and release readiness ownership covering release intake and a readiness checklist.

**Options considered.**
- Ask for more writing capacity only. More capacity for the same reactive catch-up work.
- Ask for both capabilities, as a package.
- Ask for both, and state in advance which to take if only one is approved.

**Decision.** Ask for both, and say plainly: if only one is approved, take release readiness. Place it above the documentation team, not inside it.

**Reasoning.** The bottleneck was warning, not writing. Writing capacity added today would do the same late work at higher volume; release readiness changes when the team finds out, and process is the one thing headcount cannot substitute for. Placement mattered as much as the capability: if it reported into documentation, its requests would read as "documentation wants something" and the gate would stay advisory. The proposal also said that a planned shift toward pipeline work depended on the product-area capability, so approving one without the other would quietly cancel the shift. Stating that up front made it a choice rather than a discovery.

**What happened after.** Added writing capacity was approved and is being onboarded, the option this memo argued was not enough on its own. Neither the release readiness nor the product-area capability has been decided in the records I drew on, so whether the warning problem gets solved is still open.

## 2. Ask for what a feature's stage owes, not for everything

**Status:** accepted
**Kind of judgment:** process

**Context.** Release guides tell sellers and field engineers what a feature does and how to position it. A sweep found that most positioned briefs had no business value statement and most in-development features had no dated milestone or program status. Nobody had refused to write these. Nobody had been asked at a moment when the ask made sense. The two existing review steps both corrected what a guide said; neither asked for what was missing.

**Options considered.**
- A flat checklist on every guide. Simple, but it asks a prototype's product manager for FAQs and enablement material the feature will not need this year.
- Leave it to writers to chase each gap by hand.
- A ladder: a fixed, cumulative set of sections owed at each release stage, with the stage read from the issue tracker.

**Decision.** The ladder. The tracker is authoritative for the stage; where tracker and guide disagree, reconciling them is the first ask and the tool changes neither side. Asks appear on each product manager's existing release check page: no new page, spreadsheet or channel.

**Reasoning.** An ask lands when it fits the work in front of someone. Keeping the ladder in one table, checked against the code, means moving a row between stages is a documentation change, not a code change.

**What happened after.** The record was accepted. Its first sweep made about one in nine of the asks a flat checklist would have made. At the time it was written, the tracker read had not yet run, and the page said so instead of hiding it. Later results are not in the record.

## 3. Where the source of record lives

**Status:** proposed
**Kind of judgment:** platform and tooling

**Context.** An internal knowledge base mirrored release guides from the company wiki into git. After a bad sync damaged files on the git side, I recorded that the wiki was the source of record and that nothing in the repository would write to it. Six weeks later the facts had moved: authors drafted in Markdown and pasted into the wiki, the connector they pasted through failed and stopped three workflows at once, and the round trip lost structure such as panels, status lozenges and expand blocks.

**Options considered.**
- Keep the one-way rule. Safe, but every connector outage stops authoring.
- Flip the whole tree to git at once.
- Sync both ways, so edits in either place flow to the other. Rejected: with two writable copies, a bad state on either side can overwrite good edits on the other.
- Move pages one at a time, each with exactly one recorded source, through one guarded publisher.

**Decision.** Proposed the third. A page is either repository-sourced or wiki-sourced, never both, and a test fails if one appears in both lists. One publisher writes. It refuses any page whose live version changed since it last published and any construct its converter cannot map, and it holds any page with inline comments until a person forces that single page; there is no bulk override.

**Reasoning.** The original concern still held: a bad git state must never overwrite a page someone edited by hand. A version check and an allowlist enforced in code keep that protection without a blanket ban. The record also listed the costs, including that wiki editors hit a drift block.

**What happened after.** Not yet known. The record is proposed, and until it is accepted the one-way rule stands.

## 4. Gating a connector before it reads real content

**Status:** proposed
**Kind of judgment:** risk

**Context.** The knowledge base's sync pipeline had never run for real. Every source in its manifest was disabled, and that one flag was doing two jobs: standing in for a security decision and hiding that the pipeline had never been exercised. The daily job ran green dozens of times with nothing happening.

**Options considered.**
- Keep every source disabled until review. Safe, but an unmet gate looks the same as success.
- Enable the sources and treat the security question as settled.
- Separate the two questions: prove the pipeline works without credentials, and write a review gate for the token itself.

**Decision.** Separate them. Credentials live only as repository secrets, scoped to what the manifest names, never in content or logs. The pipeline is read-only against every connector, and any write path needs a new decision record. A security and customer-trust review signs off on token scope and content routing before the first real sync.

**Reasoning.** A flag that produces a green run cannot show that a gate is unmet. With sources enabled and credentials absent, the job now fails loudly and names every unreachable source.

**What happened after.** An early run damaged many files because I enabled the credentials before the fix had merged. It was repaired the next day. The record keeps that history and the lesson that came from it: land the code before the credentials. A later proposal, since implemented, took one pipeline off credentials entirely.
