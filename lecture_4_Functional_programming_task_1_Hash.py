"""
Преобразовать код в императивном стиле

names = ['Alexey', 'Ivan', 'Petr']​
​
for i in range(len(names)):​
    names[i] = hash(names[i])​
​
print(names)​

в функциональный.
функция hash_names на вход принимает список строк, на выход - список интов.

Не забываем про документацию!
"""

from typing import List


def hash_names(names: List[str]) -> List[int]:
    """
    Accepts a list of lines as input, as a list of int as output.

    :param names: list of lines
    :return: hash lines in int
    """
    # raise NotImplementedError('Implement me!')
    return (list(map(hash, names)))

"""
from typing import List

def hash_names(names: List[str]) -> List[int]:
    #Take list of strings and return list of hashes
    return list(map(hash, names))
"""
