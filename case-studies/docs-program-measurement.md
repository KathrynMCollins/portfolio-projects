# Measuring a documentation program: from monthly workbooks to page-type goals

**Type:** Case study: documentation program measurement, internal research and a writing standard
**When:** 2021 to 2023, with later use in 2026
**Author:** Kathryn Collins
**Tools:** Google Analytics (Universal Analytics, then GA4), spreadsheet pivot tables, an internal survey form
**Prepared for:** Content management and technical writing roles

## What this shows

Running a documentation program on evidence for several years, and changing the measurement when the questions changed. A monthly traffic workbook gained an internal survey, release-level and annual comparisons, and finally goals set per page type, so exit rate could count as success on one page and a warning on another. The same record later served as the baseline for an analytics framework for a docs AI assistant.

Portfolio note: traffic and survey figures are shown as trends, ratios and rounded percentages. Respondent comments are paraphrased. Page names, internal tools and people are removed.

## The problem

The program needed to know which pages carried the site, whether readers finished what they came for, what the colleagues who send docs to customers needed, and whether a release's documentation was read.

Raw page views could not answer those questions. In the first workbooks, the pages with the highest exit rates were integration setup pages that readers reached by direct link. A high exit rate there could mean the reader got the answer and left, or gave up.

## What I did

### 1. A monthly workbook with a fixed shape

I built a workbook template and filled it every month from 2021 through late 2023. Each one had the same sheets: most viewed pages, longest viewed pages, pages most often reached by direct link, a watch list comparing this month with last month for selected pages, and the raw export with a notes column. From the mid-2021 template on, each workbook also carried the previous month's raw data, so month-over-month changes were visible without opening a second file.

Because the columns did not change, a page could be followed for years. The raw data also surfaced malformed inbound links; whether each was traced and fixed is not recorded.

### 2. An internal survey (2021)

I surveyed the colleagues who use the docs site to support customers, across sales engineering, solutions architecture, customer success, support and integrations. It asked their role, how often they used the site and for what, how they found pages, whether they shared pages with customers, and what they wished were different.

What it found:

- Nearly everyone (over 90 percent) used the API documentation, about 70 percent used the site to learn how features work, and about 60 percent used integration setup instructions.
- About 70 percent shared docs links directly with customers, to answer questions or to explain a feature.
- Searching within the site was the most common way to find a page, used by about two in three.
- Requests clustered around more content for complex features, incomplete API reference, thin integration troubleshooting, search and how often pages were updated.

I tagged every free-text answer by topic and wrote a response note for each. The notes tie requests to work: review each API for accuracy as the reference moved to new OpenAPI-based pages, add separate integration instruction pages, and agree an update routine with the integrations team. Some notes show this work was already planned, so the survey confirmed and ordered it rather than starting it.

The later analytics show the structural changes. In mid-2021 the API reference was one page; by December 2021 the workbook tracks well over a hundred endpoint pages, and a set of separate integration installation pages appears in the same workbook. One note proposed a regular audit of integration pages; whether one started then is not recorded. Most search complaints concerned the hosting platform's search, which the notes say the team could not change beyond archiving stale changelog entries.

### 3. Release-level comparisons (2022)

To see whether release docs were read, I built a workbook of every page's monthly views across 2021 and 2022. When the enrichment documentation was replaced, the old page fell to about a fifth of its traffic within two months while the new page took it over.

For the SCIM release I compared month-long windows around the announcement. Views across the SCIM and role management pages rose about 70 percent afterward, monthly views roughly doubled over four months, and readers moved from the older beta user API pages to the new endpoints. A 2023 workbook compared the SSO pages with their page-type baseline: one setup page held readers about two and a half times as long as a typical instructions page. What followed from that is not recorded.

### 4. Annual comparisons and page-type goals (2023)

With the move to GA4 I pulled the history back to 2019 into one annual comparisons workbook. Site views grew by about half from 2020 to 2021 and by about two thirds the next year, and searches for the top terms more than doubled from 2021 to 2022, led both years by integrations, enrichment, the API and the query language.

The answer to the exit-rate problem was a granular template. Every page was tagged with one of about a dozen content types, each type got a goal direction for views, time on page and exits, and a fourth-quarter 2022 baseline was set per type. A sample:

| Page type | Views | Time on page | Exits |
| --- | --- | --- | --- |
| Instructions | Up | Down | Up |
| API endpoint | Up | Down | Up |
| Landing page | Up | Down | Down |
| Navigation | Down | Down | No goal |
| Archived | Down | No goal | No goal |

Read this way, an exit from an instruction page is a finished task, and an exit from a landing page is a reader who found no way in. The baseline showed why this was needed: instruction pages had about twice the site's average exit rate, which the goals treat as success. A second goal table restated the same goals in GA4's terms, engagement time and bounce rate, so the targets would survive the change in tools.

### 5. A writing standard (2022)

Measurement shows where docs fall short; a standard helps fix them. I taught a best-practices session in four stages. Planning starts with audience: who needs the doc and why. Outlining goes big, then small: what, why and who, then where and how. Drafting walks through the steps while writing, keeps text short and consistent and gets a second reader. Revising includes adjusting to feedback. The session closed with templates for support ticket updates and bug reports: what is happening and where, what should happen, and how to reproduce it.

## Results

- A consistent measurement record from 2021 to late 2023, ending in a page-type goal model with a baseline, in place of single-number judgments.
- Survey priorities matched to structural changes visible in the site's own data, and release-level evidence that readers moved to new pages.
- Later use. The [analytics framework for a docs AI assistant](../projects/ai-widget-analytics/README.md) used older site analytics as its traffic baseline and keeps low-traffic pages the assistant cites often: the same caution the page-type goals built in, that views alone do not decide a page's value.
- A recurring theme. The 2021 survey asked for pages updated when integrations change and for easier finding; feedback for the 2026 [capacity and investment case](docs-capacity-and-investment-case.md) asked for advance notice of changes and findability. That case measured demand from engineering's tracker, not traffic.

## Limitations

- Traffic grew with the product and customer base. Nothing here isolates the effect of the docs work on those trends.
- The survey was internal, small and run once; no repeat survey is recorded.
- Universal Analytics and GA4 define their metrics differently, so comparisons that span the switch are approximate.
- The sources show goals and a baseline but not a full year scored against them.
- The analytics cannot tell internal readers from customers, and reader-level analytics remain a planned goal.
- Release comparisons are before and after views, not controlled tests.
