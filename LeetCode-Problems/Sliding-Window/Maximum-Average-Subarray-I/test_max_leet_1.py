import pytest
from max_leet_1 import Solution

def test_find_max_average_positive_numbers():
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    expected_result = 12.75
    assert sol.findMaxAverage(nums, k) == pytest.approx(expected_result, 0.0001)

def test_find_max_average_mixed_numbers():
    sol = Solution()
    nums = [5, -10, 4, 9, -2, 3, 1]
    k = 3
    expected_result = 4.0
    assert sol.findMaxAverage(nums, k) == pytest.approx(expected_result, 0.0001)

def test_find_max_average_all_negative():
    sol = Solution()
    nums = [-3, -7, -9, -4, -2, -6]
    k = 2
    expected_result = -2.5
    assert sol.findMaxAverage(nums, k) == pytest.approx(expected_result, 0.0001)

def test_find_max_average_single_element():
    sol = Solution()
    nums = [7]
    k = 1
    expected_result = 7.0
    assert sol.findMaxAverage(nums, k) == expected_result

def test_find_max_average_large_k():
    sol = Solution()
    nums = [4, 3, 8, 10, 5, 7, 11]
    k = 5
    expected_result = 8.2
    assert sol.findMaxAverage(nums, k) == pytest.approx(expected_result, 0.0001)

def test_find_max_average_identical_elements():
    sol = Solution()
    nums = [2, 2, 2, 2, 2, 2, 2]
    k = 3
    expected_result = 2.0
    assert sol.findMaxAverage(nums, k) == expected_result

def test_find_max_average_large_numbers():
    sol = Solution()
    nums = [3000, 2000, 1000, 0, -1000]
    k = 3
    expected_result = 2000.0
    assert sol.findMaxAverage(nums, k) == pytest.approx(expected_result, 0.0001)

def test_find_max_average_zero():
    sol = Solution()
    nums = [0, 0, 0, 0, 0]
    k = 2
    expected_result = 0.0
    assert sol.findMaxAverage(nums, k) == expected_result

# To run these tests, ensure the class `Solution` is defined in a file named `solution.py` or adjust the import statement accordingly.
