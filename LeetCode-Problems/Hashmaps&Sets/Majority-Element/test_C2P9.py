import pytest
from C2P9 import Solution  # Assuming the class is saved in a file named solution.py

def test_majority_element_basic():
    sol = Solution()
    assert sol.majorityElement([3, 2, 3]) == 3, "Test case [3, 2, 3] failed"

def test_majority_element_single_element():
    sol = Solution()
    assert sol.majorityElement([1]) == 1, "Test case [1] failed"

def test_majority_element_multiple_same_elements():
    sol = Solution()
    assert sol.majorityElement([2, 2, 1, 1, 2]) == 2, "Test case [2, 2, 1, 1, 2] failed"

def test_majority_element_large_input():
    sol = Solution()
    assert sol.majorityElement([1, 2, 2, 2, 3, 2, 2, 4, 5, 2, 2, 6, 2, 2]) == 2, "Large input test case failed"

def test_majority_element_no_majority():
    sol = Solution()
    assert sol.majorityElement([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1]) == 1, "Test case with no clear majority failed"

def test_majority_element_negative_numbers():
    sol = Solution()
    assert sol.majorityElement([-1, -1, -1, 2, 2, 2, -1, -1]) == -1, "Test case with negative numbers failed"

def test_majority_element_zeros():
    sol = Solution()
    assert sol.majorityElement([0, 0, 0, 1]) == 0, "Test case with zeros failed"

def test_majority_element_all_same_elements():
    sol = Solution()
    assert sol.majorityElement([7, 7, 7, 7, 7]) == 7, "Test case with all same elements failed"

def test_majority_element_empty_list():
    sol = Solution()
    assert sol.majorityElement([]) == -1, "Test case with empty list failed"

if __name__ == "__main__":
    pytest.main()
