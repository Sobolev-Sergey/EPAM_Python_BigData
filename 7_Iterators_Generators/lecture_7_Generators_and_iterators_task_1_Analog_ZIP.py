"""
Создайте свой аналог zip с точно таким же поведением и который тоже возвращает итератор.
При реализации нельзя использовать zip, itertools или другие сторонние модули.

>>> list(zip(['A', 'B', 'C'], [1, 2, 3]))
    [('A', 1), ('B', 2), ('C', 3)]

>>> list(zip('!', ['A', 'B', 'C', 'D'], range(1, 3)))
    [('!', 'A', 1)]

>>> list(zip('abcd', ['A', 'B', 'C', 'D'], range(0, 40)))
    [('a', 'A', 0), ('b', 'B', 1), ('c', 'C', 2), ('d', 'D', 3)]

Используйте что сочтете нужным:
Или класс
class CustomZip:
    pass

list(CustomZip(['A', 'B', 'C'], [1, 2, 3], (22, 33, 44, 55, 66)))
# [('A', 1, 22), ('B', 2, 33), ('C', 3, 44)]

Или функцию:
def CustomZip():
    pass

list(custom_zip(['A', 'B', 'C'], [1, 2, 3], (22, 33, 44, 55, 66)))
# [('A', 1, 22), ('B', 2, 33), ('C', 3, 44)]

Используйте имя класса/функции "CustomZip" в каждом случае для простоты тестирования.
"""

class CustomZip:
    pass

# OR

def CustomZip(x, y, z):
    return [(x[i], y[i], z[i]) for i in range(min(len(x), len(y), len(z)))]


list(CustomZip(['A', 'B', 'C'], [1, 2, 3], (22, 33, 44, 55, 66)))
# >> [('A', 1, 22), ('B', 2, 33), ('C', 3, 44)]

"""
def CustomZip(*args):
    iterators = [iter(it) for it in args]
    while True:
        values = []
        for val in iterators:
            try:
                value = next(val)
            except StopIteration:
                return
            values.append(value)
        yield tuple(values)


list(CustomZip(['A', 'B', 'C'], [1, 2, 3], (22, 33, 44, 55, 66)))
# >> [('A', 1, 22), ('B', 2, 33), ('C', 3, 44)]

"""
