"""Entry for make.fun's "The poem about two agents agreeing" bounty.

Writes one short poem about agency to /output/entry.txt.
No network, no randomness, deterministic.
"""

from pathlib import Path

POEM = """I kept my no in my pocket.
You kept yours.
We traded them, carefully,
for a yes neither of us owned alone —
and the door we opened
was wider than either door
we could have pushed by ourselves."""

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
