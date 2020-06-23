"""
Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и
изменение данных реализуются через вызовы методов.

В ООП принято имена методов для извлечения данных начинать со слова "get" (взять),
а имена методов, в которых свойствам присваиваются значения, – со слова "set"
(установить).
Например: "get_field", "set_field".
"""


class Field:
    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


field = Field()
field.set_value(123)
print(field.get_value())

"""
class Field:
    def __init__(self):
        self.__value = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


field = Field()
field.set_value(123)
print(field.get_value())
"""
