import pytest
from cod import permute
def test_permute_empty_list():
    assert permute([]) == [[]], "Failed on empty list"

def test_permute_single_element():
    assert permute([1]) == [[1]], "Failed on single element list"

def test_permute_two_elements():
    result = permute([1, 2])
    expected = [[1, 2], [2, 1]]
    assert sorted(result) == sorted(expected), "Failed on two elements list"

def test_permute_three_elements():
    result = permute([1, 2, 3])
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    assert sorted(result) == sorted(expected), "Failed on three elements list"

def test_permute_with_duplicates():
    result = permute([1, 1, 2])#  AssertionError: Failed on list with duplicates assert [] == [[1, 1, 2], [...1], [2, 1, 1]]
    expected = [
        [1, 2, 1],
        [2, 1, 1],
        [1, 1, 2]
    ]
    assert sorted(result) == sorted(expected), "Failed on list with duplicates"

def test_permute_large_list():
    result = permute([1, 2, 3, 4])
    expected_length = 24  # 4! = 24 permutations
    assert len(result) == expected_length, "Failed on large list"

# Run the tests
if __name__ == "__main__":
    pytest.main()
