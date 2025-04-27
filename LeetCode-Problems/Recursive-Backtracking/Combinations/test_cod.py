import pytest
from cod import combine
def test_combine_basic():
    # Basic test case
    assert combine(4, 2) == [[2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3]]

def test_combine_k_equals_n():
    # Test case where k equals n
    assert combine(3, 3) == [[3, 2, 1]]

def test_combine_k_greater_than_n():
    # Test case where k is greater than n, should return an empty list
    assert combine(2, 3) == []#AssertionError: assert [[2, 1, 0]] == []

def test_combine_k_zero():
    # Test case where k is zero, should return a list with an empty list
    assert combine(3, 0) == [[]]

def test_combine_n_zero():
    # Test case where n is zero, should return an empty list
    assert combine(0, 2) == [] #AssertionError: assert [[0, -1]] == []

def test_combine_n_and_k_zero():
    # Test case where both n and k are zero, should return a list with an empty list
    assert combine(0, 0) == [[]] 

def test_combine_single_combination():
    # Test case where there is only one possible combination
    assert combine(1, 1) == [[1]]

def test_combine_large_n_small_k():
    # Test case with a larger n and small k
    assert combine(5, 1) == [[1], [2], [3], [4], [5]]

def test_combine_large_k():
    # Test case with a larger k
    assert combine(5, 5) == [[5, 4, 3, 2, 1]]

# Run the tests
if __name__ == "__main__":
    pytest.main()
