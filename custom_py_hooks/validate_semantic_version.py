from __future__ import annotations

import argparse
from semantic_version import Version
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, "rb") as f:
            d = f.read()
            try:
                _ = Version(d.decode())
            except ValueError:
                print(f"{filename}: Not a valid semantic version")
                retval = 1
    return retval


if __name__ == "__main__":
    raise SystemExit(main())
