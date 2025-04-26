import pytest
from brute_force import Solution  # Assuming the code is in a file named solution.py

@pytest.fixture
def solution():
    return Solution()

def test_find_max_average_basic_case(solution):
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    expected = 12.75
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_single_element_repeated(solution):
    nums = [5, 5, 5, 5, 5]
    k = 2
    expected = 5.0
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_negative_numbers(solution):
    nums = [-1, -2, -3, -4]
    k = 2
    expected = -1.5
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_large_k(solution):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    expected = 8.0
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_k_equals_length_of_nums(solution):
    nums = [7, 8, 9]
    k = 3
    expected = 8.0
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_small_k(solution):
    nums = [4, 2, 0, 3, 5]
    k = 1
    expected = 5.0
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_edge_case_empty(solution):
    # Although the problem statement likely assumes k <= len(nums), it's safe to check for this
    nums = []
    k = 0
    expected = 0.0  # Or handle this case with an exception
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_edge_case_zero_elements(solution):
    nums = [0, 0, 0, 0, 0]
    k = 3
    expected = 0.0
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_with_floats(solution):
    nums = [2.5, 3.5, 4.5, 5.5]
    k = 2
    expected = 5.0
    assert solution.findMaxAverage(nums, k) == expected

def test_find_max_average_all_identical_elements(solution):
    nums = [4, 4, 4, 4, 4]
    k = 3
    expected = 4.0
    assert solution.findMaxAverage(nums, k) == expected
