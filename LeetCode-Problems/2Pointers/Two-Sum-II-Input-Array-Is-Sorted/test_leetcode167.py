import pytest
from leetcode167 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_two_sum_example_case(solution):
    numbers = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(numbers, target) == [1, 2]

def test_two_sum_no_solution(solution):
    numbers = [1, 2, 3, 4, 5]
    target = 10
    assert solution.twoSum(numbers, target) is None

def test_two_sum_multiple_solutions(solution):
    numbers = [1, 2, 3, 4, 4, 9]
    target = 8
    assert solution.twoSum(numbers, target) == [4, 5]

def test_two_sum_negative_numbers(solution):#AssertionError: assert [1, 5] == [2, 5]
    numbers = [-3, -1, 0, 2, 4, 5]
    target = 1
    assert solution.twoSum(numbers, target) == [2, 5]

def test_two_sum_identical_numbers(solution):#AssertionError: assert [1, 6] == [1, 2]
    numbers = [1, 1, 1, 1, 1, 1]
    target = 2
    assert solution.twoSum(numbers, target) == [1, 2]

def test_two_sum_large_numbers(solution):
    numbers = [1000000, 1000001, 1000002, 1000003]
    target = 2000003
    assert solution.twoSum(numbers, target) == [1, 4]

def test_two_sum_single_pair(solution):
    numbers = [1, 2]
    target = 3
    assert solution.twoSum(numbers, target) == [1, 2]

def test_two_sum_empty_list(solution):
    numbers = []
    target = 0
    assert solution.twoSum(numbers, target) is None

def test_two_sum_single_element(solution):
    numbers = [1]
    target = 1
    assert solution.twoSum(numbers, target) is None
