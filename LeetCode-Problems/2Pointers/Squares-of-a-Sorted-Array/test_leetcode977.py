import pytest
from leetcode977 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_sortedSquares_positive_numbers(solution):
    nums = [1, 2, 3, 4, 5]
    expected = [1, 4, 9, 16, 25]
    assert solution.sortedSquares(nums) == expected

def test_sortedSquares_negative_numbers(solution):
    nums = [-5, -4, -3, -2, -1]
    expected = [1, 4, 9, 16, 25]
    assert solution.sortedSquares(nums) == expected

def test_sortedSquares_mixed_numbers(solution):
    nums = [-4, -1, 0, 3, 10]
    expected = [0, 1, 9, 16, 100]
    assert solution.sortedSquares(nums) == expected

def test_sortedSquares_single_element(solution):
    nums = [0]
    expected = [0]
    assert solution.sortedSquares(nums) == expected

def test_sortedSquares_all_zeros(solution):
    nums = [0, 0, 0, 0]
    expected = [0, 0, 0, 0]
    assert solution.sortedSquares(nums) == expected

def test_sortedSquares_large_numbers(solution):
    nums = [-10000, -5000, 0, 5000, 10000]
    expected = [0, 25000000, 25000000, 100000000, 100000000]
    assert solution.sortedSquares(nums) == expected

def test_sortedSquares_empty_list(solution):
    nums = []
    expected = []
    assert solution.sortedSquares(nums) == expected

def test_sortedSquares_duplicates(solution):
    nums = [-2, -2, 2, 2]
    expected = [4, 4, 4, 4]
    assert solution.sortedSquares(nums) == expected
