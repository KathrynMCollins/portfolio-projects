# Release documentation in a component CMS: ServiceNow integration upgrade and new setup flow

**Type:** Technical writing and editing, with content operations
**When:** October 2026
**Tools:** Paligo (DocBook XML component CMS), Paligo API, Python, Markdown, Claude Code
**Prepared for:** [Technical Editor, Editorial Publishing, Anthropic](https://job-boards.greenhouse.io/anthropic/jobs/5443997008)

## What this shows

Fact-checking with experts while the release was moving. Release notes changed mid-release, an ambiguous support statement went to the product owner as a specific question, and nothing reached readers before it was checked. Unreleased material stayed out of every publication, which is disclosure judgment in practice.

## The problem

Two releases needed documentation at the same time, both in a structured CMS where topics are XML components and one topic can be reused on several published pages:

- **An integration app upgrade.** A new version of the ServiceNow integration app changed behaviour, added settings and fixed several issues. The release notes were revised during the release, and a statement in the notes about supported ServiceNow platform versions read as excluding one that was in fact supported.
- **A new setup flow.** The docs had to be drafted and held for review before publishing.

In this CMS, any change to a live topic goes out with the next publication, and a change to a reused topic changes every page that includes it.

## What I did

### 1. Audited the ServiceNow release for doc impact

- Mapped each change in the release notes to the affected docs pages and sections, and grouped the edits into six items.
- Re-checked the plan when revised release notes arrived, recorded what changed between the two versions, and folded the new behaviour changes, settings and fixes into the edits.
- Raised the ambiguous platform statement with the product owner, got a clear answer on which versions were tested and approved, and updated the drafts to match.

### 2. Worked safely on copies until the release was live

- Held all live edits until the app was available and each topic had my go-ahead.
- Made a fresh test copy of each live topic, applied a scripted, repeatable edit to the copy, and checked that the edit landed and nothing else changed.
- Checked for reuse before every edit so changes to shared components couldn't spill onto other pages. When snapshots from an earlier session were lost, I confirmed the live topics were unchanged before rebuilding from them.
- Kept every open question marked in the text for review instead of guessing, and noted a colleague's in-progress review edit so it wasn't lost when outdated copies were deleted.

### 3. Drafted the new setup flow

- Wrote two new topics in Markdown for the setup flow, linked to each other as next steps.
- Converted them to the CMS's XML structure with tables, callouts, nested steps and cross-links, then confirmed the converted text matched the draft word for word.
- Left the verification, link, screenshot and placeholder markers in place for subject-matter review, and kept the drafts out of every publication until release.

### 4. Recorded what the CMS API could and couldn't do

- Documented each run step by step: what changed, what was checked and what was left open.
- Recorded limits the team could reuse, such as the API being unable to move a topic between folders, so those steps went to the editor instead.

## Results

- **Four ServiceNow integration topics** updated on review copies, covering all six audit items and the revised release notes, ready to go live once the app was released.
- A platform support statement **corrected with the product owner**, so the docs no longer implied a supported version was excluded.
- **Two new setup topics** drafted and converted with a word-for-word match (about 1,000 words in total), held until the feature launched.
- **Zero unintended changes** to live or reused content: nothing was published without review.

## Limitations

- The setup flow drafts were held unpublished until release, with verification markers left for subject-matter review.
- The CMS API could not move topics between folders, so those steps were done by hand in the editor.

## What I'd highlight

- **Release notes as a moving target:** tracking revisions and changing the docs plan to match, rather than editing once and hoping.
- **Working with product and engineering:** turning an ambiguous statement into a specific question and getting it answered on record.
- **Safe editing in a reuse-heavy CMS:** copies, reuse checks and verification before anything reaches readers.

Details are generalized and identifiers removed. No internal product names, internal tickets, people or unreleased feature details are included.
