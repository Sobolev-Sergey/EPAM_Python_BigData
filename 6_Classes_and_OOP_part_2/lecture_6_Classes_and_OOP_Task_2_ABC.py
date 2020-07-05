"""
Создать абстрактный класс Vehicle с методами:
vehicle_type, который выводит имя и тип транспортного средства (ТС),
is_motorcycle, который выводит True/False в зависимости от числа колес (2 колеса -> мотоцикл),
purchase_price - выводит стоимость ТС в зависимости от кол-ва пройденных км: (базовая цена - 0.1 * кол-во км).
Если получился меньше "100" - вернуть "100".

Класс должен содержать поля:
год выпуска
имя бренда
все поля необходимые для обеспечения функциональности классов наследников.

Расставить где необходимо и если необходимо abstractmethod, classmethod, staticmethod или другие декораторы.
Создать классы наследники Vehicle: Car, Motorcycle, Truck, Bus.

vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000),
)


for vehicle in vehicles:
    print(
        f"Vehicle type={vehicle.vehicle_type()}\n"
        f"Is motorcycle={vehicle.is_motorcycle()}\n"
        f"Purchase price={vehicle.purchase_price()}\n"
    )

Vehicle type=Toyota Car
Is motorcycle=False
Purchase price=985000.0

Vehicle type=Suzuki Motorcycle
Is motorcycle=True
Purchase price=796500.0

Vehicle type=Scania Truck
Is motorcycle=False
Purchase price=14915000.0

Vehicle type=MAN Bus
Is motorcycle=False
Purchase price=9905000.0
"""

from abc import ABC
from abc import abstractmethod


class Vehicle(ABC):
    """
    The main abstract class
    """

    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    def vehicle_type(self) -> str:
        """
        Return the name and type of vehicle
        """
        return f"{self.brand_name} {self.__class__.__name__}"

    @abstractmethod
    def is_motorcycle(self) -> bool:
        """
        abstract method that will need to be redefined for each subclass
        """
        pass

    def purchase_price(self) -> float:
        """
        Return the cost of the vehicle depending on the number of miles traveled
        """
        new_price = self.base_price - 0.1 * self.mileage
        return new_price if new_price >=100 else 100


class Car(Vehicle):
    """
    Class Car
    """
    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int, wheels=4):
        super().__init__(brand_name, year_of_issue, base_price, mileage)
        self.wheels = wheels

    def is_motorcycle(self) -> bool:
        """
        Return True if count wheels are two, False is otherwise
        """
        return self.wheels == 2

class Motorcycle(Vehicle):
    """
    Class Motorcycle
    """
    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int, wheels=2):
        super().__init__(brand_name, year_of_issue, base_price, mileage)
        self.wheels = wheels

    def is_motorcycle(self) -> bool:
        """
        Return True if count wheels are two, False is otherwise
        """
        return self.wheels == 2

class Truck(Vehicle):
    """
    Class Truck
    """
    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int, wheels=6):
        super().__init__(brand_name, year_of_issue, base_price, mileage)
        self.wheels = wheels

    def is_motorcycle(self) -> bool:
        """
        Return True if count wheels are two, False is otherwise
        """
        return self.wheels == 2

class Bus(Vehicle):
    """
    Class Bus
    """
    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int, wheels=4):
        super().__init__(brand_name, year_of_issue, base_price, mileage)
        self.wheels = wheels

    def is_motorcycle(self) -> bool:
        """
        Return True if count wheels are two, False is otherwise
        """
        return self.wheels == 2


vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000),
)

for vehicle in vehicles:
    print(
        f"Vehicle type={vehicle.vehicle_type()}\n"
        f"Is motorcycle={vehicle.is_motorcycle()}\n"
        f"Purchase price={vehicle.purchase_price()}\n"
    )

# Vehicle type=Toyota Car
# Is motorcycle=False
# Purchase price=985000.0
#
# Vehicle type=Suzuki Motorcycle
# Is motorcycle=True
# Purchase price=796500.0
#
# Vehicle type=Scania Truck
# Is motorcycle=False
# Purchase price=14915000.0
#
# Vehicle type=MAN Bus
# Is motorcycle=False
# Purchase price=9905000.0



from abc import ABC
from abc import abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels_num(self):
        pass

    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    def vehicle_type(self) -> str:
        return f"{self.brand_name} {self.__class__.__name__}"

    def is_motorcycle(self) -> bool:
        return True if self.wheels_num == 2 else False

    def purchase_price(self) -> float:
        res = self.base_price - 0.1 * self.mileage
        return 100 if res < 100 else res

class Car(Vehicle):
    wheels_num = 4

class Motorcycle(Vehicle):
    wheels_num = 2

class Truck(Vehicle):
    wheels_num = 10

class Bus(Vehicle):
    wheels_num = 6

vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000),
)

for vehicle in vehicles:
    print(
        f"Vehicle type={vehicle.vehicle_type()}\n"
        f"Is motorcycle={vehicle.is_motorcycle()}\n"
        f"Purchase price={vehicle.purchase_price()}\n"
    )
