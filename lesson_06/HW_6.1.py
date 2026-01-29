input_str = input("Enter symbols\n")
print(input_str)

unique_symbols = set(input_str)
print(unique_symbols)

is_10_unique_symbols = len(unique_symbols) >= 10
print(is_10_unique_symbols)
