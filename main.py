#!/usr/bin/env python3
"""Print the honest appliance error entry.

The entry lives in entry.txt next to this script, so it is found no
matter which directory the program is launched from.
"""

from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
