# Sizing a documentation capacity gap and making the investment case

**Type:** Case study: capacity planning, an investment case to leadership and team design
**When:** August to October 2026
**Author:** Kathryn Collins

## What this shows

Planning and team leadership for a documentation function that fell behind its product. I measured the gap instead of asserting it, split one complaint into three problems with different fixes, put the options to the decision-maker with their risks attached, and told the same argument differently to executives, product leaders, engineering leaders and the field. Every figure carried a label saying how much weight it could bear.

Portfolio note: customer names, people, internal product and team names, tools and dollar figures are removed or generalized. Hours, ratios and counts are as they appear in the source decks.

## The problem

Engineering at BigPanda was shipping faster than the documentation team could follow. The symptoms reached me from every direction: features that went live before their docs, field engineers learning about changes from customers, and finished docs waiting weeks for someone in engineering to confirm them. Feedback I collected from three accounts named the cost as lost trust, unannounced behavior changes and content that existed but could not be found. Two of the three were not asking for more documentation. They wanted notice, and they wanted what existed to be findable.

The team was small, and release coordination had no owner, so it was being absorbed by me alongside the team's tooling work.

## How I sized it

**First pass: planned work against capacity.** The September capacity review put planned feature documentation at about 540 hours a month against about 234 hours of writing capacity: 2.3 times oversubscribed. An earlier quarter view showed the same shape: process fixes could recover about 22% of the quarter's shortfall at no added headcount, and whatever was left would slip into a following quarter that already carried its own load.

**Second pass: what actually ships.** Planned work only counts what reaches a doc plan, so I went to the issue tracker. I harvested every issue across the product teams, kept 12 teams and about 3,900 completed issues since the tracker migration in May, and removed scripted bulk closures (runs of five or more completions within 90 seconds). I hand-labeled a stratified sample of 291 issues, 25 per team, as customer-doc, field-enablement or none, with a complexity tier, then scaled team rates by completions with 95% intervals. Hours used the team's existing forecast constants and validation multipliers by tier. A keyword classifier tried first reached 92% recall but 34% precision, so I discarded it.

That produced three workloads, not one:

| Workload | Size | What kind of problem |
| --- | --- | --- |
| Planned feature docs | about 540 hours a month, 2.3 times capacity | A real headcount problem |
| Generated change | about 300 customer-facing items a month, about 70% with no project; implied load 5 to 7 times the planned figure | Not solvable by headcount: process, ownership and product |
| Internal enablement | about 50 items a month | Docs-owned, mostly two teams |

About 85 items a month of per-customer implementation configuration sat on engineering boards but belonged to the services team by charter, so I showed it only to say where it was filed and excluded it from documentation demand.

The harvest also showed why the team's own tooling could not fix lead time. Our daily digest flagged work when it entered "started", but on the largest team half of issues finished within a day of starting, and on some teams a third to half never passed through "started" at all. Estimates were unused on 80 to 100% of issues. Lead time had to come from projects and releases instead.

**The trust number.** Docs that reached the ready-for-validation gate waited a median of about 35 days (range 5 to 91), and half were still there. Separately, under a "better some than none" policy, about 1 in 3 documents published with no developer or product review. I framed that as the bar any automation had to beat: the status quo was not "reviewed by humans."

## The options

The decision deck went to the R&D leader with a shared foundation and two options, and left the choice to that leader.

**Foundation, either way:** documentation in the definition of done, doc requirements as a project field, customer-facing issues required to have a project, release-level bundling, validation evidence attached by engineering at source, reference generated from schemas, and implementation configuration moved to the team that owns it. Cost: process change and about three to four weeks of docs-team build time.

| | Option A: redistribute authoring | Option B: content engineering pipeline |
| --- | --- | --- |
| What changes | Engineering and product write first drafts; writers review, validate and author narrative, procedures and overhauls | Content compiled from code and schemas; evals and procedure tests run in CI replace editorial review |
| Load | Planned load falls to about 350 to 400 hours a month; the remaining gap is about one writer | About 85% of item volume becomes review or automation |
| Staffing shape | The current team plus one | Two to three content engineers, after a two to three quarter build |
| Risk | Lower; the long tail is only partly covered | Higher; narrative, overhauls and trust depend on eval quality |

A and B were not exclusive: A is where B starts. The team's recommendation, stated separately from the decision deck, was to close the gap now with one writer and Option A's levers, prove the testing layer, and only then decide on B, because weak evals would make B a downgrade. For immediate relief I set out two staffing routes: moving an experienced support engineer across, with no product ramp, or an external hire, with the trade-off that some user-facing language review would shift back to the existing team.

## Retelling it for each audience

The same evidence went to four audiences, each with a different ask.

- **Executives** got the cost of the gap and the plan already committed: a knowledge-share site owned by Product and an automated change-notification bot owned by R&D. Each solution was shown with what it does not solve and what was blocking it (single sign-on for the site, per-repository rollout for the bot). The message was that this unblocks committed work, not a new initiative to fund.
- **Product leadership** got the two automations as one system (a self-updating repository wiki for engineers and coding agents, and a notifier that routes doc-relevant merges to writing, support and marketing) and the team's Claude skills they could use directly.
- **R&D leadership** got the same two automations framed around reducing friction with the field, plus four setup paths per repository so each team could pick one.
- **The field** got no capacity argument at all: where to find product knowledge today, what was coming, and how to save the documentation drafting skill so their drafts arrived closer to house style.

The wider investment proposal had a full version and a plain-language version with identical substance, so a reader who would not read the first still got the whole argument, including what was not yet measurable.

## Labeling claims by confidence

Every number carried its provenance. In the handoff I wrote for building the executive and leadership slides, each claim was marked deck (analyst-derived round numbers from the September review), repo (verified against the knowledge base, its decision records or scripts) or derived (computed from a hand-authored dependency map, exact but only as good as its edges). Anything unmarked was framing, not evidence.

The labels came with instructions that traveled with the numbers: nobody should staff to the 5 to 7 times figure; the build horizon for Option B was the softest number; customer quotes were to be pulled from the source, never paraphrased from memory; and a dependency line that would have implied B first was proposed and declined because it inverted the recommendation. The decks' appendices listed method and weaknesses, and the investment proposal opened its metrics section by saying none of its three headline numbers could yet be measured.

Claude helped. The slide handoff was written so a Claude session with no repository access could build the leadership slides, and the product leadership deck was produced with the team's brand deck skill. The analysis, the labels and the decisions about what to claim were mine.

## The role proposal as part of the plan

The investment proposal treated team design as part of the fix. It described one function with a writing-to-systems gradient rather than writers plus a separate tooling team, and named two new roles: a documentation engineer owning a product area, and a release readiness program role, reporting above the documentation team so its requests would not read as one team's requests. It stated that the senior documentation engineer's shift toward pipeline work and the new documentation engineer were a package: approve one without the other and the shift does not happen. It also said which to take if only one were approved (the readiness role, because it changes the process).

Alongside it I wrote a role definition for my own position as a hybrid manager and builder, with markers of success and concern and the staffing risks to decide explicitly rather than discover later, and a realistic week-in-the-life description of the documentation engineer role: review model, meeting load and how work is split across product areas.

## What was decided

The executive deck records the knowledge-share site and change-notification bot as committed and blocked on dependencies outside the team. The records I drew on do not show a decision on Option A or B, on the additional writer, or on the two proposed roles. That outcome is not known here.

## Limitations

- The tracker's history started at the May migration, so there is no year-over-year view.
- With 25 samples per team, the largest team's estimate is a wide range (580 to 1,100 items) because its volume multiplies sampling error.
- Issue-level hours vary about two times with per-item assumptions, so they are shown as ranges and ratios.
- Large overhauls are invisible at issue level and were counted from projects instead.
- Industry comparisons in the decks were vendor-reported.
- The case sizes the problem and frames the choice. It does not show that either option worked.
