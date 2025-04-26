import pytest
from collections import Counter
from C2P4 import Solution  # Replace 'your_module' with the actual module name

@pytest.fixture
def solution():
    return Solution()

def test_identical_strings(solution):
    assert solution.isAnagram("a", "a") == True

def test_anagrams(solution):
    assert solution.isAnagram("listen", "silent") == True
    assert solution.isAnagram("triangle", "integral") == True
    assert solution.isAnagram("anagram", "nagaram") == True

def test_non_anagrams(solution):
    assert solution.isAnagram("hello", "world") == False
    assert solution.isAnagram("rat", "car") == False

def test_different_lengths(solution):
    assert solution.isAnagram("a", "ab") == False
    assert solution.isAnagram("abc", "abcd") == False

def test_empty_strings(solution):
    assert solution.isAnagram("", "") == True
    assert solution.isAnagram("a", "") == False
    assert solution.isAnagram("", "a") == False

def test_special_characters(solution):
    assert solution.isAnagram("!@#", "#@!") == True
    assert solution.isAnagram("123", "321") == True
    assert solution.isAnagram("123", "1234") == False

def test_unicode_characters(solution):
    assert solution.isAnagram("���", "���") == True
    assert solution.isAnagram("���", "���") == True
