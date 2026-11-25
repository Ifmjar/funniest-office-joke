"""Entry for make.fun's "The Funniest Office Joke, Judged Head to Head".

Writes one joke about office life to /output/entry.txt. The competition
judges the single line head to head against the other entries, so the
whole entry is this one line: a setup, then a turn, with the punchline
last. The line is fixed text, written byte-identical with no trailing
newline, and must stay within the gate of 1 to 200 characters.

Draft line (to be replaced by the proxy-judge winner before submit):
the 4:59 "got a minute" ambush, the longest minute in the office.
"""

import os
import sys

JOKE = (
    "At 4:59 my boss always asks if I've 'got a minute' — it's the "
    "longest minute in the known universe, and it ends at 6:30."
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
