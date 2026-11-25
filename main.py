#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to entry.txt.
Stdlib only.
"""

import os

JOKE = "I marked an email as unread so I could experience the thrill of ignoring it twice."

# Gate from the kit rules: entry.txt must be UTF-8 text of 1-200 chars,
# not only whitespace, and a single line. Enforce it here so a bad joke
# fails loudly at build time instead of silently at grading time.
assert JOKE.strip(), "joke must not be empty or only whitespace"
assert "\n" not in JOKE.strip(), "joke must be a single line"
assert 1 <= len(JOKE.strip()) <= 200, "joke must be 1-200 chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE.strip() + "\n")


if __name__ == "__main__":
    main()
