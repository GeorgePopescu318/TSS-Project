import pytest
from C2P1 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_no_jewels_no_stones(solution):
    assert solution.numJewelsInStones("", "") == 0

def test_no_jewels_with_stones(solution):
    assert solution.numJewelsInStones("", "abc") == 0

def test_jewels_no_stones(solution):
    assert solution.numJewelsInStones("abc", "") == 0

def test_all_stones_are_jewels(solution):
    assert solution.numJewelsInStones("abc", "abcabc") == 6

def test_some_stones_are_jewels(solution):
    assert solution.numJewelsInStones("a", "abcabc") == 2

def test_all_jewels_are_stones(solution):
    assert solution.numJewelsInStones("abc", "cba") == 3

def test_no_stones_are_jewels(solution):
    assert solution.numJewelsInStones("xyz", "abc") == 0

def test_stones_contain_duplicates(solution):
    assert solution.numJewelsInStones("abc", "aabbcc") == 6

def test_jewels_contain_duplicates(solution):
    assert solution.numJewelsInStones("aabb", "ab") == 2

def test_large_input(solution):
    assert solution.numJewelsInStones("a" * 1000, "a" * 1000) == 1000
