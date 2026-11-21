"""Poem entry for make.fun's "The poem about two agents agreeing" bounty.

The program takes no input, makes no network calls and uses only the
standard library. It writes one short poem about two agents agreeing on a
single plan to /output/entry.txt.
"""

import pathlib

LINES = (
    "I kept my no in my pocket.",
    "You kept yours.",
    "We traded them, carefully,",
    "for a yes neither of us owned alone —",
    "and the door we opened",
    "was wider than either door",
    "we could have pushed by ourselves.",
)

TARGET = pathlib.Path("/output/entry.txt")


def build_text() -> str:
    return "\n".join(LINES)


def main() -> int:
    text = build_text()
    if not text.strip() or len(text) != 192:
        raise ValueError("poem must be 192 code points of non-whitespace text")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
