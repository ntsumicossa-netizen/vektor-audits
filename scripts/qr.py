#!/usr/bin/env python3
"""Make a QR code PNG for an audit: python3 scripts/qr.py <slug> -> qr/<slug>.png"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    import qrcode
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "qrcode[pil]"])
    import qrcode


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/qr.py <slug>")
    slug = sys.argv[1]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        sys.exit(f"invalid slug {slug!r}: use lowercase letters, digits and hyphens")
    domain = json.loads((ROOT / "config.json").read_text())["domain"]
    url = f"https://{domain}/{slug}/"
    out = ROOT / "qr" / f"{slug}.png"
    out.parent.mkdir(exist_ok=True)
    img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=4)
    img.save(out)
    print(f"{url} -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
