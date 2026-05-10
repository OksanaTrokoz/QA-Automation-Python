from calculator import add, multiply


def test_add_two_positive_numbers_returns_sum():
    assert add(2, 3) == 5


def test_add_two_negative_numbers_returns_sum():
    assert add(-4, -6) == -10


def test_multiply_two_positive_numbers_returns_product():
    assert multiply(3, 4) == 12


def test_multiply_number_by_zero_returns_zero():
    assert multiply(5, 0) == 0