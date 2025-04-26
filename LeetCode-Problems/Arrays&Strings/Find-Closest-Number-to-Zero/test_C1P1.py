import pytest
from typing import List
from C1P1 import Solution  # Assume the Solution class is in the solution.py file

@pytest.fixture
def solution():
    return Solution()

def test_single_positive_number(solution):
    assert solution.findClosestNumber([10]) == 10

def test_single_negative_number(solution):
    assert solution.findClosestNumber([-10]) == -10

def test_multiple_positive_numbers(solution):
    assert solution.findClosestNumber([5, 11, 20]) == 5

def test_multiple_negative_numbers(solution):
    assert solution.findClosestNumber([-5, -11, -20]) == -5

def test_mixed_numbers(solution):
    assert solution.findClosestNumber([-10, -4, 3, 7, 8]) == 3

def test_mixed_numbers_with_zero(solution):
    assert solution.findClosestNumber([-2, 1, 0, 3]) == 0

def test_negative_and_positive_same_distance(solution):
    assert solution.findClosestNumber([-3, 3, 8, -8]) == 3  # Should return the positive number

def test_empty_list(solution):
    with pytest.raises(IndexError):
        solution.findClosestNumber([])

def test_large_numbers(solution):
    assert solution.findClosestNumber([-100000, 100000, 2, -2]) == 2

def test_large_dataset(solution):
    nums = list(range(-5000, 5001))
    assert solution.findClosestNumber(nums) == 0
