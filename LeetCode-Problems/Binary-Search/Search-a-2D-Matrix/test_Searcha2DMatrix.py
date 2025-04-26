import pytest
from typing import List
from Searcha2DMatrix import searchMatrix  # Import the function from your module

def test_searchMatrix_found_in_single_row():
    matrix = [
        [1, 3, 5, 7]
    ]
    target = 3
    assert searchMatrix(matrix, target) == True

def test_searchMatrix_not_found_in_single_row():
    matrix = [
        [1, 3, 5, 7]
    ]
    target = 4
    assert searchMatrix(matrix, target) == False

def test_searchMatrix_found_in_single_column():
    matrix = [
        [1], 
        [3], 
        [5], 
        [7]
    ]
    target = 5
    assert searchMatrix(matrix, target) == True

def test_searchMatrix_not_found_in_single_column():
    matrix = [
        [1], 
        [3], 
        [5], 
        [7]
    ]
    target = 6
    assert searchMatrix(matrix, target) == False

def test_searchMatrix_found_in_large_matrix():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    target = 15
    assert searchMatrix(matrix, target) == True

def test_searchMatrix_not_found_in_large_matrix():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    target = 12
    assert searchMatrix(matrix, target) == False

def test_searchMatrix_found_at_start():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    target = 1
    assert searchMatrix(matrix, target) == True

def test_searchMatrix_found_at_end():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    target = 6
    assert searchMatrix(matrix, target) == True

def test_searchMatrix_empty_matrix():
    matrix = []
    target = 1
    with pytest.raises(IndexError):  # Assuming the function raises an error on empty input
        searchMatrix(matrix, target)

def test_searchMatrix_found_in_matrix_with_one_element():
    matrix = [[5]]
    target = 5
    assert searchMatrix(matrix, target) == True

def test_searchMatrix_not_found_in_matrix_with_one_element():
    matrix = [[5]]
    target = 3
    assert searchMatrix(matrix, target) == False
