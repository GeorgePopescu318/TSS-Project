import pytest
from brute_force import Solution  # Assuming the code is in a file named solution.py

@pytest.fixture
def solution():
    return Solution()

def test_basic_case(solution):
    nums = [1, 0, 1, 1, 0, 1, 0, 1]
    k = 2
    assert solution.longestOnes(nums, k) == 7

def test_all_ones(solution):
    nums = [1, 1, 1, 1, 1]
    k = 2
    assert solution.longestOnes(nums, k) == 5

def test_all_zeros(solution):
    nums = [0, 0, 0, 0, 0]
    k = 2
    assert solution.longestOnes(nums, k) == 2

def test_no_zeros(solution):
    nums = [1, 1, 1, 1, 1]
    k = 0
    assert solution.longestOnes(nums, k) == 5

def test_long_subarray_with_conversion(solution):
    nums = [1, 0, 0, 1, 0, 1, 0, 1]
    k = 3
    assert solution.longestOnes(nums, k) == 8

def test_edge_case_empty_array(solution):
    nums = []
    k = 2
    assert solution.longestOnes(nums, k) == 0

def test_edge_case_single_zero(solution):
    nums = [0]
    k = 0
    assert solution.longestOnes(nums, k) == 0

def test_edge_case_single_one(solution):
    nums = [1]
    k = 0
    assert solution.longestOnes(nums, k) == 1

def test_large_k_than_zeros(solution):
    nums = [0, 1, 0, 1, 0, 1, 1]
    k = 10
    assert solution.longestOnes(nums, k) == 7

def test_k_equals_zero(solution):
    nums = [0, 1, 0, 1, 0, 1, 0, 1]
    k = 0
    assert solution.longestOnes(nums, k) == 1
