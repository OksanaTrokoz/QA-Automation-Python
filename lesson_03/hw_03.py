import math

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
    "That depends a good deal on where you want to get to," said the Cat.
    "I don't much care where ——" said Alice.
    "Then it doesn't matter which way you go," said the Cat.
    "—— so long as I get somewhere," Alice added as an explanation.
    "Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''


# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

# task 04
black_sea_s = 436402
azov_sea_s =  37800
total_area = black_sea_s + azov_sea_s
print(total_area)

# task 05
all_warehouse = 375291
first_second_warehouse = 250449
second_third_warehouse = 222950
third_warehouse = all_warehouse - first_second_warehouse
second_warehouse = second_third_warehouse - third_warehouse
first_warehouse = first_second_warehouse - second_warehouse
print("First warehouse:")
print(first_warehouse)
print("Second warehouse:")
print(second_warehouse)
print("Third warehouse:")
print(third_warehouse)

# task 06
monthly_payment = 1179
payment_period = 18
price_computer = monthly_payment * payment_period
print(price_computer, "грн")

# task 07
a = 8019 % 8
print(a)

b = 9907 % 9
print(b)

c = 2789 % 5
print(c)

d = 7248 % 6
print(d)

e = 7128 % 5
print(e)

f = 19224 % 9
print(f)

# task 08
pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total = pizza_big + pizza_medium + juice + cake + water
print( total, "грн")

# task 09
all_photos = 232
page = 8
all_pages = all_photos // page
print(all_pages)

# task 10
distance = 1600
tank_volume = 48
gas_per_100km = 9
gas_per_trip = distance / 100 * gas_per_100km
print(gas_per_trip)
tanks_per_trip = gas_per_trip / tank_volume
full_tanks_per_trip = math.ceil(tanks_per_trip)
print(full_tanks_per_trip)



