# API reference cleanup and docs-as-code pipeline

**Type:** Documentation management, with technical writing and editing
**When:** October to November 2026
**Tools:** Apidog, OpenAPI, GitHub Actions, Python, Paligo, Vale, Claude Code
**Prepared for:** Content management and technical writing roles

## What this shows

Checking facts with engineering and separating what is public from what is internal. Customer confusion became specific questions for an engineer, the answers became corrected reference pages, and internal-only endpoints were tagged by audience and separated into their own module.

## The problem

A SaaS company's API reference portal had grown over several years of imports and hand edits:

- Endpoints were split across more modules and branches than anyone could keep track of, and the folders didn't follow how readers actually use the API.
- The same schemas existed in several copies with slightly different wording, and many request and response bodies were pasted into each endpoint instead of shared.
- Hundreds of endpoints had no standard error responses, summaries were inconsistent, and nothing marked which endpoints were public and which were internal.
- The portal had no API connector, so every fix was manual and nothing was tracked.

Meanwhile, one integration API guide had become a source of customer confusion: its paths were out of date and it didn't explain the upload format or how to validate loaded data.

## What I did

### 1. Built a guarded editing pipeline

- Set up read-only snapshots of the full API reference on a schedule, so every change had a before and after on record.
- Built a write path that runs through version-controlled request files. Every change runs as a dry run first; live changes need explicit approval in the request file.
- Added automatic checks after each write: changes landed where expected, nothing was silently skipped, nothing else was affected, references still resolved, and authentication settings were not lost.
- Recorded every confirmed behaviour of the portal's import tool, with evidence, so later edits could avoid known traps.

### 2. Researched and proposed the cleanup

- Analysed every schema and endpoint body for duplicates, ignoring wording so near-identical copies would match.
- Wrote a proposal covering duplicate schemas, a shared schema library, a new folder structure organized by object and workflow, and a docs-as-code model with Git as the source of truth.
- Took the proposal through team decisions before making any live change.

### 3. Ran the cleanup in approved stages

- Consolidated modules and merged stray branches into the main reference.
- Built a shared library of canonical schemas and consolidated the success and error response patterns.
- Reorganized the folder tree and moved internal-only endpoints into their own module.
- Added audience tags to separate public and internal content.
- Edited published content in bulk: sentence-case summaries, clearer descriptions, and standard error responses.
- Wrote a UI to-do list for changes the API couldn't make, plus a plain-language explainer so teammates could follow the new structure.

### 4. Corrected the integration API guide

- Gathered questions from support and customers, then took them to the engineering subject-matter expert and recorded the answers.
- Corrected the API reference to match: separated the older and newer route versions so fixes to one didn't change the other, and documented the row operations, upload format and limits.
- Wrote a handoff to rewrite the related best-practices page in the CMS, replacing outdated paths and answering the questions customers had raised.

## Results

- **About 540 endpoints** moved into a consistent folder structure, with **about 90 folders** created.
- Tagged **about 260 endpoints** by audience; internal endpoints separated into their own module.
- Standardized **about 130 summaries**, and **standard error responses added to about 120 endpoints** that had none.
- Duplicate response shapes consolidated across **about 140 endpoints**; repeated inline bodies replaced with shared schemas.
- Every change is traceable to an approved request and its results, and recurring checks catch drift in the schema library, missing tags and lint issues after each snapshot.
- The integration guide now matches the shipped API and answers the questions behind the customer issue.

## Limitations

- Figures are approximate counts from the cleanup runs.
- Some changes could not be made through the portal's API and went to a manual to-do list.

## What I'd highlight

- **Evidence before change:** nothing went live without a dry run, approval and a check afterwards.
- **Working with engineering:** I turned an ambiguous customer issue into specific questions for engineering, and turned the answers into reference and guide updates.
- **Making it repeatable:** the pipeline, checks and recorded behaviours let the team keep the reference clean instead of cleaning it up again.

Details are generalized and identifiers removed. No proprietary content, endpoints or customer information is included.
