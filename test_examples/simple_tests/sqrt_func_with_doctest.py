"""
Square root functions

>>> [sqrt(9), sqrt(4)]
[3.0, 2.0]
"""


def sqrt(value):
    """

    :param value: source value
    :type value: int
    :return: float --result of calculation

    >>> sqrt(-1)
    Traceback (most recent call last):
      ...
    ValueError: Positive value required
    """
    if value <= 0:
        raise ValueError('Positive value required')

    return value ** 0.5


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
