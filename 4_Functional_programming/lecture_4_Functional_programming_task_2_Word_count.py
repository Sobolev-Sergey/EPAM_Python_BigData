"""
sentences = ['test string',​
             'with two test words: test and test',​
             'and some without ** string']​
​
count = 0​
for sentence in sentences:​
    count += sentence.count('test')


Написать в функциональном стиле функцию, которая на вход получает
список строк и слово.
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

"""
from typing import List


def count_words(sentences: List[str], word: str) -> int:
    #Useless docs
    return sum(s.count(word) for s in sentences)
"""
