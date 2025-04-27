import pytest
from cod import findKthLargest  # Replace 'your_module' with the actual module name

def test_findKthLargest_typical_case():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert findKthLargest(nums, k) == 5

def test_findKthLargest_single_element():
    nums = [1]
    k = 1
    assert findKthLargest(nums, k) == 1

def test_findKthLargest_all_elements_same():
    nums = [2, 2, 2, 2]
    k = 2
    assert findKthLargest(nums, k) == 2

def test_findKthLargest_k_equals_length():
    nums = [3, 1, 2, 4]
    k = 4
    assert findKthLargest(nums, k) == 1

def test_findKthLargest_large_k():
    nums = [7, 10, 4, 3, 20, 15]
    k = 3
    assert findKthLargest(nums, k) == 10

def test_findKthLargest_negative_numbers():
    nums = [-1, -2, -3, -4, -5]
    k = 2
    assert findKthLargest(nums, k) == -2

def test_findKthLargest_mixed_numbers():
    nums = [3, -1, 2, 5, 0, -2]
    k = 4
    assert findKthLargest(nums, k) == 0

def test_findKthLargest_large_input():
    nums = list(range(1000, 0, -1))  # [1000, 999, ..., 1]
    k = 500
    assert findKthLargest(nums, k) == 501
