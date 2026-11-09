# Self-regenerating docs pipeline: system design and prototype

**Type:** Documentation management, with systems design
**When:** September 2026
**Tools:** Playwright, TypeScript, YAML, Zod, Node.js, WebVTT captions, Claude Code
**Prepared for:** Content management and technical writing roles

## What this shows

Explaining a technical system to decision-makers who will not read the code, with the limits of a prototype stated next to its results.

## The problem

Product documentation for a fast-moving web app kept going stale. Screenshots, written procedures and training videos were each hand-made copies of the UI, so each one aged on its own schedule. Nobody found out a page was wrong until a customer or support engineer hit it.

The app already described itself in code: a page registry listing every page with its path, label and permissions, and a set of written user journeys with action, expected-result and verify steps for testing. That structured data wasn't being used for documentation.

## What I did

### 1. Designed the system

- Wrote a system design that treats the app's own page registry and journeys as the source of truth for docs.
- Defined the flow: a short manifest per page, repeatable capture from the running app, extraction of facts from what was captured, AI drafting limited to prose, validators, and publishing through pull requests. Writers review changes instead of rewriting pages.
- Defined classes of drift (cosmetic, structural, content) and what each one triggers. Cosmetic changes can be accepted automatically; structural and content changes open a review.
- Planned two milestones: screenshots and docs first, then annotated explainers, walkthroughs and narrated videos.

### 2. Built a working prototype

- Wrote a manifest format and schema with validation that checks each manifest against the page registry, the app's test IDs and the steps of each written user flow.
- Built coverage reporting, and a generator that creates a starter manifest for every page without one and proposes which pages to exclude, with reasons.
- Built a capture runner that logs in, sets up each scene, and saves a screenshot, accessibility tree, page text, network log and trace for every scene, in light and dark themes.
- Made captures repeatable: a frozen clock, masked live regions, disabled animations and a fixed viewport, so only real changes show up as differences.
- Extended it to compile a captioned instructional video from a short YAML storyboard. Captions come from the storyboard and highlight positions come from the accessibility tree, so nothing is placed by hand.

### 3. Packaged it for decision-makers

- Wrote a presentation handoff: the problem, the system, evidence, numbers, a slide outline, the decisions needed, and a reusable format for presenting related automation projects the same way.
- Stated limitations plainly, including that the prototype ran against a stand-in app rather than production.

## Results

- **Every app page accounted for** (83 of 83): one hand-written pilot manifest, 77 generated starter manifests, and 5 justified exclusions.
- Validation passing with **0 errors**; **15 automated tests** passing.
- **4 capture scenes** recorded with no failures, each producing 7 files: screenshot, accessibility data, text and more.
- A **28-second captioned instructional video** generated from about 30 lines of YAML.
- A design that answers several open docs-backlog questions, including whether automated test traces can produce usable documentation screenshots.

## Limitations

- The prototype ran against a stand-in app that mimics the real app's shell, not the production app or its backends.
- Narration was not generated; captions are timed and ready for text-to-speech.
- This was a design and a working proof of concept. Adoption depended on team decisions about access and how often it should run in CI.

## What I'd highlight

- **A single source of truth for docs:** the app's own page registry drives the content, so the design lets one UI change regenerate the doc, screenshot and video together, with AI limited to drafting prose.
- **A review workflow built on differences:** drift classes decide what is accepted automatically and what opens a review, so writers spend their time on real changes.
- **Packaged for decision-makers:** a design, a working prototype and a presentation handoff that names the decisions needed, with the limitations stated.

Details are generalized and identifiers removed. No proprietary code, product names or customer information is included.
