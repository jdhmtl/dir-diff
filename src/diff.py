#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path

from src.display import TableDisplay


def compare(left: str, right: str):
    left_path = Path(left).resolve()
    right_path = Path(right).resolve()

    left_files = get_dominant_files(left_path)
    right_files = get_dominant_files(right_path)

    only_in_left = only_in_list(left_files, right_files)
    only_in_right = only_in_list(right_files, left_files)

    table = TableDisplay(left, only_in_left, right, only_in_right)
    table.display()


def directory_contents(path: Path):
    if not path.is_dir():
        raise NotADirectoryError(f"Path {path} is not a directory")

    contents = []
    ls = path.iterdir()
    for item in ls:
        if item.is_file():
            contents.append(item)

    return contents


def dominant_file_type(files: list):
    extensions = {}
    for file in files:
        extension = file.suffix
        count = extensions.get(extension, 1)
        extensions.update({extension: count + 1})

    dominant_type = ""
    dominant_count = 0
    for key, value in extensions.items():
        if value > dominant_count:
            dominant_type = key
            dominant_count = value

    return dominant_type


def files_of_type(files: list, file_type: str):
    matching = []
    for file in files:
        if file.suffix == file_type:
            matching.append(file.stem)

    return sorted(matching, key=str.lower)


def get_dominant_files(path: Path):
    files = directory_contents(path)
    file_type = dominant_file_type(files)
    matching_files = files_of_type(files, file_type)

    return matching_files


def only_in_list(reference: list, compared: list):
    compared_lower = list(map(lambda name: name.lower(), compared))

    missing = []
    for item in reference:
        if item.lower() not in compared_lower:
            missing.append(item)

    return missing


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
