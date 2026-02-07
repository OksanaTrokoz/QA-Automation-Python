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

our_student = Student("Oksana", "Trokoz", 34, 96.67)
print(our_student.get_info())

our_student.change_average_score(99)

print(our_student.get_info())
