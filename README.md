# Portfolio

Kathryn Collins, Senior Manager of Content Operations at BigPanda. I lead documentation and knowledge programs: I size what a team can carry and make the case for what it needs, decide where content lives and who owns it, and build the review and publishing processes that keep docs accurate as products change. AI tools are part of that work, held to the same standards and human review as everything else.

## Pieces

The pieces are grouped into two reading paths: strategy and leadership, then writing, editing and content management.

### Strategy and leadership

#### [Sizing a documentation capacity gap and making the investment case](case-studies/docs-capacity-and-investment-case.md)
Demand measured from engineering's own tracker, split into three workloads with different fixes, and two options put to leadership with their risks.
Shows the same argument retold for executives, product and engineering leaders and the field, with every figure labeled by confidence.

#### [Decision memos](samples/decision-memos.md)
Four one-page memos rewritten from real proposals and decision records: which capability to staff first, a stage-based readiness process, where a source of record lives, and a security gate.
Each states the options, the reasoning and what happened after, or says the outcome is not yet known.

#### [Feature name governance across docs, product and marketing](case-studies/feature-name-governance.md)
Naming treated as disclosure: one owner per release stage, a record of every rename, and no automated step that can set the name customers see.
Shows a naming process designed to stay consistent across teams.

#### [Security evaluation for moving an internal knowledge base](case-studies/security-evaluation.md)
A tooling proposal turned into a document a security team can decide on: access options and their fit, recommendations, a pre-launch checklist and the questions only security can answer.
Recommends keeping public and internal docs on separate platforms so nothing reaches the public without human review.

#### [Doc impact digest: automated documentation triage from engineering work](projects/doc-impact-digest/README.md)
Applied safety for a deployed AI agent: its role is limited in its instructions and its writes are limited by access.
Includes security review, decision records and fixes drawn from its own run logs.

#### [Internal knowledge base designed as a catalog, not a warehouse](projects/pandashare-knowledge-base/README.md)
Information architecture where content stays at its source: a concept format, a source registry with reliability tiers and an audience label on every concept.
Includes decision records, review guides for product and marketing reviewers, and a read-only internal site.

#### [Release guides consolidation: a content migration with nothing deleted](projects/release-guides-consolidation/README.md)
38 guides in seven product-area folders by October, with every merged source kept as a pointer and old links redirected.
Shows structural checks, stage-based readiness checks and contradictions kept visible for their owners.

#### [Guardrails for AI-assisted publishing](case-studies/ai-publishing-guardrails.md)
Disclosure and confidentiality controls for a customer-facing log that AI drafts and people publish, with agent permissions enforced in instructions and by scoped access.
Includes a postmortem of a silent failure and the limits kept manual on purpose.

### Writing, editing and content management

#### [One style standard, five AI models: a pre-registered test](case-studies/model-variance-study.md)
Evaluation design and reporting: hypotheses fixed before any run, every result reported as logged, and the limits stated next to the claims.
Shows how models behave under a written standard, what automated checks miss, and why blind human review still matters.

#### [Talk: Same standard, different readers](talks/same-standard-different-readers/README.md)
Explains model behavior to technical writers who don't work with models, using only results from the logged test.
Slides with speaker notes, an outline that cites the source of every number, and stated limits.

#### [Editorial standards for AI-assisted documentation](samples/editorial-standards.md)
The house standard every doc meets, whether a person or a model drafts it: severity tiers, before and after rewrites, and who checks what.
Shows editing judgment written down so it holds across writers, scanners and models.

#### [Model variance test kit](test-kit/model-variance-kit/)
The pre-registrations, prompts, inputs, scorers, raw logs and results behind the case study and talk.
Shows that every claim can be traced to a logged run.

#### [AI assistant skills for a technical documentation team](projects/tech-docs-skills/README.md)
Editorial standards turned into rules a model applies, with drafting and evaluation on separate models and a person deciding every outcome.
Shows Claude in editorial work with human review gates.

#### [Release documentation in a component CMS](projects/cms-release-docs/README.md)
Release docs written while the release was moving, with an ambiguous support statement settled with the product owner on record.
Nothing reached readers before it was checked.

#### [Analytics framework for a docs AI assistant](projects/ai-widget-analytics/README.md)
States what its evidence can and cannot support, and sets disclosure and confidentiality controls for transcript data.
Written for leadership and the docs team at once.

#### [API reference cleanup and docs-as-code pipeline](projects/api-docs-cleanup/README.md)
Facts checked with engineering, public and internal content separated, and every change approved before it went live.

#### [Self-regenerating docs pipeline: system design and prototype](projects/docs-pipeline-design/README.md)
A technical system explained to decision-makers, with the prototype's limits stated next to its results.

#### [Accessible brand UI kit and design review guide](projects/ui-kit/README.md)
Standards with their reasons written down, and review of upcoming UI before it reaches engineering.

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
What it shows for the role, in one line.
One more line on the evidence.
-->
