import pytest
from C2P2 import Solution

def test_contains_no_duplicates():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    assert not solution.containsDuplicate(nums), "Failed: List contains no duplicates"

def test_contains_duplicates_at_beginning():
    solution = Solution()
    nums = [1, 1, 2, 3, 4, 5]
    assert solution.containsDuplicate(nums), "Failed: List contains duplicates at the beginning"

def test_contains_duplicates_at_end():
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 5]
    assert solution.containsDuplicate(nums), "Failed: List contains duplicates at the end"

def test_contains_duplicates_in_middle():
    solution = Solution()
    nums = [1, 2, 3, 2, 4, 5]
    assert solution.containsDuplicate(nums), "Failed: List contains duplicates in the middle"

def test_all_same_element():
    solution = Solution()
    nums = [1, 1, 1, 1, 1]
    assert solution.containsDuplicate(nums), "Failed: List with all elements the same"

def test_empty_list():
    solution = Solution()
    nums = []
    assert not solution.containsDuplicate(nums), "Failed: Empty list should return False"

def test_single_element_list():
    solution = Solution()
    nums = [1]
    assert not solution.containsDuplicate(nums), "Failed: Single element list should return False"

def test_large_input_with_duplicates():
    solution = Solution()
    nums = list(range(10000)) + [9999]
    assert solution.containsDuplicate(nums), "Failed: Large list with duplicates"

def test_large_input_without_duplicates():
    solution = Solution()
    nums = list(range(10000))
    assert not solution.containsDuplicate(nums), "Failed: Large list without duplicates"
