# Task_1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        self.team_size = team_size

lead = TeamLead("Oksana", 100000, "Main", "Pyton", 9001)
print(f"Manager: {lead.name}, {lead.department}, {lead.salary}")
print(f"Developer: {lead.name}, {lead.programming_language}, {lead.salary}")

#Task_2
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return 4 * self.__side_length

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.__radius


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


figures = [
    Square(4),
    Circle(5),
    Rectangle(4, 6),
]

for figure in figures:
    print("Figure:", figure.__class__.__name__)
    print("Area =", figure.area())
    print("Perimeter =", figure.perimeter())
    print()


