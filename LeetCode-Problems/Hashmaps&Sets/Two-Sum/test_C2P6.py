import pytest
from typing import List
from C2P6 import Solution  # Assuming the code is in a file named solution.py

@pytest.fixture
def solution():
    return Solution()

def test_two_sum_basic_case(solution):
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [1, 0]

def test_two_sum_multiple_possible_pairs(solution):
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [2, 1]

def test_two_sum_same_element_used_twice(solution):
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [1, 0]

def test_two_sum_no_solution(solution):
    nums = [1, 2, 3]
    target = 7
    # No solution is expected, should handle the case gracefully if specified
    assert solution.twoSum(nums, target) is None

def test_two_sum_large_numbers(solution):
    nums = [1000000000, 250, 123456789, -1000000000]
    target = 123456789
    assert solution.twoSum(nums, target) == [2, 1]

def test_two_sum_negative_numbers(solution):
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert solution.twoSum(nums, target) == [4, 2]

def test_two_sum_zero_and_negatives(solution):
    nums = [0, 4, 3, 0]
    target = 0
    assert solution.twoSum(nums, target) == [3, 0]

def test_two_sum_identical_elements(solution):
    nums = [1, 1, 1, 1]
    target = 2
    assert solution.twoSum(nums, target) == [1, 0]

def test_two_sum_with_zeros(solution):
    nums = [0, 4, 3, 0]
    target = 0
    assert solution.twoSum(nums, target) == [3, 0]

def test_two_sum_boundary_case_empty_list(solution):
    nums = []
    target = 0
    assert solution.twoSum(nums, target) is None
