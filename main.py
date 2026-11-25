#!/usr/bin/env python3
"""Write one excuse line to /output/entry.txt.

The excuse is fixed text: deterministic, no input, no network.
"""
import os

ENTRY = (
    "Sorry \u2014 I shipped the bug, then 'fixed' it three times, "
    "and each fix was just me confidently deleting the test "
    "that caught it."
)


def main():
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # No input data is needed for this entry.
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200
    assert ENTRY.strip() == ENTRY
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
