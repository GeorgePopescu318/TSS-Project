import pytest
from typing import List
from BinarySearch import search  # import the function from your module

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 2, 3, 4, 5], 3, 2),  # target in the middle
    ([1, 2, 3, 4, 5], 1, 0),  # target is the first element
    ([1, 2, 3, 4, 5], 5, 4),  # target is the last element
    ([1, 2, 3, 4, 5], 6, -1), # target not in list
    ([5, 6, 7, 8, 9], 5, 0),  # target is the first element
    ([5, 6, 7, 8, 9], 9, 4),  # target is the last element
    ([], 3, -1),              # searching in an empty list
    ([1], 1, 0),              # single element list where element is target
    ([1], 2, -1),             # single element list where element is not target
    ([1, 3, 5, 7, 9, 11], 8, -1),  # target not in list
    ([1, 3, 5, 7, 9, 11], -1, -1)  # target less than the smallest element
])
def test_search(nums: List[int], target: int, expected: int):
    assert search(nums, target) == expected
