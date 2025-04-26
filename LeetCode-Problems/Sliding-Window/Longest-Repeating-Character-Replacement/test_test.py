import pytest
from test import Solution  # Update the import to reflect the correct module path

@pytest.fixture
def solution():
    return Solution()

def test_basic_replacement(solution):
    assert solution.characterReplacement("ABAB", 2) == 4

def test_no_replacement_needed(solution):
    assert solution.characterReplacement("AABABBA", 1) == 4

def test_single_character_long_string(solution):
    assert solution.characterReplacement("A" * 1000, 3) == 1000

def test_empty_string(solution):
    assert solution.characterReplacement("", 2) == 0

def test_no_replacement_possible(solution):
    assert solution.characterReplacement("ABCDE", 0) == 1

def test_full_replacement(solution):
    assert solution.characterReplacement("AAAA", 2) == 4

def test_large_k(solution):
    assert solution.characterReplacement("BAAAB", 10) == 5

def test_all_different_characters(solution):
    assert solution.characterReplacement("ABCDEFG", 3) == 4

def test_minimum_string_length(solution):
    assert solution.characterReplacement("A", 0) == 1

def test_max_k_with_different_characters(solution):
    assert solution.characterReplacement("ABCDE", 5) == 5
