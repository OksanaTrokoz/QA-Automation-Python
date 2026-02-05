# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_two_numbers(a,b):
    return a + b

a = 3
b = 4
print(add_two_numbers(a,b))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_with_cycle(numbers):
    size = len(numbers)

    if size == 0:
        return 0

    sum = 0

    for number in numbers:
        sum += number

    return sum / size

def average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]

s = "abc123"
print(reverse_string(s))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    return max(words, key = lambda w: len(w))

words = ["abc", "big", "cat", "dad", "eat", "family", "game", "house"]
print(longest_word(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def count_title_words(text):
    words_list = text.split()
    count_capital = 0

    for word in words_list:
        if word.istitle():
            count_capital = count_capital + 1

    return count_capital

print(f"count_title_words = {count_title_words(str1)}")

# task 8
def validate_unique_symbols(text, threshold):
    unique_symbols = set(text)
    return len(unique_symbols) >= threshold

print(validate_unique_symbols(str1, 10))

# task 9
def check_contains_letter(text, letter):
    if letter.lower() in text.lower():
        print(f'The letter {letter} is in the text.')
    else:
        print(f'The letter {letter} is not in the text.')

check_contains_letter(str1, 'z')

# task 10
def search_cars(car_data, search_criteria):
    year = search_criteria[0]
    engine_volume = search_criteria[1]
    price = search_criteria[2]

    filtered_cars = {
      car_name: car_info for car_name, car_info in car_data.items()
      if car_info[1] >= year
      and car_info[2] >= engine_volume
      and car_info[4] <= price
    }

    return filtered_cars

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Tesla': ('silver', 2021, 0.0, 'sedan', 60000)
}
search_criteria = (2020, 1.6, 60000)

print(search_cars(car_data, search_criteria))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""