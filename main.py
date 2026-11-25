"""One Line, No Deadline Met: a single-line missed-deadline excuse.

Writes one excuse line to /output/entry.txt. Stdlib only, no
network, deterministic: the same line on every run.
"""

import os

LINE = "I missed the deadline because my calendar and my laptop disagreed on what day it was, and I sided with the wrong one."


def run() -> None:
    directory = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    run()
