import pytest
from test import Solution  # Replace 'your_module' with the actual module name

@pytest.fixture
def solution():
    return Solution()

def test_check_inclusion_exact_match(solution):
    assert solution.checkInclusion("ab", "eidbaooo") is True

def test_check_inclusion_no_match(solution):
    assert solution.checkInclusion("ab", "eidboaoo") is False

def test_check_inclusion_empty_s1(solution):
    assert solution.checkInclusion("", "anything") is True

def test_check_inclusion_empty_s2(solution):
    assert solution.checkInclusion("a", "") is False

def test_check_inclusion_s1_longer_than_s2(solution):
    assert solution.checkInclusion("abcd", "abc") is False

def test_check_inclusion_identical_strings(solution):
    assert solution.checkInclusion("abc", "abc") is True

def test_check_inclusion_permutation_exists(solution):
    assert solution.checkInclusion("adc", "dca") is True

def test_check_inclusion_large_input_no_match(solution):
    s1 = "a" * 1000 + "b"
    s2 = "a" * 1000
    assert solution.checkInclusion(s1, s2) is False

def test_check_inclusion_single_character(solution):
    assert solution.checkInclusion("a", "a") is True
    assert solution.checkInclusion("a", "b") is False

def test_check_inclusion_all_distinct_characters(solution):
    assert solution.checkInclusion("abc", "def") is False

