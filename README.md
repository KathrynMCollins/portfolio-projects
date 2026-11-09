# Portfolio

Kathryn Collins, Senior Manager of Content Operations at BigPanda. I lead documentation and knowledge programs: I size what a team can carry and make the case for what it needs, decide where content lives and who owns it, and build the review and publishing processes that keep docs accurate as products change. AI tools are part of that work, held to the same standards and human review as everything else. [About me, experience and LinkedIn](about.md).

## Pieces

The pieces are grouped into two reading paths: strategy and leadership, then writing, editing and content management.

### Strategy and leadership

#### [Sizing a documentation capacity gap and making the investment case](case-studies/docs-capacity-and-investment-case.md)
Demand measured from engineering's own tracker, split into three workloads with different fixes, and two options put to leadership with their risks.
Shows the same argument retold for executives, product and engineering leaders and the field, with every figure labeled by confidence.

#### [Decision memos](samples/decision-memos.md)
Four one-page memos rewritten from real proposals and decision records: which capability to staff first, a readiness ladder for release guides, where a source of record lives, and a security gate.
Each states the options, the reasoning and what happened after, or says the outcome is not yet known.

#### [Measuring a documentation program: from monthly workbooks to page-type goals](case-studies/docs-program-measurement.md)
Monthly analytics, an internal survey, release-level comparisons and goals set per page type, kept from 2021 and revised as the questions changed.
Shows which changes the evidence supports, what is not recorded, and how the record later fed the AI assistant analytics framework.

#### [Internal knowledge base designed as a catalog, not a warehouse](projects/pandashare-knowledge-base/README.md)
Information architecture where content stays at its source: a concept format, a source registry with reliability tiers and an audience label on every concept.
Includes decision records, review guides for product and marketing reviewers, and a read-only internal site.

#### [Release guides consolidation: a content migration with nothing deleted](projects/release-guides-consolidation/README.md)
38 guides in seven product-area folders by October, with every merged source kept as a pointer and old links redirected.
Shows structural checks, a readiness ladder for what each guide owes at each stage, and contradictions kept visible for their owners.

#### [Feature name governance across docs, product and marketing](case-studies/feature-name-governance.md)
Naming treated as disclosure: one owner per release stage, a record of every rename, and no automated step that can set the name customers see.
Shows a naming process designed to stay consistent across teams.

#### [Security evaluation for moving an internal knowledge base](case-studies/security-evaluation.md)
A docs platform proposal turned into a document security and leadership reviewers can decide on: access options and their fit, recommendations, a pre-launch checklist and the questions only security can answer.
Recommends keeping public and internal docs on separate platforms so nothing reaches the public without human review.

#### [Doc impact digest: automated documentation triage from engineering work](projects/doc-impact-digest/README.md)
Engineering work is triaged for docs impact when it starts and after it ships, and each docs stage produces a ticket, a draft or a notice.
Includes the Feature Name Registry, decision records, security review, and fixes drawn from its own run logs.

### Writing, editing and content management

#### [Release documentation in a component CMS](projects/cms-release-docs/README.md)
Release docs written while the release was moving, with an ambiguous support statement settled with the product owner on record.
Nothing reached readers before it was checked.

#### [API reference cleanup and docs-as-code pipeline](projects/api-docs-cleanup/README.md)
Facts checked with engineering, public and internal content separated, and every change approved before it went live.

#### [Editorial standards for AI-assisted documentation](samples/editorial-standards.md)
The house standard every doc meets, whether a person or a model drafts it: severity tiers, before and after rewrites, and who checks what.
Shows editing judgment written down so it holds across writers, scanners and models.

#### [AI assistant skills for a technical documentation team](projects/tech-docs-skills/README.md)
A long style guide turned into core rules and 14 doc-type templates applied on every draft, with every run ending in owned action items.
Shows style governance across a suite of skills, with drafting and evaluation on separate models and a person deciding every outcome.

#### [Analytics framework for a docs AI assistant](projects/ai-widget-analytics/README.md)
A measurement model that counts goals instead of conversations and turns unanswered questions into a docs backlog.
Written for leadership and the docs team at once, with redaction rules for transcript data and the evidence's limits stated.

#### [Self-regenerating docs pipeline: system design and prototype](projects/docs-pipeline-design/README.md)
A technical system explained to decision-makers, with the prototype's limits stated next to its results.

#### [Accessible brand UI kit and design review guide](projects/ui-kit/README.md)
Standards with their reasons written down, and review of upcoming UI before it reaches engineering.

#### [Guardrails for AI-assisted publishing](case-studies/ai-publishing-guardrails.md)
A review and publishing workflow for a monthly customer Bug Fix Log: AI drafts, people verify, approve and publish, and no automated step writes to the public docs.
Includes the controls, a postmortem of a silent failure and the limits kept manual on purpose.

#### [One style standard, five AI models: a pre-registered test](case-studies/model-variance-study.md)
Quality control for a written style standard: hypotheses fixed before any run, every result reported as logged, and the limits stated next to the claims.
Shows how models behave under a written standard, what automated checks miss, and why blind human review still matters.

#### [Talk: Same standard, different readers](talks/same-standard-different-readers/README.md)
Explains to technical writers what changes when a style guide becomes a prompt, using only results from the logged test.
Slides with speaker notes, an outline that cites the source of every number, and stated limits.

#### [Model variance test kit](test-kit/model-variance-kit/)
The pre-registrations, prompts, inputs, scorers, raw logs and results behind the case study and talk.
Shows that every claim can be traced to a logged run.

Internal names, identifiers and figures are removed or generalized throughout; bracketed items are open questions or figures still to be confirmed.

## Structure

- `case-studies/`: longer write-ups.
- `samples/`: work samples.
- `talks/`: talk materials.
- `test-kit/`: the test kit the case study and talk are built on.
- `projects/<project-name>/`: one page per project.

## Contributing notes

- Keep entries brief and outcome-focused.
- Don't include confidential, customer, or internal-only material. Redact or summarize instead.

<!-- Entry template (under a ### reading-path heading):
#### [Project title](path/to/page.md)
What it shows, in one line.
One more line on the evidence.
-->
