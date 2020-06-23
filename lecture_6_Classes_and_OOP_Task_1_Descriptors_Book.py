"""
Создать класс Book с аттрибутами price, author, name.

Автор и название книги не должны меняться. (Выкидываем ValueError)
Цена может меняться, но должна находится в пределах: 0 <= price <= 100


>>> b = Book("William Faulkner", "The Sound and the Fury", 12)

>>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
Author='William Faulkner', Name='The Sound and the Fury', Price='12'

>>> b.price = 55
>>> b.price
55
>>> b.price = -12  # => ValueError: Price must be between 0 and 100.
>>> b.price = 101  # => ValueError: Price must be between 0 and 100.

>>> b.author = "new author"  # => ValueError: Author can not be changed.
>>> b.name = "new name"      # => ValueError: Name can not be changed.

"""


class PriceControl:
    """
    Class controlling price range
    """

    def __init__(self):
        self.price = 0

    def __get__(self, instance, owner):
        return self.price

    def __set__(self, instance, value):
        """
        The price may vary, but should be in the range:
        0 <= price <= 100
        """
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.price = value

class NameControl:
    """
    Class for controlling fields author and name
    """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        Adding new fields.
        The fields author and name can not be changed.
        """
        if self.name in instance.__dict__:
            if 'author' == self.name:
                raise ValueError("Author can not be changed.")
            if 'name' == self.name:
                raise ValueError("Name can not be changed.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Book:
    """
    Class Book
    """
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author: str, name: str, price: int):
        self.author = author
        self.name = name
        self.price = price


b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# Author='William Faulkner', Name='The Sound and the Fury', Price='12'

b.price = 55
print(b.price)
# 55

# b.price = -12  # => ValueError: Price must be between 0 and 100.
# print(b.price)
# b.price = 101  # => ValueError: Price must be between 0 and 100.
# print(b.price)
#
# b.author = "new author"  # => ValueError: Author can not be changed.
# print(b.author)
# b.name = "new name"      # => ValueError: Name can not be changed.
# print(b.name)
# b.bla = "asd"
# print(b.bla)


"""
class PriceControl:

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Price must be between 0 and 100.")

    def __set_name__(self, owner, name):
        self.name = name


class NameControl:

    def __set__(self, instance, value):
        if not instance.__dict__.get(self.name, None):
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"{self.name.capitalize()} can not be changed.")

    def __set_name__(self, owner, name):
        self.name = name


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author: str, name: str, price: int):
        self.author = author
        self.name = name
        self.price = price


b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")

b.price = 55
print(b.price)

"""
