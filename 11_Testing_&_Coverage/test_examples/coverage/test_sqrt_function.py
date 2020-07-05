from datetime import date
import pytest

from sqrt_function import sqrt


def test_int_sqrt():
    assert 4 == sqrt(16)
    

def test_str_sqrt():
    assert 5 == sqrt('25')


def test_date_sqrt():
    with pytest.raises(ValueError) as e:
        sqrt(date.today())

    assert str(e.value) == "Unsuported type passed: <class 'datetime.date'>", \
        'Wrong exception was raised'
