import tempfile, os


class File:
    path = None
    data = None

    def __init__(self, path):
        self.path = path

        with open(path, 'a+') as f:
            f.seek(0)
            raw_data = f.read()
            self.data = raw_data.split("\n")

    def __add__(self, other):
        f = open(self.path)
        content_1 = f.read()
        f.close()

        f = open(other.path)
        content_2 = f.read()
        sum_file_name = os.path.basename(self.path) + os.path.basename(other.path)
        sum_file_path = os.path.join(tempfile.gettempdir(), sum_file_name)
        f = open(sum_file_path, "w+")
        f.write(content_1 + content_2)
        f.close()
        return File(sum_file_path)

    def __iter__(self):
        self._curr = 0
        with open(self.path, "r") as f:
            self._lines = f.readlines()
        return self

    def __next__(self):
        try:
            line = self._lines[self._curr]
            self._curr += 1
            return line
        except IndexError:
            raise StopIteration

    def __str__(self):
        return self.path

    def write(self, new_string):
        with open(self.path, "w") as f:
            self.data.extend(new_string.split('\n'))
            f.write(new_string)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()
