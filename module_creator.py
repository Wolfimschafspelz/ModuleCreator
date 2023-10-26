import os


class Module:
    def __init__(self, name):
        self.name = name

    def generate_cpp_file(self):
        os.chdir('Private')

        lines = ['#include"Modules/ModuleManager.h"\n\n', 'IMPLEMENT_MODULE(' + self.name + ');\n']
        file_name = self.name + 'Module.cpp'

        file = open(file_name, 'w')
        file.writelines(lines)

        os.chdir('..')

    def generate_build_file(self):
        pass

    def generate_module(self):
        try:
            os.mkdir(self.name)
        except OSError as error:
            print(error)

        os.chdir(self.name)

        try:
            os.mkdir('Private')
        except OSError as error:
            print(error)

        try:
            os.mkdir('Public')
        except OSError as error:
            print(error)

        self.generate_cpp_file()

if __name__ == '__main__':
    moduleName = input('Desired module name: ')

    module = Module(moduleName)
    module.generate_module()
