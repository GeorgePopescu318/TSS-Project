import pytest
from leetcode11 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_max_area_typical_case(solution):
    height = [1,8,6,2,5,4,8,3,7]
    assert solution.maxArea(height) == 49

def test_max_area_single_element(solution):
    height = [1]
    assert solution.maxArea(height) == 0

def test_max_area_two_elements(solution):
    height = [1, 2]
    assert solution.maxArea(height) == 1

def test_max_area_increasing_heights(solution):
    height = [1, 2, 3, 4, 5]
    assert solution.maxArea(height) == 6

def test_max_area_decreasing_heights(solution):
    height = [5, 4, 3, 2, 1]
    assert solution.maxArea(height) == 6

def test_max_area_plateau(solution):
    height = [5, 5, 5, 5, 5]
    assert solution.maxArea(height) == 20

def test_max_area_alternating_heights(solution):
    height = [1, 3, 2, 5, 25, 24, 5]
    assert solution.maxArea(height) == 24

def test_max_area_large_input(solution):
    height = [10000] * 1000
    assert solution.maxArea(height) == 9990000

def test_max_area_zero_heights(solution):
    height = [0, 0, 0, 0, 0]
    assert solution.maxArea(height) == 0

def test_max_area_mixed_heights(solution):#assert 12 == 9
    height = [1, 0, 2, 0, 3, 0, 4, 0, 5]
    assert solution.maxArea(height) == 9
