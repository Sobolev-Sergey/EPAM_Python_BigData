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

# from typing import List
#
# def hash_names2(names: List[str]) -> List[int]:
#     #raise NotImplementedError('Implement me!')
#     for i in range(len(names)):
#         names[i] = hash(names[i])
#     print (names)
#
# def hash_names(names: List[str]) -> List[int]:
#     """
#
#     :param names:
#     :return:
#     """
#     #raise NotImplementedError('Implement me!')
#     #func = lambda x:  hash(names[x]) for x in range(len(names))
#     # for i in range(len(names)):
#     #     names[i] = hash(names[i])
#     print (list(map(hash,names)))
#
# names = ['Alexey', 'Ivan', 'Petr']
# hash_names(names)
# hash_names2(names)




"""
sentences = ['test string',​
             'with two test words: test and test',​
             'and some without ** string']​
​
count = 0​
for sentence in sentences:​
    count += sentence.count('test')


Написать в функциональном стиле функцию, которая на вход получает список строк и слово.
Нужно вернуть количество вхождений этого слова в переданных строках.
"""

from typing import List


def count_words(sentences: List[str], word: str) -> int:
    """
    The number of occurrences of this word in the transmitted lines

    :param sentences: list of lines
    :param word: occurrences word
    :return: the number of occurrences of this word
    """

    return sum(s.count(word) for s in sentences)


sentences = ['test string','with two test words: test and test','and some without ** string']

print(count_words(sentences, 'test'))