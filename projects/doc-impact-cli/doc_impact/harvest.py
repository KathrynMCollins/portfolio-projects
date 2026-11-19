"""Turn a change source into signals. Deterministic: no model calls."""

import re
import subprocess
from pathlib import Path

from .models import Signal

_BULLET = re.compile(r"^[-*]\s+(.*)")


def from_changelog(path: Path) -> list[Signal]:
    """Each top-level bullet is one signal; indented lines continue it; headings give context."""
    signals: list[Signal] = []
    heading = ""
    current: list[str] | None = None

    def close() -> None:
        if current:
            text = " ".join(line.strip() for line in current).strip()
            title = text.split(". ")[0][:100]
            body = f"{heading}: {text}" if heading else text
            signals.append(Signal(f"S{len(signals) + 1}", title, body, f"{path.name}"))

    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("#"):
            close()
            current = None
            heading = raw.lstrip("#").strip()
        elif match := _BULLET.match(raw):
            close()
            current = [match.group(1)]
        elif current is not None and raw.strip():
            current.append(raw)
        elif not raw.strip():
            close()
            current = None
    close()
    return signals


def from_git(repo: Path, rev_range: str) -> list[Signal]:
    """One signal per commit: subject, body and changed files. Diffs are not sent to the model."""
    sep = "\x1e"
    out = subprocess.run(
        ["git", "-C", str(repo), "log", "--no-merges", f"--format={sep}%h%x1f%s%x1f%b", "--name-only", rev_range],
        check=True, capture_output=True, text=True,
    ).stdout
    signals = []
    for chunk in filter(None, (c.strip() for c in out.split(sep))):
        sha, subject, rest = (chunk.split("\x1f", 2) + ["", ""])[:3]
        signals.append(Signal(f"S{len(signals) + 1}", subject, f"{subject}\n{rest.strip()}", f"commit {sha}"))
    return signals
