import pytest
from SearchInsertPosition import Solution  # Assuming the code is saved in a file named solution.py

@pytest.fixture
def solution():
    return Solution()

def test_search_insert_exact_match(solution):
    # Test case where the target is present in the list
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2

def test_search_insert_insert_position_middle(solution):
    # Test case where the target should be inserted in the middle
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1

def test_search_insert_insert_position_end(solution):
    # Test case where the target should be inserted at the end
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4

def test_search_insert_insert_position_start(solution):
    # Test case where the target should be inserted at the beginning
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0

def test_search_insert_empty_list(solution):#FAILED: UnboundLocalError: local variable 'm' referenced before assignment
    # Test case where the list is empty
    assert solution.searchInsert([], 5) == 0

def test_search_insert_single_element_equal(solution):
    # Test case where the list has a single element equal to the target
    assert solution.searchInsert([5], 5) == 0

def test_search_insert_single_element_less(solution):
    # Test case where the list has a single element less than the target
    assert solution.searchInsert([2], 3) == 1

def test_search_insert_single_element_more(solution):
    # Test case where the list has a single element more than the target
    assert solution.searchInsert([6], 5) == 0

def test_search_insert_large_list(solution):
    # Test case with a larger list
    nums = list(range(0, 1000000, 2))  # List with even numbers from 0 to 999998
    target = 500001
    assert solution.searchInsert(nums, target) == 250001
