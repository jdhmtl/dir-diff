#!/usr/bin/env python3

from argparse import ArgumentParser

from src.compare import DirectoryCompare
from src.display import TableDisplay


def compare(left: str, right: str):
    comparator = DirectoryCompare(left, right)
    left_files, right_files = comparator.compare()

    table = TableDisplay(left, left_files, right, right_files)
    table.display()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("left", help="Directory to compare")
    parser.add_argument("right", help="Other directory to compare")
    args = parser.parse_args()

    try:
        compare(args.left, args.right)
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)
