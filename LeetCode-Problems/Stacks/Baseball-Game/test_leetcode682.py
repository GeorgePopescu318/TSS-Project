import pytest
from leetcode682 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_calPoints_example1(solution):
    operations = ["5", "2", "C", "D", "+"]
    assert solution.calPoints(operations) == 30

def test_calPoints_example2(solution):
    operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    assert solution.calPoints(operations) == 27

def test_calPoints_single_number(solution):
    operations = ["10"]
    assert solution.calPoints(operations) == 10

def test_calPoints_all_operations(solution): #AssertionError: assert 105 == 37
    operations = ["5", "2", "C", "D", "+", "3", "C", "D", "+"]
    assert solution.calPoints(operations) == 37

def test_calPoints_empty_operations(solution):
    operations = []
    assert solution.calPoints(operations) == 0

def test_calPoints_only_cancellations(solution):#IndexError: pop from empty list
    operations = ["5", "C", "C", "C"]
    assert solution.calPoints(operations) == 0

def test_calPoints_only_doublings(solution):#AssertionError: assert 75 == 40
    operations = ["5", "D", "D", "D"]
    assert solution.calPoints(operations) == 40

def test_calPoints_only_additions(solution):#AssertionError: assert 23 == 19
    operations = ["5", "2", "+", "+"]
    assert solution.calPoints(operations) == 19

def test_calPoints_mixed_operations(solution):#AssertionError: assert 36 == 19
    operations = ["1", "2", "+", "D", "C", "5", "D", "+"]
    assert solution.calPoints(operations) == 19
