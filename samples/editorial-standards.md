# Editorial standards for AI-assisted documentation

**Type:** Sample: an editorial standard and how it is enforced
**When:** November 2026
**Author:** Kathryn Collins
**Prepared for:** [Technical Editor, Editorial Publishing, Anthropic](https://job-boards.greenhouse.io/anthropic/jobs/5443997008)

## What this shows

Editing judgment written down so a writer, a reviewer, a scanner and a model all apply it the same way: severity tiers that leave correct uses alone, before and after rewrites, separate drafting and evaluation, and a limits section on what a standard cannot guarantee.

## Summary

I wrote and maintain the house editorial standard that every BigPanda technical doc must meet, whether a person or an AI model drafts it. People apply it, a deterministic scanner checks the countable parts, and a separate model evaluates drafts against it. One principle governs every rule: **constrain phrasing, never substance.** No rule may cost a reader a fact, a caveat or a step.

Portfolio note: excerpted and lightly generalized from the internal standard. Product-specific examples are simplified. The Before column keeps the habits it corrects, including dashes, on purpose.

## Why it exists

Documentation only works if readers believe it. Once a reader notices prose that sounds generated, they start to doubt the facts inside it, including the correct ones.

AI drafting made that risk constant. Models produce fluent text with recognizable habits: long dashes as all-purpose connectors, "you can" in front of every capability, and marketing verbs that say nothing specific. The standard names those habits so a writer, a reviewer and a scanner can all find them the same way.

## Blockers vs. warnings

Rules come in two severities, because a rule that is almost always right is different from one that is often right.

| Severity | Examples | What happens |
| --- | --- | --- |
| Blocker | Long dashes in prose, the buzzword list, stock AI phrases, hedged capability verbs ("is designed to"), repeated sentence openers | Fixed before delivery. These are almost never right in a technical doc. |
| Warning | More than one "you" per paragraph; the words "simply", "just" and "ensure" | Flagged for a person to judge. A doc can ship with warnings and needs no justification. |

The warning tier exists because published pages use those words correctly all the time. Making them blockers would push writers to remove good sentences to satisfy a checker. Severity keeps the editor's judgment where it belongs.

## Before and after

Each rewrite replaces a habit with the specific thing that happens. The dash rule shows the method: a dash is replaced by whatever mark does the job the dash was doing, not by habit.

| Rule | Before | After |
| --- | --- | --- |
| Dash before a list | Two fields are required — `source_system` and `check`. | Two fields are required: `source_system` and `check`. |
| Dash before an aside | The analyzer — which reads change events — flags the likely cause. | The analyzer reads change events and flags the likely cause. |
| Dash in a procedure | Save the rule — it applies on the next ingest. | Save the rule. It applies on the next ingest. |
| "You can" before a capability | You can configure the timeout in Settings. | Configure the timeout in Settings. |
| Reader as subject | You'll see a confirmation when the sync completes. | A confirmation appears when the sync completes. |
| Vague capability | You are able to map up to 50 fields. | The mapper supports up to 50 fields. |
| Marketing verb | Leverage the query language to filter alerts. | Use the query language to filter alerts. |

"You" stays where it carries meaning, such as a permission the reader needs: "You need Admin permissions to edit this setting."

## Naming: the product vs. how people use it

An AI assistant often has two names: the formal product name on contracts and access pages, and a short name people use when they talk to it. Mixing them confuses readers about whether they are reading about the product or about an interaction.

The rule I set separates the two:

- **Titles, headings and anything about the product itself** (access, licensing, setup) use the formal name: AI Incident Assistant.
- **How people engage with it** uses the short name: "Tag Biggy in the incident channel."
- **First mention on a page** introduces both: "BigPanda AI Incident Assistant, known as Biggy." The short name is used after that.

The rule is being written into every writing skill as well as the style guide, so the product reads as one thing across docs, release notes and in-app text.

## Who checks what

No single check is trusted alone, and nothing grades its own work.

1. **Drafting.** A writer, or an Opus-class model following the standard, produces the draft.
2. **Deterministic scan.** A script counts the mechanical tells: dashes, blocklisted words, "you" inside numbered steps, repeated openers. It skips code, URLs and review flags so real technical strings are not flagged.
3. **Separate evaluation.** A Sonnet-class model, in a separate call from the drafter, grades the draft against the standard. The drafting model never evaluates its own output.
4. **Human review.** A writer resolves warnings, fact-checks with engineering and approves. Any claim that could not be verified carries a visible `[VERIFY]` flag until someone confirms it.

If a run cannot use the intended models, the run report says so. It never claims a check happened when it did not.

## Limits

The standard makes prose trustworthy to read; it cannot make it true.

- **The scanner counts words, not meaning.** A draft can pass every check and still be wrong. Accuracy depends on review with the engineers who built the feature.
- **Clean text can hide a missing caveat.** That is why the governing principle forbids cutting substance to satisfy a rule, and why reviewers check what is absent as well as what is present.
- **Warnings rely on judgment.** Two good editors may resolve the same warning differently. The standard accepts that rather than forcing a false precision.
