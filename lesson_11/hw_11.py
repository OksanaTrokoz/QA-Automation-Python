numbers = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def sum_numbers(string):
    total = 0
    parts = string.split(",")

    for number in parts:
        total += int(number)
    return total

for item in numbers:
    try:
        result = sum_numbers(item)
        print(result)
    except ValueError:
        print("Не можу це зробити")