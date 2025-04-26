import pytest
from typing import List
from C1P6 import Solution  # Assuming the solution code is in a file named solution.py

@pytest.mark.parametrize("strs, expected", [
    # Test cases with common prefixes
    (["flower", "flow", "flight"], "fl"),
    (["dog", "dodge", "dodgeball"], "do"),
    # Test case with identical strings
    (["test", "test", "test"], "test"),
    # Test case with a single string in the list
    (["alone"], "alone"),
    # Test case with no common prefix
    (["cat", "dog", "bird"], ""),
    # Test case with an empty string in the list
    (["", "b", "c"], ""),
    # Test case with an empty list
    ([], ""),
    # Test case with varied lengths, where common prefix is shorter
    (["intro", "in", "introspection"], "in"),
    # Test case with all strings being empty
    (["", "", ""], ""),
    # Test case with strings consisting of a single character
    (["a", "a", "a"], "a"),
    # Test case with a mix of single and multiple character strings
    (["a", "abc", "ab"], "a"),
])
def test_longest_common_prefix(strs: List[str], expected: str):
    solution = Solution()
    assert solution.longestCommonPrefix(strs) == expected
