"""
Необходимо написать фабрику декораторов(также декоратор).
Фабрика принимает на вход функцию (lambda) возвращает декоратор,
который вернет результат выполнения функции в которую первым
аргументом передается результат выполнения декорируемой функции.

Пример:

@apply(lambda user_id: user_id + 1)
def return_user_id():
  return 42

>> return_user_id()
43

Не забываем про документацию!
"""

import functools

def apply(func_lambda: callable):
    """
    Decorator factory

    :param func_lambda: A function as an input (lambda) returns
    a decorator that returns the result of the function to which
    the result of the decorated function is passed as the first
    argument
    :return: return result for the input function (lambda)
    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result_lambda = func_lambda
            user_id = func(*args, **kwargs)
            return result_lambda(user_id)
        return inner
    return decorator

"""
import functools

def apply(func: callable):
    def decor(original_func):
        @functools.wraps(original_func)
        def wrapper(*args, **kwargs):
            return func(original_func(*args, **kwargs))
        return wrapper
    return decor

"""
