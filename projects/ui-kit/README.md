# Accessible brand UI kit and design review guide

**Type:** Documentation management, with design systems and accessibility
**When:** October to November 2026
**Author:** Kathryn Collins
**Tools:** HTML, CSS custom properties (design tokens), vanilla JavaScript, axe-core, Playwright, Python, Claude Code
**Prepared for:** Content management and documentation leadership roles

## What this shows

Standards with their reasons written down, and review before release. Each accessibility decision names the rule behind it, and a review mode checks upcoming UI before it reaches engineering.

## The problem

Docs pages, internal tools, prototypes and one-off web pages were each styled by hand. Brand colours, type and spacing drifted from page to page, accessibility depended on whoever built the page, and common controls (menus, dialogs, tabs, tooltips) behaved differently each time. Nobody wrote down the brand decisions, so the same questions came up on every project.

## What I did

### 1. Turned the brand guideline into design tokens

- Converted the brand guideline into one set of tokens for colour, type scale, spacing, corner radius and focus, with light, dark and high-contrast themes.
- Components use semantic roles (text, accent, control border) instead of raw colour values, so dark mode and high contrast work automatically.
- Recorded each brand decision and the reason for it, for example using only the web-licensed brand font, and what replaces pure black in dark mode.

### 2. Built accessible components

- Built styles for layout, cards, buttons, form fields, badges, callouts, tables, dialogs, side panels, menus, dropdowns, tabs, tooltips and toasts.
- Built the interactive behaviour in a small, dependency-free script that follows the W3C ARIA Authoring Practices patterns.
- Set the accessibility bar at **WCAG 2.2 AA**. Focus appearance and target size meet **AAA**, and the kit supports Windows High Contrast mode, reduced motion and print.
- Wrote a decision table that names each choice and the WCAG criterion behind it: text size, line length, visible focus, colour never used alone, errors announced to screen readers, and disabled controls that explain why.

### 3. Wrote the guidance around it

- A reference page that demonstrates every token and component, and copy-and-paste markup for each component.
- Three audience profiles (public docs, internal tools, product UI) with rules for callouts, capitalisation, links and wording.
- A developer handoff covering install, accessibility decisions, rules code can't enforce, and the component API.
- Rules for extending the kit, so new components follow the same patterns.

### 4. Made checking part of the workflow

- Wrote a page checker that runs axe-core and keyboard tests in light and dark mode and saves light, dark and mobile screenshots.
- Added a **design review mode** for upcoming UI, such as prototypes, mocks, designs and pre-release builds, that produces findings ranked by severity before work goes to engineering.
- Packaged the kit as an AI assistant skill, so pages built with AI help follow the same rules and pass the same checks.

## Results

- **0 accessibility violations** in automated testing (axe-core, WCAG 2.0 to 2.2 A/AA plus best practices), in light and dark themes.
- **Adopted by an internal platform's admin console**, which now follows the kit's tokens, accessibility bar and dialog patterns, with an accessibility check required before UI changes ship.
- One source for brand and accessibility decisions, maintained with a changelog as product naming and guidance change.

## Limitations

- Automated tests catch only part of WCAG 2.2. Manual testing with assistive technology is not recorded.
- Adoption so far is one internal admin console.

## What I'd highlight

- **Standards with their reasons on record:** every brand and accessibility decision names the rule behind it, in one source kept current with a changelog.
- **Review built into the workflow:** a page checker and a design review mode that flags upcoming UI before it goes to engineering help catch problems early, and pages built with AI help pass the same checks.
- **One system for several audiences:** semantic tokens and three audience profiles let one kit serve docs, internal tools and product UI, and an internal admin console has adopted it.

Details are generalized and identifiers removed. No proprietary brand assets, internal URLs or product code are included.
