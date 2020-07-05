"""
Реализовать абстрактный класс валюты, с наследниками Euro, Dollar, Rubble.
Курс пусть будет 1 EUR == 2 USD == 100 RUB

Имплементировать методы из примеров ниже:


print(
    f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n"
    f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n"
    f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n"
)
# Euro.course(Rubble)   ==> 100.0 RUB for 1 EUR
# Dollar.course(Rubble) ==> 50.0 RUB for 1 USD
# Rubble.course(Euro)   ==> 0.01 EUR for 1 RUB

e = Euro(100)
r = Rubble(100)
d = Dollar(200)

print(
    f"e = {e}\n"
    f"e.to(Dollar) = {e.to(Dollar)}\n"
    f"e.to(Rubble) = {e.to(Rubble)}\n"
    f"e.to(Euro)   = {e.to(Euro)}\n"
)
# e = 100 EUR
# e.to(Dollar) = 200.0 USD
# e.to(Rubble) = 10000.0 RUB
# e.to(Euro)   = 100.0 EUR

print(
    f"r = {r}\n"
    f"r.to(Dollar) = {r.to(Dollar)}\n"
    f"r.to(Euro)   = {r.to(Euro)}\n"
    f"r.to(Rubble) = {r.to(Rubble)}\n"
)
# r = 100 RUB
# r.to(Dollar) = 2.0 USD
# r.to(Euro)   = 1.0 EUR
# r.to(Rubble) = 100.0 RUB

print(
    f"e > r   ==> {e > r}\n"
    f"e == d  ==> {e == d}\n"
)
# e > r   ==> True
# e == d  ==> True

print(
    f"e + r  =>  {e + r}\n"
    f"r + d  =>  {r + d}\n"
    f"d + e  =>  {d + e}\n"
)
# e + r  =>  101.0 EUR
# r + d  =>  10100.0 RUB
# d + e  =>  400.0 USD

print(sum([Euro(i) for i in range(5)]))
# 10.0 EUR

"""

from abc import ABC
from abc import abstractmethod
import functools


class Currency(ABC):
    """1 EUR = 2 USD = 100 RUB"""

    def __init__(self, nominal_volume: int):
        self.nominal_volume = nominal_volume

    @abstractmethod
    def course(self):
        pass

    @abstractmethod
    def to(self):
        pass


@functools.total_ordering
class Euro(Currency):
    rate_to_euro = 1.0
    currency_code = "EUR"

    def course(self) -> str:
        current_course = self.__dict__["rate_to_euro"]
        code_currency = self.__dict__["currency_code"]
        return f"{current_course} {code_currency} for 1 {Euro.currency_code}"

    def to(self, currency) -> str:
        return f"{self.nominal_volume * currency.rate_to_euro} {currency.currency_code}"

    def __repr__(self):
        return f"{self.nominal_volume} {Euro.currency_code}"

    def __gt__(self, other) -> bool:
        return self.nominal_volume > (
            other.nominal_volume / other.rate_to_euro
        )

    def __eq__(self, other) -> bool:
        return self.nominal_volume == (
            other.nominal_volume / other.rate_to_euro
        )

    def __add__(self, other):
        return f"{self.nominal_volume + (other.nominal_volume / other.rate_to_euro)} {Euro.currency_code}"


@functools.total_ordering
class Dollar(Currency):
    rate_to_euro = 2.0
    currency_code = "USD"

    def course(self) -> str:
        current_course = self.__dict__["rate_to_euro"] / Dollar.rate_to_euro
        code_currency = self.__dict__["currency_code"]
        return f"{current_course} {code_currency} for 1 {Dollar.currency_code}"

    def to(self, currency) -> str:
        return f"{self.nominal_volume * currency.rate_to_euro / Dollar.rate_to_euro} {currency.currency_code}"

    def __repr__(self):
        return f"{self.nominal_volume} {Dollar.currency_code}"

    def __gt__(self, other) -> bool:
        return (self.nominal_volume / self.rate_to_euro) > (
            other.nominal_volume / other.rate_to_eur
        )

    def __eq__(self, other) -> bool:
        return (self.nominal_volume / self.rate_to_euro) == (
            other.nominal_volume / other.rate_to_eur
        )

    def __add__(self, other):
        return f"{((self.nominal_volume / self.rate_to_euro) + (other.nominal_volume / other.rate_to_euro)) * self.rate_to_euro} {Dollar.currency_code}"


@functools.total_ordering
class Rubble(Currency):
    rate_to_euro = 100.0
    currency_code = "RUB"

    def course(self) -> str:
        current_course = Euro.rate_to_euro / Rubble.rate_to_euro
        code_currency = self.__dict__["currency_code"]
        return f"{current_course} {code_currency} for 1 {Rubble.currency_code}"

    def to(self, currency) -> str:
        return f"{self.nominal_volume * currency.rate_to_euro / Rubble.rate_to_euro} {currency.currency_code}"

    def __repr__(self):
        return f"{self.nominal_volume} {Rubble.currency_code}"

    def __gt__(self, other) -> bool:
        return (self.nominal_volume / self.rate_to_euro) > (
            other.nominal_volume / other.rate_to_euro
        )

    def __eq__(self, other) -> bool:
        return (self.nominal_volume / self.rate_to_euro) == (
            other.nominal_volume / other.rate_to_euro
        )

    def __add__(self, other):
        return f"{((self.nominal_volume / self.rate_to_euro) + (other.nominal_volume / other.rate_to_euro)) * self.rate_to_euro} {Rubble.currency_code}"


def sum(data):
    cash = 0.0
    currency_code = ""
    for i in data:
        string = str(i).split()
        cash += float(string[0])
        currency_code = string[1]
    return f"{cash} {currency_code}"


print(
    f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n"
    f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n"
    f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n"
)

e = Euro(100)
r = Rubble(100)
d = Dollar(200)

print(
    f"e = {e}\n"
    f"e.to(Dollar) ==> {e.to(Dollar)}\n"
    f"e.to(Rubble) ==> {e.to(Rubble)}\n"
    f"e.to(Euro)   ==> {e.to(Euro)}\n"
)
print(
    f"r = {r}\n"
    f"r.to(Dollar) ==> {r.to(Dollar)}\n"
    f"r.to(Euro)   ==> {r.to(Euro)}\n"
    f"r.to(Rubble) ==> {r.to(Rubble)}\n"
)

print(
    f"e > r  ==> {e > r}\n"
    f"e == d ==> {e == d}\n"
)

print(
    f"e + r  =>  {e + r}\n"
    f"r + d  =>  {r + d}\n"
    f"d + e  =>  {d + e}\n"
)

print(sum([Euro(i) for i in range(5)]))

"""
import functools

@functools.total_ordering
class Currency:
    
    # 1 EUR = 2 USD = 100 RUB
    # 
    # 1 EUR = 2 USD    ;  1 EUR = 100 RUB
    # 1 USD = 0.5 EUR  ;  1 USD = 50 RUB
    # 1 RUB = 0.02 USD ;  1 RUB = 0.01 EUR
    

    label = None
    usd_rate = None

    def __init__(self, value: int):
        self.value = value

    @property
    def _usd_val(self) -> int:
        return self.value * self.usd_rate

    @classmethod
    def course(cls, other_cls):
        return f"{cls(1).to(other_cls)} for 1 {cls.label}"

    def to(self, other_cls) -> float:
        new_currency_val = self._usd_val / other_cls.usd_rate
        return other_cls(new_currency_val)

    def __add__(self, other):
        new_val = self.value + other.to(self.__class__).value
        return self.__class__(new_val)

    def __radd__(self, other):
        new_val = self.value + other
        return self.__class__(new_val)

    def __eq__(self, other):
        return self._usd_val == other._usd_val

    def __lt__(self, other):
        return self._usd_val < other._usd_val

    def __repr__(self):
        return f"{self.value} {self.label}"


class Euro(Currency):
    label = "EUR"
    usd_rate = 2  # 1EUR == 2USD


class Dollar(Currency):
    label = "USD"
    usd_rate = 1  # 1USD == 1USD


class Rubble(Currency):
    label = "RUB"
    usd_rate = 0.02  # 1RUB == 0.02USD


print(
    f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n"
    f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n"
    f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n"
)

e = Euro(100)
r = Rubble(100)
d = Dollar(200)

print(
    f"e = {e}\n"
    f"e.to(Dollar) ==> {e.to(Dollar)}\n"
    f"e.to(Rubble) ==> {e.to(Rubble)}\n"
    f"e.to(Euro)   ==> {e.to(Euro)}\n"
)
print(
    f"r = {r}\n"
    f"r.to(Dollar) ==> {r.to(Dollar)}\n"
    f"r.to(Euro)   ==> {r.to(Euro)}\n"
    f"r.to(Rubble) ==> {r.to(Rubble)}\n"
)

print(
    f"e > r  ==> {e > r}\n"
    f"e == d ==> {e == d}\n"
)

print(
    f"e + r  =>  {e + r}\n"
    f"r + d  =>  {r + d}\n"
    f"d + e  =>  {d + e}\n"
)

print(sum([Euro(i) for i in range(5)]))

"""
