import pytest
from leetcode125 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_empty_string(solution):
    assert solution.isPalindrome("") == True

def test_single_character(solution):
    assert solution.isPalindrome("a") == True

def test_simple_palindrome(solution):
    assert solution.isPalindrome("racecar") == True

def test_simple_non_palindrome(solution):
    assert solution.isPalindrome("hello") == False

def test_palindrome_with_spaces(solution):
    assert solution.isPalindrome("A man a plan a canal Panama") == True

def test_palindrome_with_mixed_case(solution):
    assert solution.isPalindrome("No 'x' in Nixon") == True

def test_non_palindrome_with_special_characters(solution):
    assert solution.isPalindrome("hello!") == False

def test_palindrome_with_numbers(solution):
    assert solution.isPalindrome("12321") == True

def test_non_palindrome_with_numbers(solution):
    assert solution.isPalindrome("12345") == False

def test_palindrome_with_special_characters(solution):
    assert solution.isPalindrome("Able , was I saw eLba") == True

def test_non_palindrome_with_mixed_case_and_special_characters(solution):
    assert solution.isPalindrome("This is not a palindrome!") == False

def test_palindrome_with_only_special_characters(solution):
    assert solution.isPalindrome("!!!") == True

def test_non_palindrome_with_only_special_characters(solution):
    assert solution.isPalindrome("!@#") == True  # Since no alphanumeric characters, should return True
