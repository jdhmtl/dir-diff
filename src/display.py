
class TableDisplay:
    def __init__(self, left_path: str, left_files: list, right_path: str, right_files: list):
        self.left_path = left_path
        self.right_path = right_path
        self.left_files = left_files
        self.right_files = right_files

        self.left_column_width = self._get_column_width(left_path, left_files)
        self.right_column_width = self._get_column_width(right_path, right_files)

    def display(self):
        if len(self.left_files) == 0 and len(self.right_files) == 0:
            print("Directories contain the same files")
            return

        output = []
        output.extend(self._table_header())
        for i in range(0, max(len(self.left_files), len(self.right_files))):
            output.append(self._file_row(i))

        output.extend(self._table_footer())

        print("\n".join(output))

    def _get_column_width(self, path: str, files: list):
        if not files:
            return len(path)

        return max(len(path), max(len(item) for item in files))

    def _table_border(self):
        return "+" + ("=" * (self.left_column_width + 2)) + "+" + ("=" * (self.right_column_width + 2)) + "+"

    def _table_header(self):
        output = []

        left_path = self.left_path.ljust(self.left_column_width)
        right_path = self.right_path.ljust(self.right_column_width)

        output.append(self._table_border())
        output.append(self._table_row(left_path, right_path))
        output.append(self._table_border())

        return output

    def _table_row(self, left: str, right: str):
        return f"| {left} | {right} |"

    def _table_footer(self):
        output = []

        left_file_count = (str(len(self.left_files))).rjust(self.left_column_width)
        right_file_count = (str(len(self.right_files))).rjust(self.right_column_width)

        output.append(self._table_border())
        output.append(self._table_row(left_file_count, right_file_count))
        output.append(self._table_border())

        return output

    def _file_row(self, index: int):
        left = ""
        if index < len(self.left_files):
            left = self.left_files[index]

        right = ""
        if index < len(self.right_files):
            right = self.right_files[index]

        return self._table_row(left.ljust(self.left_column_width), right.ljust(self.right_column_width))
