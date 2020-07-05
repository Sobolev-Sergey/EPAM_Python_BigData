import pytest
from lecture_1_Base_types_task_3_FizzBuzz import fizzbuzz


def test_fizzbuzz_of_positive():
    assert fizzbuzz(1, 2, 3, 4, 5, 6, 15) == [1, 2, "Fizz", 4, "Buzz", "Fizz", "FizzBuzz",]


def test_fizzbuzz_of_negative():
    with pytest.raises(ValueError) as e:
        fizzbuzz(1, 2, 3, "4", 5, 6, 15)
    assert str(e.value) == "Value Error"
