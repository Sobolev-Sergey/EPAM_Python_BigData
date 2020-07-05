"""
Написать декоратор, который будет считать время работы функции
и выводить на экран. Для текущего времени можно использовать
модуль time.​

>> long_running()
0.212341254
complete

"""

import time


def print_run_time(func: callable) -> callable:
    def wrapper():
        start = time()
        print(func())
        print("{}".format(float(time() - start)))

    return wrapper


@print_run_time
def long_running():
    time.sleep(0.2)
    return "complete"
