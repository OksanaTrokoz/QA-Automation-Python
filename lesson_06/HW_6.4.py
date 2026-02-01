list_from_range = list(range(1, 20))

even_numbers = sum([x for x in list_from_range if x % 2 == 0])
print(even_numbers)