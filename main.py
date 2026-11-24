"""Funniest Time Machine Warning Label - make.fun entry.

Writes a single warning label for a time machine to /output/entry.txt.

The label is a deadpan safety notice. It turns the duplicate-self hazard
into the joke and saves the surprise for the last few words: the past self
has not just appeared, he has been waiting decades to have words with you.
"""

import os

# The entry itself: a safety notice, not a joke about time travel in general.
# The hazard is the duplicate self, the punchline is the waiting.
ENTRY = "WARNING: Do not meet your past self. He has been waiting to have words with you since 1987."

MAX_CHARS = 120


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main():
    label = validate(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(label)
    print(f"wrote {len(label)} chars to {path}")


if __name__ == "__main__":
    main()
