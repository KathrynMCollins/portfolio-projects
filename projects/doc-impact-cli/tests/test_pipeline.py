from pathlib import Path
from types import SimpleNamespace

from doc_impact import audit, harvest, report, retrieve, verify
from doc_impact.models import PageImpact, Verdict

EXAMPLE = Path(__file__).parent.parent / "examples" / "lanternfish"
PAGES = retrieve.load_docs(EXAMPLE / "docs")
SIGNALS = harvest.from_changelog(EXAMPLE / "CHANGELOG-2.4.md")


def verdict(bucket="impact", action="update", impacts=(), priority="P2"):
    return Verdict(bucket=bucket, reason="r", priority=priority, effort="S", action=action,
                   impacts=list(impacts), question="")


class FakeClient:
    """Stands in for anthropic.Anthropic(); returns canned verdicts in order."""

    def __init__(self, verdicts, stop_reason="end_turn"):
        self.calls = []
        it = iter(verdicts)

        def parse(**kwargs):
            self.calls.append(kwargs)
            return SimpleNamespace(parsed_output=next(it), stop_reason=stop_reason, model=kwargs["model"])

        self.beta = SimpleNamespace(messages=SimpleNamespace(parse=parse))


def test_changelog_bullets_become_signals_with_continuations():
    assert len(SIGNALS) == 7
    assert "deprecation warning" in SIGNALS[0].body
    assert SIGNALS[0].body.startswith("Changed:")


def test_rank_finds_the_page_that_names_the_key():
    batch = next(s for s in SIGNALS if "batch_size" in s.title)
    assert retrieve.rank(batch, PAGES)[0].path == "configuration.md"


def test_verify_accepts_exact_quote_despite_markdown_and_spacing():
    f = audit.Finding(SIGNALS[1], verdict(impacts=[PageImpact(
        page_path="configuration.md", section="Batching", stale_quote="The maximum   is 500.", proposed_edit="2000")]), [])
    verify.verify([f], PAGES)
    assert f.flags == [] and f.verdict.bucket == "impact"


def test_verify_downgrades_invented_evidence():
    f = audit.Finding(SIGNALS[1], verdict(impacts=[
        PageImpact(page_path="configuration.md", section="Batching", stale_quote="The maximum is 250.", proposed_edit="x"),
        PageImpact(page_path="limits.md", section="Limits", stale_quote="500", proposed_edit="x"),
    ]), [])
    verify.verify([f], PAGES)
    assert f.verdict.bucket == "confirm"
    assert any("Quote not found" in fl for fl in f.flags)
    assert any("not in the docs folder" in fl for fl in f.flags)


def test_new_page_needs_no_quote():
    f = audit.Finding(SIGNALS[3], verdict(action="new_page", impacts=[PageImpact(
        page_path="oauth.md", section="Authenticate with OAuth", stale_quote="", proposed_edit="x")]), [])
    verify.verify([f], PAGES)
    assert f.verdict.bucket == "impact"


def test_run_sends_rubric_once_cached_and_candidates_in_prompt():
    client = FakeClient([verdict("none", "none", priority="n/a")] * 2)
    audit.run(SIGNALS[:2], PAGES, client=client)
    call = client.calls[0]
    assert call["model"] == "claude-opus-5-5"
    assert call["system"][0]["cache_control"] == {"type": "ephemeral"}
    assert call["system"] == client.calls[1]["system"]
    assert '<page path="configuration.md">' in call["messages"][0]["content"]


def test_refusal_becomes_confirm_with_flag():
    client = FakeClient([None], stop_reason="refusal")
    [f] = audit.run(SIGNALS[:1], PAGES, client=client)
    assert f.verdict.bucket == "confirm" and f.flags


def test_report_lists_every_signal_once():
    findings = [audit.Finding(s, verdict("none", "none", priority="n/a"), []) for s in SIGNALS]
    md = report.to_markdown(findings, source="CHANGELOG", docs="docs", model="claude-opus-5-5")
    assert all(md.count(s.title) == 1 for s in SIGNALS)
    assert "## Coverage and limits" in md
