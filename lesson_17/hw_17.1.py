def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i
print(list(even_numbers_generator(10)))

def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
print(list(fibonacci_generator(20)))

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = ReverseIterator([1, 2, 3, 4, 5])
for x in rev: print(x)

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

for num in EvenIterator(16):
    print(num)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function call {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(7, 8)


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))

