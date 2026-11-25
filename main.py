#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to entry.txt.
Gate (from the competition rules): UTF-8 text of 1 to 200 characters,
not only white space, a single line. Anything else exits 1.
"""
import os
import sys

ENTRY = ("The fire drill went so well that management scheduled one "
         "every Friday, and now the fire alarm has its own calendar invite.")


def main() -> int:
    entry = ENTRY
    if not entry or not entry.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(entry) > 200:
        print("error: entry exceeds 200 characters", file=sys.stderr)
        return 1
    if "\n" in entry or "\r" in entry:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in entry):
        print("error: entry contains control characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
