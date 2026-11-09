# Sizing a documentation capacity gap and making the investment case

**Type:** Case study: capacity planning, an investment case to leadership and team design
**When:** August to October 2026
**Author:** Kathryn Collins
**Prepared for:** Content management and documentation leadership roles

## What this shows

Planning and team leadership for a documentation function that fell behind its product. I measured the gap instead of asserting it, split one complaint into three problems with different fixes, put the options to the decision-maker with their risks attached, and told the same argument differently to executives, product leaders, engineering leaders and the field. Every figure in the handoff behind the leadership slides carried a label saying how much weight it could bear.

Portfolio note: customer names, people, internal product and team names, tools and dollar figures are removed or generalized. Figures are rounded or expressed as ratios.

## The problem

Engineering at BigPanda was shipping faster than the documentation team could follow. The symptoms reached the team from every direction: features that went live before their docs, field engineers learning about changes from customers, and finished docs waiting weeks for someone in engineering to confirm them. Feedback I gathered for the review asked less for more documentation than for advance notice of changes and for existing content to be easier to find.

The team was small, and release coordination had no owner, so it was being absorbed by me alongside the team's tooling work.

## How I sized it

**First pass: planned work against capacity.** The September capacity review found that planned feature documentation ran at roughly twice the team's writing capacity. A separate quarter view showed the same shape: process fixes could recover only about a fifth of the quarter's shortfall at no added headcount, and the rest would slip into a following quarter that already carried its own load.

**Second pass: what actually ships.** Planned work only counts what reaches a doc plan, so the analysis went to engineering's issue tracker: thousands of completed issues across the product teams, with scripted bulk closures removed. I hand-labeled a stratified sample of a few hundred issues by documentation need and scaled it up by team, with the uncertainty shown as ranges.

That produced three workloads, not one:

| Workload | Size | What kind of problem |
| --- | --- | --- |
| Planned feature docs | roughly twice writing capacity | A real headcount problem |
| Generated change | most customer-facing change had no project attached; implied load 5 to 7 times the planned figure | Not solvable by headcount: process, ownership and product |
| Internal enablement | a smaller, steady stream | Docs-owned, mostly two teams |

Per-customer implementation configuration sat on engineering boards but belonged to the services team by charter, so it was shown only to say where it was filed and excluded from documentation demand.

The analysis also showed why the team's own tooling could not fix lead time. The daily pass of our doc impact digest (an automated report of tracker work that might need docs) flagged issues when they moved to "started", meaning work had begun. On the largest team about 60 percent of issues finished within a day of starting, about half across the whole stream, and on some teams a third to half never passed through "started" at all. Lead time had to come from projects and releases instead.

**The trust problem.** Docs that reached the ready-for-validation gate, the step where engineering confirms a draft before it publishes, waited a median of several weeks, and half were still waiting. Separately, the team's own estimate was that about 1 in 3 documents published with no developer or product review, under a "better some than none" policy; that share reflects the policy rather than a measurement. I framed it as the bar any automation had to beat: the status quo was not "reviewed by humans."

## The options

The decision deck went to the R&D leader with a shared foundation and two options.

**Foundation, either way:** documentation in the definition of done (a change does not count as finished until its docs are), doc requirements as a project field (product managers state what a project needs documented when it is planned), customer-facing issues required to have a project, release-level bundling, validation evidence attached by engineering at source, and reference generated from schemas. Cost: process change and a few weeks of docs-team build time.

| | Option A: redistribute authoring | Option B: content engineering pipeline |
| --- | --- | --- |
| What changes | Engineering and product write first drafts; writers review, validate and author narrative, procedures and overhauls | Content compiled from code and schemas; evals (automated checks that score generated content) and procedure tests run in CI replace editorial review |
| Load | A modest staffing gap remained | Most item volume becomes review or automation |
| Staffing shape | The current team with a small addition | A dedicated pipeline function of content engineers (people who build and run the pipeline rather than write pages), after a multi-quarter build |
| Risk | Lower; the long tail is only partly covered | Higher; narrative, overhauls and trust depend on eval quality |

A and B were not exclusive: A is where B starts. The deck also carried the team's recommendation: close the gap now with Option A's levers and modest added capacity, prove the testing layer, and only then decide on B, because weak evals would make B a downgrade. For immediate relief I set out staffing routes with the trade-off of each.

## Retelling it for each audience

- **Executives** saw two committed automation projects, each shown with what it does not solve and what blocked it, framed as unblocking committed work rather than funding a new initiative.
- **Product leadership** saw the two automations as one system, plus the team's Claude skills they could use directly.
- **R&D leadership** saw the same automations framed around reducing friction with the field.
- **The field** got no capacity argument at all: where to find product knowledge today, what was coming, and how to save the documentation drafting skill.

The wider investment proposal had a full version and a plain-language version with the same substance.

## Labeling claims by confidence

In the handoff I wrote for building the leadership slides, every claim was marked as coming from the capacity deck, verified against the knowledge base repository, or derived from a hand-authored dependency map; anything unmarked was framing, not evidence. Warnings traveled with the numbers: nobody should staff to the 5 to 7 times figure, the build horizon for Option B was the softest number, and customer quotes were to be pulled from the source rather than paraphrased. The investment proposal's instrumentation section said up front that none of its three headline numbers could yet be measured. Claude helped: the handoff was written so a Claude session could build the leadership slides, and the product leadership deck says it was made with one of the team's Claude skills.

## Team design as part of the plan

The investment proposal treated team design as part of the fix: one function with a writing-to-systems gradient, product-area ownership with an engineering lean, and a release readiness function placed above the documentation team, with a planned shift toward pipeline work depending on the product-area ownership. I also defined how a hybrid manager and builder position and engineering-leaning documentation work fit the team. The reasoning behind which capability to staff first is in the [decision memos](../samples/decision-memos.md).

## What was decided

The executive deck records the two automation projects as committed and blocked on dependencies outside the team. Added writing capacity was approved, and onboarding is under way. That matches the first step of the team's recommendation, though no record names Option A or B as the chosen path. The records I drew on do not show a decision on the proposed team changes.

## Limitations

- The tracker's history was short, so there is no year-over-year view.
- The per-team sample was small, so the largest team's estimate had a wide interval.
- Issue-level hours depend heavily on per-item assumptions, so they are shown as ranges and ratios.
- Large overhauls are invisible at issue level and were counted from projects instead.
- Industry comparisons in the decks were vendor-reported.
- The case sizes the problem and frames the choice. It does not show that either option worked.
