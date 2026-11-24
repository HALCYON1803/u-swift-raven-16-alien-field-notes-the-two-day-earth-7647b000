"""Alien Field Notes: The Two Day Earth Review.

Writes one line to /output/entry.txt: a review of planet Earth
left by an alien tourist. The line is a single clean joke from the
visitor's angle, with the punch at the end.
"""

from pathlib import Path

# One line, invented here. Design: a single joke from the visitor's
# angle — the locals' strangest daily habit, seen as a machine
# powering down — closed with a tourist's star rating, punch last,
# nothing explained.
REVIEW = (
    "The locals go dark for a third of every day "
    "and call it 'sleep'. I tried it. "
    "5/5 stars, would power down again."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
