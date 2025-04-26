import pytest
from C1P2 import Solution  # Assuming the class is in a file named solution.py

@pytest.fixture
def solution():
    return Solution()

def test_alternating_characters(solution):
    # Test case with words of equal length
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"

def test_word1_longer(solution):
    # Test case where the first word is longer
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"

def test_word2_longer(solution):
    # Test case where the second word is longer
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"

def test_empty_word1(solution):
    # Test case with an empty first word
    assert solution.mergeAlternately("", "pqrs") == "pqrs"

def test_empty_word2(solution):
    # Test case with an empty second word
    assert solution.mergeAlternately("abcd", "") == "abcd"

def test_both_empty(solution):
    # Test case where both words are empty
    assert solution.mergeAlternately("", "") == ""

def test_single_characters(solution):
    # Test case with single character words
    assert solution.mergeAlternately("a", "b") == "ab"

def test_single_and_empty(solution):
    # Test case with one single character word and one empty
    assert solution.mergeAlternately("a", "") == "a"
    assert solution.mergeAlternately("", "b") == "b"

def test_identical_characters(solution):
    # Test case with identical characters
    assert solution.mergeAlternately("aaa", "bbb") == "ababab"
