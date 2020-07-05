"""
Дописать универсальные функции работы с множествами​.
Функции должны принимать произвольное число аргументов разных типов: list, tuple, set.
Возвращать должны set.

>>> intersect(s1, s2), union(s1, s2) # Два операнда​
([‘S’, ‘A’, ‘M’], [‘S’, ‘P’, ‘A’, ‘M’, ‘C’])​
>>> intersect([1,2,3], (1,4)) # Смешивание типов​
[1]
"""


def union(first, *args) -> set:
    result = set(first)
    for arg in args:
        result = result.union(set(arg))
        # result |= set(arg)
    return result


def intersect(first, *args) -> set:
    result = set(first)
    for arg in args:
        result = result.intersection(set(arg))
        # result &= set(arg)
    return result

"""
def union(first, *args) -> set:
    result = set(first)
    for arg in args:
        result = result.union(set(arg))
    return result

def intersect(first, *args) -> set:
    result = set(first)
    for arg in args:
        result = result.intersection(set(arg))
    return result
"""
