# AI assistant skills for a technical documentation team

**Type:** Documentation management, with style governance and AI-assisted content operations
**When:** September to November 2026
**Tools:** Claude skills (Markdown instructions and reference files), Python, Vale, Git, Linear, Confluence, Paligo, Claude Code
**Prepared for:** Content management and technical writing roles

## What this shows

Claude in editorial work, with people in charge of the result. The house style became rules a model applies every time, drafting and evaluation run on separate models, and every run ends in a report that a person acts on. This is the editing judgment the role needs, written down so it is applied the same way every time.

## The problem

The docs team was starting to use AI to draft, review and maintain documentation, but the output varied with whoever wrote the prompt. The house style guide was long and rarely applied consistently, doc types had no shared templates, AI drafts carried an obvious "AI tone", and nobody kept a record of open questions and follow-ups once a chat ended.

## What I did

### 1. Turned the style guide into a reusable skill

- Built a core technical-writing skill that works as a router. A short main file points to:
  - **Core style rules** applied on every draft.
  - **Rules for removing AI tone**, such as overused dashes, heavy second-person phrasing and buzzwords.
  - **The full style guide**, for rules not in the core set.
  - **14 doc-type templates**, each with its audience, structure, type-specific rules and a worked example. Types include feature pages, integration setup, in-app instructions, landing pages, API content, onboarding guides, troubleshooting and internal references.
- Wrote validation scripts that scan drafts for style and tone problems before delivery, plus a browser-based tone checker for writers.

### 2. Set operating rules that every skill follows

- **Separate drafting from evaluation:** one AI model drafts and a different one grades, so a draft is never graded by the model that wrote it. If the environment can't switch models, the run says so instead of claiming it did.
- **Every run ends with a report:** the outcome, plus numbered action items with an owner, the exact action and whether it blocks release. Nothing actionable lives only in the chat.
- **Tickets land with the docs team first:** issues the skills create start in the docs team's tracker, and a person decides whether to move them.
- **Communication rules:** no narrating the process, plain language, a short summary, and only the items that need a person.

### 3. Grew it into a suite

Built or shaped related skills that share the same rules:

- **Checking docs against the live app,** verifying UI labels and steps against what actually shipped.
- **Feature release guides** in a fixed template, including drafts from transcripts, tickets or notes.
- **Doc impact audits** of channels, tickets, commits and releases, finding changes that make docs out of date, with a recurring digest that flags work as it starts and catches what shipped without docs review.
- **A knowledge-base staleness audit** that sorts pages by risk and files tickets for the ones that are out of date.
- **Live editing in the structured CMS**, with copies, reuse checks and verification.
- **Brand-aligned visuals and course content,** including a UI kit, diagrams, infographics and training course storyboards.

### 4. Kept it maintained

- Kept a changelog per skill, recording why each rule changed.
- Reconciled the version-controlled copies with the installed ones so they didn't drift apart.
- Rolled out cross-cutting changes to every affected skill in one pass. For example, a product naming rule is owned by the core skill and referenced by the others.
- Split large changes when they broke the automated style check in CI, so the check kept running.

## Results

- **About ten coordinated skills**, with the core skill holding 14 doc-type templates and worked examples.
- AI-assisted drafts follow the house style and templates by default, and are checked for style and tone before a person sees them.
- Every run leaves a report with numbered, owned action items, so open questions survive the end of a session.
- The other projects in this portfolio, including the API cleanup, CMS release docs and UI kit, were run through these skills.

## Limitations

- The skills make drafts consistent and checkable; they do not replace a person's review, and every run hands decisions back to a person.
- Separate evaluation depends on the environment offering a second model. When it does not, the run says so instead of grading its own draft.
- Time saved and adoption figures are not included.

## What I'd highlight

- **Style governance that scales:** the style guide is applied every time, not just referenced.
- **Guardrails over trust:** separate evaluation, explicit limitations and required follow-ups make AI output reviewable.
- **Maintained like a product:** changelogs, version control and coordinated updates across the suite.

Details are generalized and identifiers removed. No proprietary style guide text, internal tickets, people or product content are included.
