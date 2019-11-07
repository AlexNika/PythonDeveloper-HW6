from math import pi, sqrt, pow, hypot, factorial, fabs
import pytest


def get_filter_test_data():
    """
    :return: list of param tuples for function test_filter
    """
    list1 = list(range(2, 25))
    list2 = [10, 4, 2, -1, 6]
    check_list1 = [5, 7, 11, 13, 17, 19, 23]
    check_list2 = [4, 2, -1]
    f1 = (lambda x: x % 2 != 0 and x % 3 != 0)
    f2 = (lambda x: x < 5)
    return [(list1, f1, check_list1), (list2, f2, check_list2)]


def get_map_test_data():
    """
    :return: list of param tuples for function test_map
    """
    list1 = list(range(1, 11))
    list2 = [7, 2, 3, 10, 12]
    check_list1 = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    check_list2 = [5040, 2, 6, 3628800, 479001600]
    f1 = (lambda x: pow(x, 3))
    f2 = (lambda x: factorial(x))
    return [(list1, f1, check_list1), (list2, f2, check_list2)]


def get_sorted_test_data():
    """
    :return: list of param tuples for function test_sorted
    """
    list1 = [3, 2, 5, 4, 7, 1]
    list2 = [3, 6, -8, 2, -78, 1, 23, -45, 9]
    key1 = None
    key2 = abs
    check_list1 = [1, 2, 3, 4, 5, 7]
    check_list2 = [1, 2, 3, 6, -8, 9, 23, -45, -78]
    return [(list1, key1, check_list1), (list2, key2, check_list2)]


def get_pi_test_data():
    """
    :return: list of param tuples for function test_pi
    """
    return [(5, 3.14159), (10, 3.1415926536), (15, 3.141592653589793)]


def get_sqrt_test_data():
    """
    :return: list of param tuples for function test_sqrt
    """
    return [(0, 0), (1, 1), (-2, 'ValueError'), (9, 3), (6.25, 2.5)]


def get_pow_test_data():
    """
    :return: list of param tuples for function test_pow
    """
    return [(0, 0, 1), (2, 3, 8), (10, 2, 100), (10, -2, 0.01)]


def get_hypot_test_data():
    """
    :return: list of param tuples for function test_hypot
    """
    return [(1, 1, 1.4142135623730951), (50, -25, 55.90169943749474),
            (2.5, 2.5, 3.5355339059327378), (95e200, 168e200, 1.9299999999999998e+202)]


@pytest.mark.parametrize('decimal_place, expected', get_pi_test_data())
def test_pi(decimal_place, expected):
    """
    :param decimal_place:
    :param expected:
    :return: test assertions for test_pi function
    """
    assert round(pi, decimal_place) == expected


def test_pi_output_type():
    """
    :return: test assertions for test_pi_output_type function
    """
    assert type(pi) is float


@pytest.mark.parametrize('num, expected', get_sqrt_test_data())
def test_sqrt(num, expected):
    """
    :param num:
    :param expected:
    :return: test assertions for test_sqrt function
    """
    try:
        assert sqrt(num) == expected
    except ValueError:
        return ValueError


@pytest.mark.parametrize('x, y, expected', get_pow_test_data())
def test_pow(x, y, expected):
    """
    :param x:
    :param y:
    :param expected:
    :return: test assertions for test_pow function
    """
    assert pow(x, y) == expected


@pytest.mark.parametrize('x, y, expected', get_hypot_test_data())
def test_hypot(x, y, expected):
    """
    :param x:
    :param y:
    :param expected:
    :return: test assertions for test_hypot function
    """
    assert hypot(x, y) == expected


@pytest.mark.parametrize('my_list, my_function, expected', get_filter_test_data())
def test_filter(my_list, my_function, expected):
    """
    :param my_list:
    :param my_function:
    :param expected:
    :return: test assertions for test_filter function
    """
    assert list(filter(my_function, my_list)) == expected


@pytest.mark.parametrize('my_list, my_function, expected', get_map_test_data())
def test_map(my_list, my_function, expected):
    """
    :param my_list:
    :param my_function:
    :param expected:
    :return: test assertions for test_map function
    """
    assert list(map(my_function, my_list)) == expected


@pytest.mark.parametrize('my_list, sort_key, expected', get_sorted_test_data())
def test_sorted(my_list, sort_key, expected):
    """
    :param my_list:
    :param sort_key:
    :param expected:
    :return: test assertions for test_sorted function
    """
    assert sorted(my_list, key=sort_key) == expected
