from sqrt_func_with_doctest import sqrt


def test_square_root_of_9_positive():
    assert sqrt(9) == 3.0


def test_square_root_of_negative():
    try:
        sqrt(-1)
    except ValueError as e:
        assert e.args[0] == 'Positive value required', \
            'Wrong exception was raised'
        return

    assert False, 'No exception raised'


if __name__ == '__main__':
    test_square_root_of_9_positive()
    test_square_root_of_negative()
