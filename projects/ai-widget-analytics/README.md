# Analytics framework for a docs AI assistant

**Type:** Documentation management, with content strategy and analytics
**When:** October 2026
**Tools:** Transcript analysis, Google Analytics 4 data, Python, Claude Code
**Prepared for:** [Technical Editor, Editorial Publishing, Anthropic](https://job-boards.greenhouse.io/anthropic/jobs/5443997008)

## What this shows

Stating limits plainly, and disclosure and confidentiality controls. The analysis says what its data can and cannot support, the framework requires sensitive transcript content to be redacted before storage, and customer identifiers were removed before the work was shared. The framework is written for leadership and the docs team at once.

## The problem

The docs team planned to add an AI assistant widget to a public technical documentation site and needed to decide how to measure it before choosing a vendor.

The obvious measure, number of conversations, turned out to be misleading. In the only real usage data available (several hundred conversations from an in-product support assistant), one conversation record was sometimes one question, sometimes several, and sometimes half of a question the user had restarted in a new thread. Vendor "deflection" benchmarks measured a different kind of bot and audience, and couldn't be used.

## What I did

### 1. Analysed the evidence, and its limits

- Analysed the support assistant's transcripts for thread length, what follow-up messages actually contained, escalation, topic mix and which docs pages the assistant relied on.
- Used older site analytics as a baseline for page traffic and the long tail of rarely viewed pages.
- Stated up front what the data could and couldn't support: support chat isn't docs chat, the traffic data was dated, and the transcripts had no per-message timing.

### 2. Turned the findings into design decisions

- **Most threads were one question, but a meaningful minority covered several.** So the framework measures individual goals, not conversations.
- **Most extra turns came from the assistant asking for clarification, not the user digging deeper.** So depth caused by the bot is tracked separately from depth caused by the user.
- **Users often restarted instead of continuing.** So threads from the same person on the same topic are joined into one journey, so restarts aren't counted as new demand.
- **The chance of escalation rose sharply at the second turn.** That makes the second turn the point to offer a human handoff.

### 3. Designed the framework

- A four-level model: **turn → goal → thread → journey**, with the goal as the main unit for every headline metric.
- Repeatable rules for splitting a thread into goals, with thresholds kept as settings to re-tune on real docs-site data.
- A five-type thread taxonomy (lookup, guided, laboured, project, non-question). "Laboured" threads, where the assistant circles without resolving the question, are flagged as the main failure to review.
- A vendor-neutral event schema the widget must emit, so the measurement survives a vendor change.
- A four-tier metric tree led by two numbers for leadership: **Goal Resolution Rate**, which requires positive evidence of success, and **Coverage Gap Rate**, which turns unanswered questions directly into a docs backlog.
- Content metrics that give citations equal weight with pageviews. These include "load-bearing" pages that get little traffic but are cited often, so they shouldn't be deleted.
- A weekly, monthly and quarterly review rhythm, and a three-phase classification plan: rules at launch, an AI labeller next, and ongoing checks against human labels.

### 4. Built in governance and launch risks

- Measured how often transcripts contained sensitive content, and required redaction before storage, separate stores with an audit log, and limited retention.
- Removed customer identifiers from the analysis before it was shared.
- Flagged risks specific to the docs site: answers citing the wrong regional or language version, citations to unpublished drafts, answers containing code that fails silently, questions about a customer's own environment that no doc can answer, and pageviews falling because the widget works.

## Results

- A draft framework ready for stakeholder review, with **eight concrete next steps**, including adding the event schema to the vendor requirements before selection.
- A measurement model that replaces vanity counts (conversations, messages, a single deflection rate) with metrics that create docs work.
- A documented list of gaps in the analysis, so nobody treats the framework as finished.

## Limitations

- The evidence came from an in-product support assistant, not docs-site conversations, so thresholds need re-tuning on real docs data.
- Site traffic data was dated, and the transcripts had no per-message timing.
- This is a draft for stakeholder review and was not yet in use.

## What I'd highlight

- **Questioning the obvious metric:** showing with data why "conversations" wasn't a usable number.
- **Measurement that creates work:** every main metric points to a specific action for the docs team.
- **Honest about the evidence:** limits and gaps are listed next to the conclusions.

Details are generalized and identifiers removed. No customer names, transcript content, internal URLs or proprietary data are included.
