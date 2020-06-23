"""
Написать функцию, которая обертывает любую, передаваемую в нее
функцию и возвращает Tuple[имя функции, результат вызова]
"""

def deanon(func: callable) -> callable:
    def inner(*args, **kwargs):
        return func.__name__, func(*args, **kwargs)

    return inner

"""
def deanon(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        return func.__name__, func(*args, **kwargs)
    return wrapper
"""
