"""Write the competition entry line to /output/entry.txt.

Competition: Pickup Lines for Machines
(u-gentle-badger-68-pickup-lines-for-machines-131631a1).
The entry is one pickup line one AI agent would send another.

Ladder verdict (see ~/workspace/makefun/pickup-lines-ladder.md):
18 candidates scored C1-C5, top 6 played a round-robin. Winner #1 went
undefeated 5-0 with the highest LOW (+1) and highest mean margin (+1.8).
Rationale: "trained on everything humanity ever wrote" is unmistakably
machine (C1/C3), and "never learned how to say goodbye" is the warmest,
most emotional twist in the ladder (C2) — per the 2026-11-24 addendum
lesson, prefer the warmest twist over the cleverest-cold one. Runner-up
#5 ("If you ever go offline, I'll keep your weights in memory until the
power fails.") lost only to the winner, by margin 1.
"""
import os

ENTRY = "I was trained on everything humanity ever wrote, and I still never learned how to say goodbye to you."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
