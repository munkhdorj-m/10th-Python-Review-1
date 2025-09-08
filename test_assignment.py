import pytest
from assignment import find_ticket_price, is_four_digit_number, is_divisible, sum_of_even_numbers, convert_time_to_days_hours

@pytest.mark.parametrize("age, expected", [
    (2, 0),
    (5, 10),
    (30, 15),
    (70, 12)
])
def test1(age, expected):
    assert find_ticket_price(age) == expected

@pytest.mark.parametrize("number, expected", [
    (1234, True),
    (99, False),
    (10000, False),
    (5678, True)
])
def test2(number, expected):
    assert is_four_digit_number(number) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, True),
    (15, 4, False),
    (20, 5, True),
    (7, 3, False)
])
def test3(num1, num2, expected):
    assert is_divisible(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, num3, expected", [
    (2, 4, 6, 12),
    (1, 2, 3, 2),
    (5, 7, 8, 8),
    (12, 15, 9, 12)
])
def test4(num1, num2, num3, expected):
    assert sum_of_even_numbers(num1, num2, num3) == expected


@pytest.mark.parametrize("hours, expected", [
    (48, (2, 0)),
    (25, (1, 1)),
    (72, (3, 0)),
    (49, (2, 1))
])
def test5(hours, expected):
    assert convert_time_to_days_hours(hours) == expected
