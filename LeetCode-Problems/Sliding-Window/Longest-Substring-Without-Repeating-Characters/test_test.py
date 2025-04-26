import pytest
from test import Solution, length_of_longest_substring

@pytest.mark.parametrize("s, expected", [
    # Test with an empty string
    ("", 0),
    # Test with a string of unique characters
    ("abcdef", 6),
    # Test with a string with all identical characters
    ("aaaaaa", 1),
    # Test with no repeating characters
    ("abcabcbb", 3),
    # Test with repeating characters
    ("bbbbb", 1),
    # Test with multiple repeating characters scattered
    ("pwwkew", 3),
    # Test with unicode characters
    ("a€ξε€ተξa", 5),
    # Test with only whitespace
    ("    ", 1),
    # Test edge case with two unique characters repeating
    ("abababababab", 2),
    # Test with a long string without any repeating characters
    ("abcdefghijklmnopqrstuvwxyz", 26),
])
def test_length_of_longest_substring(s, expected):
    assert length_of_longest_substring(s) == expected

@pytest.mark.parametrize("s, expected", [
    # Test with an empty string
    ("", 0),
    # Test with a string of unique characters
    ("abcdef", 6),
    # Test with a string with all identical characters
    ("aaaaaa", 1),
    # Test with no repeating characters
    ("abcabcbb", 3),
    # Test with repeating characters
    ("bbbbb", 1),
    # Test with multiple repeating characters scattered
    ("pwwkew", 3),
    # Test with unicode characters
    ("a€ξε€ተξa", 5),
    # Test with only whitespace
    ("    ", 1),
    # Test edge case with two unique characters repeating
    ("abababababab", 2),
    # Test with a long string without any repeating characters
    ("abcdefghijklmnopqrstuvwxyz", 26),
])
def test_solution_length_of_longest_substring(s, expected):
    sol = Solution()
    assert sol.lengthOfLongestSubstring(s) == expected
