"""One-Sentence Absurd Invention Pitch — a toothbrush with a grudge.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output/entry.txt). The pitch: a toothbrush that hums your least
favourite song until you brush for the full two minutes, then stops
mid-chorus as a reward. The laugh comes from the invention itself —
a toothbrush that weaponises your own taste in music against you —
and the fix is silly yet weirdly plausible: shame, set to music,
with a chorus-shaped carrot.
"""

import os

ENTRY = "A toothbrush that hums your least favourite song until you brush for the full two minutes, then stops mid-chorus as a reward."

# Gate: one sentence, 1-220 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 220, "entry must be 1-220 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single sentence on one line"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be exactly one sentence"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify what actually landed on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    assert 1 <= len(written) <= 220, "written entry out of range"


if __name__ == "__main__":
    main()
