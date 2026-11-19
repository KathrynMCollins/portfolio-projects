"""The one place the model is called: one structured request per signal."""

import anthropic

from .models import Finding, Page, Signal, Verdict
from .prompts import SYSTEM, user_message
from .retrieve import rank

DEFAULT_MODEL = "claude-opus-5-5"


def triage(client, signal: Signal, pages: list[Page], *, model: str, effort: str, top_k: int) -> Finding:
    candidates = rank(signal, pages, top_k)
    content = user_message(
        signal.body, signal.source, [p.path for p in pages], [(p.path, p.text) for p in candidates]
    )
    response = client.beta.messages.parse(
        model=model,
        max_tokens=16000,
        # The rubric is identical for every signal, so it is cached after the first call.
        system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": content}],
        output_format=Verdict,
        output_config={"effort": effort},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    finding = Finding(signal, _verdict_from(response), [p.path for p in candidates], model=response.model)
    if response.stop_reason == "refusal":
        finding.flags.append("Model declined this item; triage it by hand.")
    return finding


def _verdict_from(response) -> Verdict:
    if response.stop_reason in ("refusal", "max_tokens") or response.parsed_output is None:
        return Verdict(
            bucket="confirm", reason=f"No usable verdict (stop reason: {response.stop_reason}).",
            priority="n/a", effort="n/a", action="none", impacts=[],
            question="Does this change affect the docs?",
        )
    return response.parsed_output


def run(signals: list[Signal], pages: list[Page], *, model=DEFAULT_MODEL, effort="medium", top_k=3, client=None, progress=None):
    client = client or anthropic.Anthropic()
    findings = []
    for i, signal in enumerate(signals, 1):
        if progress:
            progress(f"[{i}/{len(signals)}] {signal.title}")
        findings.append(triage(client, signal, pages, model=model, effort=effort, top_k=top_k))
    return findings
