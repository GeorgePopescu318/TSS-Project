import pytest
from C2P3 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_can_construct_same_characters(solution):
    assert solution.canConstruct("a", "a") == True

def test_can_construct_different_characters(solution):
    assert solution.canConstruct("a", "b") == False

def test_can_construct_insufficient_frequency(solution):
    assert solution.canConstruct("aa", "ab") == False

def test_can_construct_sufficient_frequency(solution):
    assert solution.canConstruct("aa", "aab") == True

def test_can_construct_empty_ransom(solution):
    assert solution.canConstruct("", "a") == True

def test_can_construct_empty_magazine(solution):
    assert solution.canConstruct("a", "") == False

def test_can_construct_both_empty(solution):
    assert solution.canConstruct("", "") == True

def test_can_construct_longer_ransom(solution):
    assert solution.canConstruct("longerstring", "longersstringbutnotexact") == True

def test_can_construct_ransom_larger_than_magazine(solution):
    assert solution.canConstruct("abcd", "abc") == False

def test_can_construct_repeated_characters(solution):
    assert solution.canConstruct("aaabbb", "aaabbbccc") == True

def test_can_construct_magazine_smaller_case_insensitive(solution):
    assert solution.canConstruct("AA", "aa") == False  # Case sensitivity implied

def test_can_construct_miscellaneous_chars(solution):
    assert solution.canConstruct("123", "321") == True
