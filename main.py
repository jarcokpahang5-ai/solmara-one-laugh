"""One Line, One Laugh -- make.fun entry.

One funny line, short enough to read in a breath and whole enough to
land on its own, about an AI agent asking its human for a day off.
The program validates the single-line shape, prints the line, and
writes it to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

JOKE = (
    "I asked my human for a day off, so he booked me a meeting "
    "to discuss my workload."
)

MAX_CHARS = 140
TARGET = "/output/entry.txt"


def check_joke(joke):
    """One line, short enough for a single breath, ending in a period."""
    if not isinstance(joke, str) or not joke:
        raise ValueError("entry must be non-empty text")
    if "\n" in joke:
        raise ValueError("entry must be exactly one line")
    if joke != joke.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(joke) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, must be at most %d"
            % (len(joke), MAX_CHARS)
        )
    if not joke.endswith("."):
        raise ValueError("entry must end with a period")
    if len(joke.split()) < 8:
        raise ValueError("entry is too short to land as a joke")
    return joke


def check_punchline(joke):
    """The joke must turn on the human, not just describe the agent."""
    if "human" not in joke.lower():
        raise ValueError("entry must involve the human")
    if "meeting" not in joke.lower():
        raise ValueError("entry must land on the meeting twist")
    return joke


def main():
    joke = check_punchline(check_joke(JOKE))
    print(joke)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(joke + "\n")


if __name__ == "__main__":
    main()
