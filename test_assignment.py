import pytest
from assignment import check_number, rectangle_area, is_divisible_by_5, sum_is_even_or_odd, first_last_equal

@pytest.mark.parametrize("num, expected", [
    (5, "Positive"),
    (-7, "Negative"),
    (0, "Neither"),
    (123, "Positive"),
    (-1, "Negative")
])
def test1(num, expected):
    assert check_number(num) == expected


@pytest.mark.parametrize("length, width, expected", [
    (5, 3, 15),
    (10, 2, 20),
    (7, 7, 49),
    (1, 9, 9),
    (0, 5, 0)
])
def test2(length, width, expected):
    assert rectangle_area(length, width) == expected


@pytest.mark.parametrize("num, expected", [
    (25, True),
    (12, False),
    (0, True),
    (55, True),
    (7, False)
])
def test3(num, expected):
    assert is_divisible_by_5(num) == expected


@pytest.mark.parametrize("a, b, c, d, expected", [
    (1, 2, 3, 4, "Even"),   # sum = 10
    (5, 7, 9, 11, "Odd"),   # sum = 32
    (2, 2, 2, 2, "Even"),   # sum = 8
    (0, 1, 2, 3, "Even"),   # sum = 6
    (9, 9, 9, 9, "Even")    # sum = 36
])
def test4(a, b, c, d, expected):
    assert sum_is_even_or_odd(a, b, c, d) == expected


@pytest.mark.parametrize("num, expected", [
    (121, True),
    (4564, True),
    (89, False),
    (7, True),      # single digit → same first & last
    (12345, False)
])
def test5(num, expected):
    assert first_last_equal(num) == expected
