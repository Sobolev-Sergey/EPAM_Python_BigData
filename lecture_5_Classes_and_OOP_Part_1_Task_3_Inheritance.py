"""
Создать класс "SchoolMember" который представляет любого человека в школе.
Класс "Teacher" наследуется от "SchoolMember" .
Класс "Student" наследуется от "SchoolMember".

Классы должны иметь одинаковый интерфейс с публичной функцией "show()".

Пример:

>>> persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]

(Created Teacher: Mr.Poopybutthole)
(Created Student: Morty)

>>> for person in persons:
            person.show()

Name: Mr.Poopybutthole, Age: 40, Salary: 3000
Name: Morty, Age: 16, Grades: 75
"""

class SchoolMember:
    """
    Represents anyone at school.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        """
        Shows information about the person
        :return: String with column names: Name, Age.
        """
        return f"Name: {self.name}, Age: {self.age},"


class Teacher(SchoolMember):
    """
    Represents teacher at school.
    """
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        """
        Shows information about the teacher
        """
        return f"{super().show()} Salary: {self.salary}"


class Student(SchoolMember):
    """
    Represents student at school.
    """
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        """
        Shows information about the student
        """
        return f"{super().show()} Grades: {self.grades}"


persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]

for person in persons:
    print(person.show())

"""
class SchoolMember:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print(f"(Created {self.__class__.__name__}: {self.name})")

class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name=name, age=age)
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades):
        super().__init__(name=name, age=age)
        self.grades = grades

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"


persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]

for person in persons:
    print(person.show())

"""
