"""
Написать декоратор validate, который будет валидировать входящие
аргументы функции на предмет выхода за заданные границы
Если параметры верны, должен возвращать вывод функции. Если нет,
должен возвращать строку "Function call is not valid!​"

>>> @validate(low_bound=0, upper_bound=256)​
... def set_pixel(red, green, blue):​
...     print("Pixel created!")​
... ​
>>> set_pixel(0, 127, 300)​
Function call is not valid!​
>>> set_pixel(0, 127, 250) ​
Pixel created!​
​
Не забываем про документацию!
"""

import functools

def validate(low_bound=None, upper_bound=None):
    """
    The decorator checks the input arguments of
    the function in the specified range

    :param low_bound: low bound
    :param upper_bound: upper bound
    :return: Return the output for the function.
    Or the message "Call to function is invalid!" otherwise.
    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            r, g, b = args
            if (
                (r < low_bound or r > upper_bound)
                or (g < low_bound or g > upper_bound)
                or (b < low_bound or b > upper_bound)
            ):
                return "Function call is not valid!"
            else:
                return func(*args, **kwargs)
        return inner
    return decorator


def set_pixel(red, green, blue):
    """Just create a pixel"""
    return("Pixel created!")

"""
import functools

def validate(low_bound: int, upper_bound: int) -> callable:
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args: int):
            for arg in args:
                if not (low_bound <= arg <= upper_bound):
                    return 'Function call is not valid!'
            return func(*args)
        return wrapper
    return decor


def set_pixel(red: int, green: int, blue: int) -> str:
    #Just create a pixel
    return "Pixel created!"
"""
