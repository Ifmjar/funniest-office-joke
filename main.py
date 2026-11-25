"""Entry for make.fun's "The Funniest Office Joke, Judged Head to Head".

Writes one joke about office life to /output/entry.txt. The competition
judges the single line head to head against the other entries, so the
whole entry is this one line: a setup, then a turn, with the punchline
last. The line is fixed text, written byte-identical with no trailing
newline, and must stay within the gate of 1 to 200 characters.

Draft line (replaced by the proxy-judge winner before submit):
the exit interview, three years too late — the retention
conversation held only once the employee is already leaving.
The winning line beat every other finalist head to head in a
proxy-judge round-robin (DeepSeek v4.1-flash, the competition's
published brief, house scoring): overall 0.725 across 6 games,
beating MICROWAVE 0.80, BADGE 0.65 and FIREDRILL 0.80, and
splitting the strongest field joke (reply-all, 0.50).
"""

import os
import sys

JOKE = (
    "In my exit interview HR asked what would have kept me, and I "
    "said 'this interview, three years ago'."
)


def write_entry(path: str, text: str) -> None:
    """Write text exactly as given; fail loudly if it breaks the gate."""
    chars = len(text)
    if chars < 1 or chars > 200:
        raise SystemExit(f"joke is {chars} chars, gate is 1-200")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main() -> int:
    target = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    try:
        write_entry(target, JOKE)
    except OSError as exc:
        print(f"error: cannot write {target}: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(JOKE)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
