import pytest
from leetcode739 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_daily_temperatures_basic_case(solution):
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures(temperatures) == expected

def test_daily_temperatures_all_increasing(solution):
    temperatures = [30, 40, 50, 60]
    expected = [1, 1, 1, 0]
    assert solution.dailyTemperatures(temperatures) == expected

def test_daily_temperatures_all_decreasing(solution):
    temperatures = [60, 50, 40, 30]
    expected = [0, 0, 0, 0]
    assert solution.dailyTemperatures(temperatures) == expected

def test_daily_temperatures_single_element(solution):
    temperatures = [30]
    expected = [0]
    assert solution.dailyTemperatures(temperatures) == expected

def test_daily_temperatures_alternating(solution):
    temperatures = [30, 60, 30, 60, 30, 60]
    expected = [1, 0, 1, 0, 1, 0]
    assert solution.dailyTemperatures(temperatures) == expected

def test_daily_temperatures_plateau(solution):
    temperatures = [30, 30, 30, 30]
    expected = [0, 0, 0, 0]
    assert solution.dailyTemperatures(temperatures) == expected

def test_daily_temperatures_large_input(solution): #Timeout
    temperatures = [30] * 10000 + [40]
    expected = [10000] * 10000 + [0]
    assert solution.dailyTemperatures(temperatures) == expected

def test_daily_temperatures_no_warmer_days(solution):
    temperatures = [80, 70, 60, 50, 40]
    expected = [0, 0, 0, 0, 0]
    assert solution.dailyTemperatures(temperatures) == expected
