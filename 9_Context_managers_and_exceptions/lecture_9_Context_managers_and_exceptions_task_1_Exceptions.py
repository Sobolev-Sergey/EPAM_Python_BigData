"""
Задание 1. Исключения
Функция divide принимает строку, которая содержит два целых числа с пользовательского ввода, разделенные пробелами.

Необходимо выполнить операцию деления (a / b) и вернуть результат или сообщение о возникшей ошибке.

Шаблон строки с сообщением об ошибке:

Error code: {exception}
`

Пример взаимодействия:

 1 0
Error code: division by zero

 9 $
Error code: invalid literal for int() with base 10: '$'

 6 2
3
"""

# def divide(user_input):
#     try:
#         a,b =[int(num) for num in user_input.split()]
#         return a/b
#     except Exception as e:
#         return f"Error code: {e}"
#
#
# if __name__ == '__main__':
#     while True:
#         print(divide(input()))

"""
Задание 2. Менеджеры контекста

Написать контекстный менеджер cd, который меняет текущую директорию на заданную.  

При входе в контекст нужно запомнить прежнюю директорию и при выходе восстановить ее.  

При инициализации менеджера проверьте, что переданный путь существует и это директория. 
Если нет, то выбрасывается ValueError.

Используйте методы из модуля os: getcwd, chdir, path.isdir
"""

import os


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



