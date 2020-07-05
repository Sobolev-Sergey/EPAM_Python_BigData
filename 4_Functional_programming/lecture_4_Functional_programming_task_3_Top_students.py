"""
 У вас есть данные формата ​
[{name: ‘Alexey’, rate: 2, course: ‘Python’}, …]​
​
Выведите топ студентов по каждому из предметов​,

например: {'Python': 'Alexey'}
"""

from typing import List


def get_top(data: List[dict]) -> dict:
    """
    Find the top person for each subject based on the max rate.

    :param data: List of dictionaries with data for a person
    :return: The top person for each subject
    """
    result = {}
    for i in sorted(data, key=lambda k: k['rate']):
        val = list(i.values())
        result[val[2]] = val[0] if val[2] not in result.values() else None

    return result

"""
from operator import itemgetter
from functools import partial
from itertools import groupby
from typing import List

def get_top(data: List[dict]) -> dict:
    #Return top student name by course
    return {course: sorted(students, key=itemgetter('rate'), reverse=True)[0]['name'] 
            for course, students in groupby(sorted(data, key=itemgetter('course')), lambda i: i['course'])}

"""
