class BuildFile:
    def __init__(self, name):
        self.name = name

    def generate_file(self):
        pass


class Module:
    def __init__(self, name, path):
        self.name = name
        self.path = path


if __name__ == '__main__':
    location = input('Destination path: ')
