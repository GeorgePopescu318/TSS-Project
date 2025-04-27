import pytest
from cod import subsets
def test_subsets_empty():
    assert subsets([]) == [[]]

def test_subsets_single_element():
    assert subsets([1]) == [[], [1]]

def test_subsets_two_elements():
    result = subsets([1, 2])
    expected = [[], [2], [1], [1, 2]]
    assert sorted(result) == sorted(expected)

def test_subsets_three_elements():
    result = subsets([1, 2, 3])
    expected = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
    assert sorted(result) == sorted(expected)

def test_subsets_duplicates():#AssertionError: assert [[], [1], [1,... 2], [2], ...] == [[], [1], [1,..., [2], [2, 2]]
    result = subsets([1, 2, 2])
    expected = [[], [2], [2, 2], [1], [1, 2], [1, 2, 2]]
    assert sorted(result) == sorted(expected)

def test_subsets_large_input():
    nums = [1, 2, 3, 4]
    result = subsets(nums)
    expected_length = 2 ** len(nums)  # 2^n subsets
    assert len(result) == expected_length

def test_subsets_negative_numbers():
    result = subsets([-1, 0, 1])
    expected = [[], [1], [0], [0, 1], [-1], [-1, 1], [-1, 0], [-1, 0, 1]]
    assert sorted(result) == sorted(expected)
