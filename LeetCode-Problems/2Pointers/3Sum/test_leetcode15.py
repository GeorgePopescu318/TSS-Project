import pytest
from leetcode15 import Solution
@pytest.fixture
def solution():
    return Solution()

def test_three_sum_empty_list(solution):
    assert solution.threeSum([]) == set()

def test_three_sum_no_triplets(solution):
    assert solution.threeSum([1, 2, 3, 4, 5]) == set()

def test_three_sum_single_triplet(solution):
    assert solution.threeSum([-1, 0, 1, 2]) == {(-1, 0, 1)}

def test_three_sum_multiple_triplets(solution):
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    expected = {(-1, -1, 2), (-1, 0, 1)}
    assert result == expected

def test_three_sum_with_duplicates(solution):
    result = solution.threeSum([-1, -1, 2, 2, 0, 0, 1, 1])
    expected = {(-1, -1, 2), (-1, 0, 1)}
    assert result == expected

def test_three_sum_all_zeros(solution):
    assert solution.threeSum([0, 0, 0, 0]) == {(0, 0, 0)}

def test_three_sum_large_numbers(solution):
    result = solution.threeSum([-1000000, 500000, 500000, 1000000])
    expected = {(-1000000, 500000, 500000)}
    assert result == expected

def test_three_sum_mixed_numbers(solution):
    result = solution.threeSum([-2, 0, 1, 1, 2])
    expected = {(-2, 0, 2), (-2, 1, 1)}
    assert result == expected
