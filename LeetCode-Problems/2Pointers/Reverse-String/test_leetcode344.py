import pytest
from leetcode344 import Solution  # Assuming the code is in a file named solution.py

@pytest.fixture
def solution():
    return Solution()

def test_reverse_string_even_length(solution):
    s = ['h', 'e', 'l', 'l', 'o']
    solution.reverseString(s)
    assert s == ['o', 'l', 'l', 'e', 'h']

def test_reverse_string_odd_length(solution):
    s = ['a', 'b', 'c', 'd', 'e']
    solution.reverseString(s)
    assert s == ['e', 'd', 'c', 'b', 'a']

def test_reverse_string_single_character(solution):
    s = ['a']
    solution.reverseString(s)
    assert s == ['a']

def test_reverse_string_empty(solution):
    s = []
    solution.reverseString(s)
    assert s == []

def test_reverse_string_palindrome(solution):
    s = ['r', 'a', 'c', 'e', 'c', 'a', 'r']
    solution.reverseString(s)
    assert s == ['r', 'a', 'c', 'e', 'c', 'a', 'r']

def test_reverse_string_identical_characters(solution):
    s = ['x', 'x', 'x', 'x']
    solution.reverseString(s)
    assert s == ['x', 'x', 'x', 'x']

def test_reverse_string_numbers(solution):
    s = ['1', '2', '3', '4', '5']
    solution.reverseString(s)
    assert s == ['5', '4', '3', '2', '1']

def test_reverse_string_mixed_characters(solution):
    s = ['a', '1', 'b', '2', 'c']
    solution.reverseString(s)
    assert s == ['c', '2', 'b', '1', 'a']
