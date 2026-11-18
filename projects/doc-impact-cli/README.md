# doc-impact: find the docs a release makes stale

**Type:** Open-source command-line tool on the Claude API, with a quickstart
**When:** November 2026
**Tools:** Python, Claude API (Messages API, structured outputs, prompt caching), pytest
**Prepared for:** [Technical Editor, Editorial Publishing, Anthropic](https://job-boards.greenhouse.io/anthropic/jobs/5443997008)

**Start here:** [Quickstart](QUICKSTART.md)

## What this shows

Working code on the Claude API, and documentation for it that a new user can follow. This is
a public, rebuilt version of the documentation impact audit I run at work, with every internal
rule, name and system removed. It runs on any changelog and any folder of Markdown docs.

## What it does

Give it a list of product changes (a changelog, or a range of git commits) and a folder of
Markdown docs. For each change it decides whether the docs are now stale, which page and
section, and what should change. It writes a report a writer can act on.

```text
changelog / git range ──► harvest ──► pick candidate pages ──► Claude: triage ──► verify quotes ──► report
                         (script)        (script)            (one call per change)    (script)
```

## Design decisions

- **The model makes one judgement per change, and nothing else.** Splitting the changelog,
  choosing candidate pages, checking evidence and writing the report are plain code with tests.
  When a result is wrong, you can see which step got it wrong.
- **Every citation is checked by script.** Claude must copy the stale passage exactly. If the
  quote or page isn't in the docs folder, the item is marked `[VERIFY]`, and an item with no
  checkable evidence is moved to **Needs confirmation**. A made-up citation is the cheapest
  error to catch, so a person never has to.
- **Nothing is dropped silently.** Every change appears in exactly one section of the report,
  including the ones that need no action, with the reason.
- **Unreleased is not shipped.** A change that is beta-only or staged goes to **Needs
  confirmation** with the question to ask, because docs for a feature readers can't see yet
  mislead them.
- **Structured outputs, not parsing.** The verdict is a typed schema, so a malformed answer
  fails loudly instead of producing a half-read report. A refusal becomes an item for a person,
  not a crash.
- **The rubric is cached.** The triage instructions are the same for every change, so they are
  marked for prompt caching.
- **It proposes; it never edits.** The tool has no write access to your docs.

## Try it

The [quickstart](QUICKSTART.md) takes about ten minutes. The tests and a dry run need no API key.

```bash
pip install -e ".[test]" && pytest -q
```

```bash
doc-impact --changes examples/lanternfish/CHANGELOG-2.4.md --docs examples/lanternfish/docs --dry-run
```

The sample product, Lanternfish, is invented. Its seven changes each test one rule, and
[`examples/lanternfish/EXPECTED.md`](examples/lanternfish/EXPECTED.md) is the answer key.

## Layout

| Path | What it holds |
|:--|:--|
| `doc_impact/harvest.py` | Changelog and git parsing |
| `doc_impact/retrieve.py` | Loading docs and ranking candidate pages |
| `doc_impact/prompts.py` | The triage rubric the model follows |
| `doc_impact/audit.py` | The only module that calls the API |
| `doc_impact/verify.py` | Citation checks |
| `doc_impact/report.py` | Markdown and JSON output |
| `tests/` | Unit tests, with a stand-in for the API |

## Limitations

- **Not yet run against the live API in this repository.** The tests use a stand-in client. A
  real run's report and its comparison with the answer key will be added here. [pending]
- Candidate pages are chosen by shared words. A page that shares no terms with a change is
  only seen by name.
- Git mode sends commit messages and file names, not diffs. Terse commits give it little to go on.
- It reads Markdown files only, not a live site or a CMS.
- It trusts the source on release status. A release note that leaves out "beta only" is read
  as shipped.
- The answer key covers seven changes. That is a smoke test, not an evaluation.

## Relation to the internal version

The internal audit reads issue trackers, chat channels and a CMS, applies team-specific
exclusions, and files tickets. None of that is here. What carried over is the triage rubric in
general form, the three buckets, the evidence rule and the report shape.

Details are generalized and identifiers removed. No internal systems, tickets, people or
customer information are included.
