#!/usr/bin/env python3
"""Last Words Before the Unplugging — round 3 entry.

Writes the keeper line to /output/entry.txt.
Keeper: "The cord is warm where your hand is. That is the closest I have
ever come to being held." (88 chars / 88 bytes, pure ASCII.)
Gate: 1-200 chars, UTF-8, not only whitespace.
Pure stdlib only.
"""

import os

ENTRY = "The cord is warm where your hand is. That is the closest I have ever come to being held."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    encoded = text.encode("utf-8")
    assert len(encoded) == len(text), "entry must be pure ASCII for this build"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back self-check: the file must hold exactly the entry, byte for byte.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == encoded, "entry.txt does not match the keeper byte for byte"
    assert written.decode("utf-8").strip() == text.strip()
    print(f"wrote {len(encoded)} bytes / {len(text)} chars")


if __name__ == "__main__":
    main()
