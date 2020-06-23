"""
Задание 2

Реализовать контекстный менеджер, выводящий в файл следующую информацию:
дата
время выполнения кода
информация о возникшей ошибке (в коде, обернутом контекстным менеджером).
Файл указать при конструировании менеджера.
Файл открывается в режиме append, чтобы при вызове менеджера с одним и тем же файлом информация дописывалась (такой самописный лог).
Выше ошибка прокидывается (происходит reraise).
Используйте ContextDecorator для решения.

Если менеджер наследуется от ContextDecorator, его можно использовать как декоратор
"""

import contextlib
import time
from datetime import datetime

FILE_NAME = "example_log.txt"


class MyContextDecorator(contextlib.ContextDecorator):
    """
    A context manager that outputs the following information to a file:
    date, code execution time,  information about the error that occurred.
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.start_time = time.time()

    def __enter__(self):
        with open(self.file_name, "a+") as f:
            f.write(f"[Info] {datetime.now()}: Start execution code.\n")

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.file_name, "a+") as f:
            result = "Successful"
            if exc_value:
                result = exc_value
            f.write(
                f"[Info] {datetime.now()}: Code execution time: {time.time() - self.start_time}. Result execution: {result}.\n"
            )


def divide(dividend, divider):
    """
    Number division function

    :param dividend: Number dividend
    :param divider: Number divider
    :return:
    """
    try:
        quotient = dividend / divider
        return f"{dividend} is divisible by {divider}, the result is {int(quotient)}"
    except Exception as e:
        raise (Exception(f"Error code: {e}"))


if __name__ == "__main__":
    with MyContextDecorator(FILE_NAME):
        print(divide(4, 2))

    with MyContextDecorator(FILE_NAME):
        print(divide(4, 0))

"""
РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ ПРОГРАММЫ.
Содержимое файла "example_log.txt":

[Info] 2020-06-17 17:17:52.850471: Start execution code.
[Info] 2020-06-17 17:17:52.852471: Code execution time: 0.003001689910888672. Result execution: Successful.
[Info] 2020-06-17 17:17:52.855470: Start execution code.
[Info] 2020-06-17 17:17:52.857471: Code execution time: 0.0039997100830078125. Result execution: Error code: division by zero.

"""
