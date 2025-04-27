import pytest
from math import isclose # nu e folosit
from leetcode150 import Solution
# Assuming the Solution class is already imported
solution = Solution()

def test_single_number():
    assert solution.evalRPN(["3"]) == 3

def test_simple_addition():
    assert solution.evalRPN(["2", "3", "+"]) == 5

def test_simple_subtraction():
    assert solution.evalRPN(["5", "3", "-"]) == 2

def test_simple_multiplication():
    assert solution.evalRPN(["2", "3", "*"]) == 6

def test_simple_division():
    assert solution.evalRPN(["6", "3", "/"]) == 2

def test_division_with_negative_result():
    assert solution.evalRPN(["7", "-3", "/"]) == -2

def test_division_with_positive_result():
    assert solution.evalRPN(["-7", "3", "/"]) == -2

def test_complex_expression():
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9

def test_expression_with_all_operations():
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6

def test_expression_with_negative_numbers():
    assert solution.evalRPN(["-2", "-3", "*", "4", "+"]) == 10

def test_expression_with_mixed_operations():#AssertionError: assert 52 == 22
    assert solution.evalRPN(["10", "6", "9", "3", "/", "-", "*", "17", "+", "5", "+"]) == 22

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        solution.evalRPN(["4", "0", "/"])

def test_large_numbers():
    assert solution.evalRPN(["100000", "100000", "*"]) == 10000000000

def test_float_division():#AssertionError: assert -3 == -4
    # This test checks if the division is correctly floored or ceiled
    assert solution.evalRPN(["10", "3", "/"]) == 3
    assert solution.evalRPN(["-10", "3", "/"]) == -4
