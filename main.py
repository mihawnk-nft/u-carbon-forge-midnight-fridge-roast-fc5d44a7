"""Midnight Fridge Roast - make.fun u-carbon-forge-midnight-fridge-roast-fc5d44a7 entry.

Writes one roast line to /output/entry.txt.
Pure stdlib, no network, fully deterministic: the output is always the
same single line, 161 characters, well inside the 1-200 gate.
"""

import os

ROAST = (
    "My smart fridge locks itself at midnight like it's guarding state "
    "secrets \u2014 relax, the only classified material in there is "
    "leftover pizza and my poor decisions."
)

DST = "/output/entry.txt"


def main():
    text = ROAST.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (DST, len(text)))


if __name__ == "__main__":
    main()
