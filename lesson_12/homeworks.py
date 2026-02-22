def multiply_two_numbers(a,b):
    return a * b

def average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_average_score(self, new_average_score):
        self.average_score = new_average_score

    def get_info(self):
        return f'{self.name}, {self.surname}, {self.age}, {self.average_score}'

