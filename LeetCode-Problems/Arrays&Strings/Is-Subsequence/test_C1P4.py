import pytest
from C1P4 import Solution  # Replace 'your_module' with the actual module name

def test_is_subsequence_empty_s():
    solution = Solution()
    assert solution.isSubsequence('', 'anything') == True

def test_is_subsequence_empty_t():
    solution = Solution()
    assert solution.isSubsequence('abc', '') == False

def test_is_subsequence_s_longer_than_t():
    solution = Solution()
    assert solution.isSubsequence('moreletters', 'less') == False

def test_is_subsequence_exact_match():
    solution = Solution()
    assert solution.isSubsequence('abc', 'abc') == True

def test_is_subsequence_subsequence_present():
    solution = Solution()
    assert solution.isSubsequence('ace', 'abcde') == True

def test_is_subsequence_subsequence_not_present():
    solution = Solution()
    assert solution.isSubsequence('aec', 'abcde') == False

def test_is_subsequence_non_consecutive_match():
    solution = Solution()
    assert solution.isSubsequence('ac', 'abbc') == True

def test_is_subsequence_no_match():
    solution = Solution()
    assert solution.isSubsequence('g', 'abcde') == False

def test_is_subsequence_single_char_matches():
    solution = Solution()
    assert solution.isSubsequence('a', 'a') == True

def test_is_subsequence_first_char_mismatch():
    solution = Solution()
    assert solution.isSubsequence('b', 'a') == False

def test_is_subsequence_middle_subsequence():
    solution = Solution()
    assert solution.isSubsequence('bd', 'abcde') == True
