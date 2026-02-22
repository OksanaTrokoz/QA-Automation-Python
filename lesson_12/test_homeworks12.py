import unittest
from homeworks import multiply_two_numbers, average, Student

class TestMultiply(unittest.TestCase):
    def test_withZeroMultiplier_returnsZero(self):
        a = 0
        b = 3

        result = multiply_two_numbers(a, b)
        self.assertEqual(0, result)
        result = multiply_two_numbers(b, a)
        self.assertEqual(0, result)

    def test_withTwoPositiveMultipliers_returnsPositiveProduct(self):
        a = 15
        b = 22
        expected = 330

        result = multiply_two_numbers(a, b)
        self.assertEqual(expected, result)
        result = multiply_two_numbers(b, a)
        self.assertEqual(expected, result)

    def test_withTwoNegativeMultipliers_returnsPositiveProduct(self):
        a = -10
        b = -1
        expected = 10

        result = multiply_two_numbers(a, b)
        self.assertEqual(expected, result)
        result = multiply_two_numbers(b, a)
        self.assertEqual(expected, result)

    def test_withSingleNegativeMultipliers_returnsNegativeProduct(self):
        a = -11
        b = 2
        expected = -22

        result = multiply_two_numbers(a, b)
        self.assertEqual(expected, result)
        result = multiply_two_numbers(b, a)
        self.assertEqual(expected, result)

class TestAverage(unittest.TestCase):
    def test_withEmptyList_returnsZero(self):
        numbers = []
        expected = 0

        result = average(numbers)
        self.assertEqual(expected, result)

    def test_withSingleNumber_returnsThatNumber(self):
        numbers = [ 122 ]
        expected = 122

        result = average(numbers)
        self.assertEqual(expected, result)

    def test_withMultiplePositiveNumber_returnsPositiveAverage(self):
        numbers = [1,9, 7, 1, 5]
        expected = 4.6

        result = average(numbers)
        self.assertEqual(expected, result)

    def test_withLessNegativeNumbersThanPositive_returnsPositiveAverage(self):
        numbers = [-1, -2, 3, 4, 5]
        expected = 1.8

        result = average(numbers)
        self.assertEqual(expected, result)

    def test_withMoreNegativeNumbersThanPositive_returnsNegativeAverage(self):
        numbers = [-1, 2, 3, -4, -5]
        expected = -1

        result = average(numbers)
        self.assertEqual(expected, result)

class TestStudent(unittest.TestCase):

    def test_changeAverageScore_withNewScore_updatesAverageScore(self):
        name = "Steven"
        surname = "McSteven"
        age = 20
        average_score = 75

        student = Student(name, surname, age, average_score)
        new_average_score = 90
        student.change_average_score(new_average_score)

        self.assertEqual(new_average_score, student.average_score)

    def test_getInfo_withValidData_returnsFormattedString(self):
        name = "Bondadonk"
        surname = "Cabbagepatch"
        age = 22
        average_score = 88

        student = Student(name, surname, age, average_score)
        expected = "Bondadonk, Cabbagepatch, 22, 88"

        result = student.get_info()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()