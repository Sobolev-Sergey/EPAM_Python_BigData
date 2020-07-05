import pytest

from sqrt_func_with_doctest import sqrt


def test_square_root_of_9_positive():
    assert sqrt(9) == 3.0


def test_square_root_of_negative():
    with pytest.raises(ValueError) as e:
        sqrt(-1)

    assert str(e.value) == 'Positive value required', \
            'Wrong exception was raised'
