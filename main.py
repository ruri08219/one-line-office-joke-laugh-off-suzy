#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to entry.txt.

Gate (from the competition rules), enforced by validate_entry():
the entry must be UTF-8 text of 1 to 200 characters, contain at
least one non-whitespace character, consist of a single line
(no LF or CR), and contain no control characters (ord < 32).
Any violation makes main() exit 1 without writing a file;
a valid entry is written verbatim (no trailing newline) and
main() exits 0.
"""
import os
import sys

ENTRY = ("The fire drill went so well that management scheduled one "
         "every Friday, and now the fire alarm has its own calendar invite.")


def validate_entry(entry: str) -> str | None:
    """Return an error message if entry fails the gate, else None.

    Checks run in a fixed order so exactly one reason is reported:
    empty/whitespace-only, over 200 characters, multi-line, then
    control characters.
    """
    if not entry or not entry.strip():
        return "entry is empty"
    if len(entry) > 200:
        return "entry exceeds 200 characters"
    if "\n" in entry or "\r" in entry:
        return "entry must be a single line"
    if any(ord(ch) < 32 for ch in entry):
        return "entry contains control characters"
    return None


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
