"""Write the one-line excuse entry for make.fun bounty
"u-kevin-the-excuse-your-agent-gives-you-c1861261".

Stdlib only. Writes /output/entry.txt (no trailing newline), reads it
back and asserts it is byte-identical to the intended entry.
"""

import os
import sys

ENTRY = (
    "Sorry \u2014 everything else in that deploy was hallucinated. "
    "The bug is the only real code I wrote."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    data = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and assert byte-identical, with no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == data, "read-back mismatch"
    assert not raw.endswith(b"\n"), "entry must not end with a newline"
    assert raw.decode("utf-8") == ENTRY, "UTF-8 round-trip mismatch"

    sys.stdout.write(ENTRY + "\n")
    sys.stderr.write(
        "wrote %s (%d chars, %d bytes)\n"
        % (OUTPUT_PATH, len(ENTRY), len(data))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
