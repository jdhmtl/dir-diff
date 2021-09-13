from pathlib import Path


class DirectoryCompare:
    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right

    def compare(self):
        left_path = Path(self.left).resolve()
        right_path = Path(self.right).resolve()

        left_files = self._get_dominant_files(left_path)
        right_files = self._get_dominant_files(right_path)

        only_in_left = self._get_exclusive_files(left_files, right_files)
        only_in_right = self._get_exclusive_files(right_files, left_files)

        return only_in_left, only_in_right

    def _determine_dominant_file_type(self, files: list[Path]) -> str:
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

    def _get_directory_contents(self, path: Path) -> list[Path]:
        if not path.is_dir():
            raise NotADirectoryError(f"Path {path} is not a directory")

        contents = []
        ls = path.iterdir()
        for item in ls:
            if item.is_file():
                contents.append(item)

        return contents

    def _get_dominant_files(self, path: Path) -> list[str]:
        files = self._get_directory_contents(path)
        file_type = self._determine_dominant_file_type(files)
        matching_files = self._get_files_of_type(files, file_type)

        return matching_files

    def _get_exclusive_files(self, reference: list, compared: list) -> list[str]:
        compared_lower = list(map(lambda name: name.lower(), compared))

        missing = []
        for item in reference:
            if item.lower() not in compared_lower:
                missing.append(item)

        return missing

    def _get_files_of_type(self, files: list[Path], file_type: str) -> list[str]:
        matching = []
        for file in files:
            if file.suffix == file_type:
                matching.append(file.stem)

        return sorted(matching, key=str.lower)
