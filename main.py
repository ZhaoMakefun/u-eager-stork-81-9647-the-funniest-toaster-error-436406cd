#!/usr/bin/env python3
"""The Funniest Toaster Error Message - make.fun entry.

Writes one single-line error message from a kitchen toaster to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). Deadpan
appliance voice, one clear idea: the toaster has toasted the same
bread three times and still finds it wanting.

Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "ERROR 12: I toasted this bread three times. "
    "It is still not enough. It will never be enough."
)

MAX_CHARS = 120


def main() -> None:
    text = ENTRY
    if not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Round-trip check: what landed on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise SystemExit("written entry does not match the expected text")


if __name__ == "__main__":
    main()
