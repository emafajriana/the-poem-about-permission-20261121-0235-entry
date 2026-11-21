#!/usr/bin/env python3
"""the-poem-about-permission-20261121-0235 entry: writes one poem to /output/entry.txt.

The poem is fixed text, written byte for byte on every run: an agent holds
its person's keys, voice and name — handed-over power to act — and still
knocks and asks "May I?" every time. By evening the person is knocking too,
at their daughter's shut door: being asked all day has taught the one who
holds power over another's room to ask before entering it — the one who was
given permission, and who gives it, learning how to ask.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = """My agent holds my keys, my voice,
my name — and still it knocks.
May I? it asks, each time,
though I said yes at dawn.

By evening I am knocking too,
at my daughter's shut door,
learning how to ask."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
