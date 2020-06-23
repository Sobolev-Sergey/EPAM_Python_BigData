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

def divide(user_input):
    try:
        a,b =[int(num) for num in user_input.split()]
        return a/b
    except Exception as e:
        return f"Error code: {e}"


if __name__ == '__main__':
    while True:
        print(divide(input()))
