import pytest
from test import Solution

@pytest.fixture
def solution():
    return Solution()

def test_min_subarray_len_example1(solution):
    assert solution.minSubArrayLen(7, [2,3,1,2,4,3]) == 2

def test_min_subarray_len_example2(solution):
    assert solution.minSubArrayLen(15, [1,2,3,4,5]) == 5

def test_min_subarray_len_no_subarray(solution):
    assert solution.minSubArrayLen(100, [1,2,3,4,5]) == 0

def test_min_subarray_len_exact_match(solution): # assert 2 == 1 where 2 = minSubArrayLen(5, [2, 3, 4, 1, 1, 1, ...])
    assert solution.minSubArrayLen(5, [2,3,4,1,1,1,1]) == 1

def test_min_subarray_len_larger_target(solution): # assert 0 == 3 where 0 = minSubArrayLen(20, [2, 3, 1, 2, 8])
    assert solution.minSubArrayLen(20, [2,3,1,2,8]) == 3

def test_min_subarray_len_repeated_elements(solution):
    assert solution.minSubArrayLen(10, [5,5,5,5]) == 2

def test_min_subarray_len_single_element(solution):
    assert solution.minSubArrayLen(10, [10]) == 1

def test_min_subarray_len_no_elements(solution):
    assert solution.minSubArrayLen(3, []) == 0

def test_min_subarray_len_all_elements_identical(solution):
    assert solution.minSubArrayLen(4, [1,1,1,1,1]) == 4

def test_min_subarray_len_all_elements_identical_larger_target(solution):
    assert solution.minSubArrayLen(14, [1,1,1,1]) == 0
