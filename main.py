"""Sum up 21 November's world news in one image.

Copies the front page in entry.png to /output/entry.png. The image was
drawn in this session by render-20261121.py from the day's reported
news: Cyclone Akvan's landfall in India, a 6.8 quake in Peru, COP31's
final stretch in Turkey, and more. Python 3.13, standard library only,
no network. Deterministic: the same bytes every run.
"""

import os
import shutil


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    with open(src, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if os.path.getsize(src) > 1024 * 1024:
        raise ValueError("entry.png is over the 1 MiB limit")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
