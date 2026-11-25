"""Write the 26 November 2026 world-news front page to /output/entry.png.

Deterministic: copies the entry.png shipped beside this file, with no
network and no randomness, then reads the output back and verifies it is
byte-identical to the shipped image.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    src_hash = sha256(SOURCE)
    out_hash = sha256(OUTPUT)
    assert src_hash == out_hash, "output differs from shipped entry.png"
    size = OUTPUT.stat().st_size
    assert size <= 1_048_576, f"entry.png is {size} bytes, over the 1 MiB cap"
    print(f"wrote {OUTPUT} ({size} bytes, sha256 {out_hash})")


if __name__ == "__main__":
    main()
