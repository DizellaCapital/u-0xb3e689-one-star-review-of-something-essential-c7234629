"""One-Star Review of Something Essential entry program.

Writes one deadpan one-star review of the sun to
MAKEFUN_OUTPUT_DIR/entry.txt: the sun shows up late all winter,
leaves early, and still expects five stars for one good sunset.
The complaint reads straight and the sting lands in the last few
words. One line, 97 characters, no trailing newline. Stdlib only.
"""

import os
import sys

LINE = "The sun shows up late all winter, leaves early, and still expects five stars for one good sunset."


def main():
    if not (1 <= len(LINE) <= 160):
        print(f"entry must be 1-160 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
