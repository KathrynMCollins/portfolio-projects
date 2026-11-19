# Quickstart: find the docs a release makes stale

In about ten minutes you will install `doc-impact`, run it against a sample product, and read
the report it writes. Then you will point it at your own changelog and docs.

`doc-impact` reads a list of product changes and a folder of Markdown docs. For each change it
asks Claude one question: would a reader following the current docs now get a wrong result? It
then checks every passage Claude quotes against your files, so a citation that doesn't exist
is flagged before a person sees it.

It proposes changes only. It never edits your docs.

## Before you start

You need:

- Python 3.10 or later. Check with `python3 --version`.
- Git.
- A Claude API key, for step 4 only. Create one in the [Claude Console](https://platform.claude.com/)
  under **API keys**. Each change in the source is one API request, so the sample makes seven.

## 1. Install

Clone the repository and move into the project folder:

```bash
git clone https://github.com/KathrynMCollins/portfolio-projects.git
```

```bash
cd portfolio-projects/projects/doc-impact-cli
```

Create a virtual environment and install the tool with its test dependencies:

```bash
python3 -m venv .venv && source .venv/bin/activate
```

```bash
pip install -e ".[test]"
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

To confirm the install, run the tests. They use a stand-in for the API, so they need no key:

```bash
pytest -q
```

You should see `8 passed`.

## 2. Look at the sample

The sample is a made-up log shipper called Lanternfish. Open these two things:

- `examples/lanternfish/CHANGELOG-2.4.md`: seven changes in one release.
- `examples/lanternfish/docs/`: five pages of its documentation, written before the release.

Some changes make a page wrong. Some don't. One hasn't shipped to most users yet.

## 3. Try it without a key

A dry run shows what the tool will send, without calling the API:

```bash
doc-impact --changes examples/lanternfish/CHANGELOG-2.4.md --docs examples/lanternfish/docs --dry-run
```

You get one entry per change, with the pages chosen as candidates:

```text
7 changes, 5 pages. No API calls made.

S1  Renamed the `flush_interval_sec` setting to `flush_interval_seconds`
    candidates: configuration.md, cli-reference.md, troubleshooting.md
S2  Raised the maximum `batch_size` from 500 to 2000 events.
    candidates: configuration.md, troubleshooting.md, cli-reference.md
...
```

Candidates are picked by shared words, and only those pages' full text is sent. Claude also
sees the list of every page, so it can name one that was missed.

## 4. Run the audit

Set your API key for this terminal session:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

Run the audit and save the report and the raw findings:

```bash
doc-impact --changes examples/lanternfish/CHANGELOG-2.4.md --docs examples/lanternfish/docs --out report.md --json findings.json
```

Progress prints as each change is checked. When it finishes, open `report.md`.

## 5. Read the report

Every change lands in exactly one section, so nothing is dropped without a record:

- **Proposed documentation changes**: the docs are now wrong or incomplete. Each item names
  the page and section, quotes what the page says now, and proposes the fix. P1 means a
  published instruction now fails.
- **Needs confirmation**: the change may matter, but something is unresolved. Usually it hasn't
  shipped to everyone. Each item has the question to ask.
- **No action**: nothing a reader sees has changed. The reason is given so you can disagree.

Look for `[VERIFY]`. It means Claude cited a passage or page the script could not find. If none
of an item's citations check out, the item is moved to **Needs confirmation**, because a
proposal without evidence is not ready to act on.

To check the run, compare it with the answer key in `examples/lanternfish/EXPECTED.md`. The
wording will vary. The buckets and pages should match.

## 6. Use your own docs

Point `--docs` at any folder of Markdown files. Subfolders are included.

For the changes, use either a changelog or a git history:

- **A changelog or release notes file.** Each top-level bullet is one change. Indented lines
  under a bullet belong to it, and the heading above it is included as context.

  ```bash
  doc-impact --changes RELEASE_NOTES.md --docs ./docs --out report.md
  ```

- **A range of commits.** Each commit's subject, message body and changed file names are sent.
  The diff itself is not, so commits with one-line messages give Claude little to go on.

  ```bash
  doc-impact --git ../my-product --range v2.3.0..v2.4.0 --docs ./docs --out report.md
  ```

Start with a single release. You can review a report of ten changes properly; a report of two
hundred, you will skim.

## Options

| Option | Default | What it does |
|:--|:--|:--|
| `--model` | `claude-opus-5-5` | The Claude model that triages each change. |
| `--effort` | `medium` | How much reasoning the model does: `low`, `medium`, `high`, `xhigh` or `max`. Higher costs more. |
| `--top-k` | `3` | How many candidate pages are sent in full with each change. |
| `--json` | none | Also write the findings as JSON, for scripts or comparison between runs. |
| `--dry-run` | off | Show changes and candidates; make no API calls. |

## Troubleshooting

**`Authentication failed`**: the key isn't set in this terminal, or it was revoked. Run
`echo $ANTHROPIC_API_KEY` to check, then set it again.

**`No changes found in the source`**: the changelog has no top-level bullets. Each change must
start with `- ` or `* ` at the start of a line.

**A page you expected isn't in the report**: it may not share words with the change. Run with
`--dry-run` to see the candidates, then try `--top-k 5`.

**`Model declined this item`**: the model refused one change. That change is listed under
**Needs confirmation** for you to triage by hand. The rest of the run is unaffected.

## What it doesn't do

- It doesn't read your live site. It checks the Markdown files you give it, so pages that live
  only in a CMS are invisible to it.
- It doesn't know whether a change is live in production. It goes by what the source says, so a
  release note that omits "beta only" will be read as shipped.
- It doesn't draft the new text. The proposed edit is a one- or two-sentence direction for a
  writer, not finished copy.
