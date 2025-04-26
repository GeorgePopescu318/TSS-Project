import pytest
from C1P5 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_max_profit_basic_case(solution):
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5

def test_max_profit_decreasing_prices(solution):
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0

def test_max_profit_all_same_prices(solution):
    prices = [5, 5, 5, 5, 5]
    assert solution.maxProfit(prices) == 0

def test_max_profit_single_element(solution):
    prices = [5]
    assert solution.maxProfit(prices) == 0

def test_max_profit_two_elements_increasing(solution):
    prices = [1, 5]
    assert solution.maxProfit(prices) == 4

def test_max_profit_two_elements_decreasing(solution):
    prices = [5, 1]
    assert solution.maxProfit(prices) == 0

def test_max_profit_large_numbers(solution):
    prices = [999, 1000, 1001, 999, 1002, 1000]
    assert solution.maxProfit(prices) == 3

def test_max_profit_empty_list(solution):
    prices = []
    assert solution.maxProfit(prices) == 0

def test_max_profit_random_case(solution):
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    assert solution.maxProfit(prices) == 4

def test_max_profit_minimum_at_end(solution):
    prices = [7, 2, 4, 8, 1]
    assert solution.maxProfit(prices) == 6
