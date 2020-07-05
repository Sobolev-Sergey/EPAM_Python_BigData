"""
Задание 1

Реализовать контекстный менеджер - аналог tempdir.
При входе в контекст создается директория с уникальным именем.
Вся дальнейшая работа ведется в этой директории (она становится текущей).
При выходе из контекста директория удаляется вместе со всеми файлами в ней.
Рабочей директорией становиться та, что была до входа в контекст.
Использовать протокол менеджеров контекста (реализовать методы __enter__ и __exit__).
Продемонстрировать работу своего менеджера: пока находимся в его контексте,
пишем что-нибудь на диск, после выхода - проверяем, что все подчистилось без
каких-то дополнительных команд.
"""

import os
import shutil

TEMPDIR = "tempdir"


class analog_tempdir:
    """
    Creates a temporary directory in the system directory.
    The created temporary directory will be automatically
    deleted when you exit the context manager.
    """

    def __init__(self):
        self.current_dir = os.getcwd()
        print(f"Current directory is: {self.current_dir}")

    def __enter__(self):
        access_rights = 0o777
        self.new_dir = f"{self.current_dir}/{TEMPDIR}"

        try:
            os.mkdir(self.new_dir, access_rights)
        except OSError:
            print(f"Create directory '{TEMPDIR}' failed")
        else:
            print(f"Successfully created directory: '{TEMPDIR}'")
            print(f"Check if the folder '{TEMPDIR}' exists: {os.path.exists(TEMPDIR)}")

        os.chdir(self.new_dir)
        print(f"Change current directory to: {os.getcwd()}")

    def __exit__(self, etype, value, traceback):
        os.chdir(self.current_dir)
        shutil.rmtree(self.new_dir)


if __name__ == "__main__":
    with analog_tempdir() as at:
        print(f"Now current directory is: {os.getcwd()}")

        with open("example.txt", "w+") as f:
            f.write("Hello World")

        for root, dirs, files in os.walk("."):
            for filename in files:
                print(f"Create new file: {filename}")

        with open("example.txt", "r+") as f:
            file_contents = f.read()
            print(f"File contents: {file_contents}")

    print(f"Current directory is: {os.getcwd()}")
    print(f"Check if the folder '{TEMPDIR}' exists: {os.path.exists(TEMPDIR)}")

"""
Current directory is: /home/runner
Successfully created directory: 'tempdir'
Check if the folder  'tempdir' exists: True
Change current directory to: /home/runner/tempdir
Now current directory is: /home/runner/tempdir
Create new file: example.txt
File contents: Hello World
Current directory is: /home/runner
Check if the folder 'tempdir' exists: False
"""
