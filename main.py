"""ICO from PNG — Build a multi-size ICO from a PNG."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='ico_from_png',
        description='Build a multi-size ICO from a PNG.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('ICO from PNG')
    print('An icon file from one master PNG.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# small fix (2026-11-03)
# update note (2026-11-03)
# tweak (2026-11-04)
# refactor bit (2026-11-05)
# refactor bit (2026-11-05)
# wip (2026-11-05)
