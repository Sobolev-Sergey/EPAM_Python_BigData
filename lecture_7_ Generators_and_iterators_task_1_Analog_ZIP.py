# """
# Instructions from your teacher:
#
# Найдите все четные числа из списка VALUES тремя способами:
# функция, которая возвращает List[int]
# функция, которая возвращает Generator
# функция, которая возвращает List[int], но используя однострочный list comprehension
#
# """
#
# from typing import Generator
# from typing import List
#
# VALUES = [
#     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
#     [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
# ]
#
#
# def get_even_for_loop(values: List) -> List[int]:
#     """Return all even numbers using classical for loop.
#     :param values: input list of lists with values
#     :return: list with int values
#     """
#     result = []
#
#     def recursive_iteration(values: List, tree_types=(list, tuple, set)):
#         """
#         Recursive iteration over nested lists
#         :param values: input list of lists with values
#         """
#         for each_item in values:
#             if isinstance(each_item, tree_types):
#                 recursive_iteration(each_item)
#             else:
#                 result.append(each_item)
#
#     recursive_iteration(values)
#
#     output = []
#     for item in result:
#         if item % 2 == 0:
#             output.append(item)
#
#     return output
#
#
# def get_even_for_loop_iterator(values: List) -> Generator:
#     """Return all even numbers using classical for loop.
#     :param values: input list of lists with values
#     :return: generator with int values
#     """
#
#     if type(values) in [list, tuple, set]:
#         for value in values:
#             for each_item in get_even_for_loop_iterator(value):
#                 yield each_item
#     else:
#         if values % 2 == 0:
#             yield values
#
#
# def get_even_list_comprehension(values: List) -> List[int]:
#     """Return all even numbers in ONE LINE using list comprehension.
#     :param values: input list of lists with values
#     :return: list with int values
#     """
#     return [
#         number
#         for value in values
#         for each_item in value
#         for number in each_item
#         if number % 2 == 0
#     ]
#
#
# print(get_even_for_loop(VALUES))
# print(list(get_even_for_loop_iterator(VALUES)))
# print(get_even_list_comprehension(VALUES))
#
# # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
# # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
# # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
#
# ###################################################################################
# # See Model Solution
#
# from typing import Generator
# from typing import List
#
#
# VALUES = [
#     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
#     [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
# ]
#
#
# def get_even_for_loop(values: List) -> List[int]:
#     """Return all even numbers using classical for loop.
#     :param values: input list of lists with values
#     :return: list with int values
#     """
#     res = []
#     for a in values:
#         for b in a:
#             for c in b:
#                 if c % 2 == 0:
#                     res.append(c)
#     return res
#
#
# def get_even_for_loop_iterator(values: List) -> Generator:
#     """Return all even numbers using classical for loop.
#     :param values: input list of lists with values
#     :return: generator with int values
#     """
#     for a in values:
#         for b in a:
#             for c in b:
#                 if c % 2 == 0:
#                     yield c
#
#
# def get_even_list_comprehension(values: List) -> List[int]:
#     """Return all even numbers in ONE LINE using list comprehension.
#     :param values: input list of lists with values
#     :return: list with int values
#     """
#     return [c for a in values for b in a for c in b if c % 2 == 0]
#
#
# print(get_even_for_loop(VALUES))
# print(list(get_even_for_loop_iterator(VALUES)))
# print(get_even_list_comprehension(VALUES))
#


"""
Создайте свой аналог zip с точно таким же поведением и который тоже возвращает итератор.
При реализации нельзя использовать zip, itertools или другие сторонние модули.

 list(zip(['A', 'B', 'C'], [1, 2, 3]))
    [('A', 1), ('B', 2), ('C', 3)]

 list(zip('!', ['A', 'B', 'C', 'D'], range(1, 3)))
    [('!', 'A', 1)]

 list(zip('abcd', ['A', 'B', 'C', 'D'], range(0, 40)))
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


print(list(CustomZip(["A", "B", "C"], [1, 2, 3], (22, 33, 44, 55, 66))))
# >> [('A', 1, 22), ('B', 2, 33), ('C', 3, 44)]
