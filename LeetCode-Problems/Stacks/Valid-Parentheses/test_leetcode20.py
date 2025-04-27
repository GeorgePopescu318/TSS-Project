import pytest
from leetcode20 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_valid_parentheses(solution):
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("{[]}") == True
    assert solution.isValid("([{}])") == True

def test_invalid_parentheses(solution):
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("(((") == False
    assert solution.isValid("}") == False
    assert solution.isValid("]") == False
    assert solution.isValid("[") == False

def test_empty_string(solution):
    assert solution.isValid("") == True

def test_single_type_parentheses(solution):
    assert solution.isValid("(((((((((())))))))))") == True
    assert solution.isValid("(((((((((()))))))))))") == False
    assert solution.isValid("(((((((((()))))))))") == False

def test_mixed_characters(solution):#AssertionError: assert False == True
    assert solution.isValid("{[a](b)c}") == True
    assert solution.isValid("{[a](b)c") == False
    assert solution.isValid("a(b)c") == True
    assert solution.isValid("a(b]c") == False
