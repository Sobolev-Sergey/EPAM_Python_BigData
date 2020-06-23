"""
Задание 2. Менеджеры контекста

Написать контекстный менеджер cd, который меняет текущую директорию на заданную.

При входе в контекст нужно запомнить прежнюю директорию и при выходе восстановить ее.

При инициализации менеджера проверьте, что переданный путь существует и это директория.
Если нет, то выбрасывается ValueError.

Используйте методы из модуля os: getcwd, chdir, path.isdir
"""

import os


class cd:
    def __init__(self, newPath):
        if os.path.isdir(newPath):
                self.newPath = newPath
        else:
            raise ValueError

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


if __name__ == '__main__':
    with cd('.') as cm:
        print(f'I am in {os.getcwd()}')
