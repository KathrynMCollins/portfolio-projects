from dataclasses import dataclass, field
from typing import Literal

from pydantic import BaseModel, Field


@dataclass
class Signal:
    """One product change, harvested from a changelog entry or a commit."""

    id: str
    title: str
    body: str
    source: str


@dataclass
class Page:
    path: str
    title: str
    text: str


class PageImpact(BaseModel):
    page_path: str = Field(description="Path of the affected page, exactly as given in the docs index.")
    section: str = Field(description="Heading of the affected section, or the proposed title for a new page.")
    stale_quote: str = Field(
        description=(
            "Text copied exactly from the page that is now wrong or incomplete. "
            "Empty only when the action is new_page or the problem is missing content."
        )
    )
    proposed_edit: str = Field(description="What the section should say instead, in one or two sentences.")


class Verdict(BaseModel):
    bucket: Literal["impact", "confirm", "none"]
    reason: str = Field(description="One sentence a writer can check against the evidence.")
    priority: Literal["P1", "P2", "P3", "n/a"]
    effort: Literal["S", "M", "L", "n/a"]
    action: Literal["update", "new_page", "relocate", "none"]
    impacts: list[PageImpact]
    question: str = Field(description="For confirm only: the exact yes/no question to ask. Otherwise empty.")


@dataclass
class Finding:
    signal: Signal
    verdict: Verdict
    candidates: list[str]
    flags: list[str] = field(default_factory=list)
    model: str = ""
