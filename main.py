#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun bounty entry.

Writes one funny line from a hopeless tech support agent to a desperate
customer to /output/entry.txt.

The line: the customer's whole thesis just vanished (their desperation is
felt, never explained), and the agent — cheerful, useless, and proud of
the little green light — declares the reboot a victory. The classic
"turn it off and on again" is the setup; the twist is that the agent
treats a glowing LED as a win while the customer's work stays gone.
The customer is never the butt of the joke: the agent is.
"""

import os

ENTRY = (
    "I know your whole thesis just vanished \u2014 but I turned it off and on "
    "again, and the little light is green now, so technically we're winning."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 199:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-199")
    if "\n" in text or text != text.strip():
        raise SystemExit("entry must be a single line with no surrounding space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the file the judge sees must be exactly the line above.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("round-trip check failed: entry.txt differs")


if __name__ == "__main__":
    main()
