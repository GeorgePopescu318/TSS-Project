import pytest
from cod import exist
def test_exist_single_cell_match():
    board = [['A']]
    word = "A"
    assert exist(board, word) == True

def test_exist_single_cell_no_match():
    board = [['A']]
    word = "B"
    assert exist(board, word) == False

def test_exist_horizontal_match():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    assert exist(board, word) == True

def test_exist_vertical_match():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "SEE"
    assert exist(board, word) == True

def test_exist_no_match():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCB"
    assert exist(board, word) == False

def test_exist_diagonal_no_match():# AssertionError: assert True == False
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABF"
    assert exist(board, word) == False

def test_exist_full_board_match():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCESEEDASFC"
    assert exist(board, word) == True

def test_exist_empty_word():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = ""
    assert exist(board, word) == True

def test_exist_empty_board():
    board = [[]]
    word = "A"
    assert exist(board, word) == False

def test_exist_large_board():#AssertionError: assert False == True
    board = [
        ['A', 'B', 'C', 'E', 'F', 'G'],
        ['H', 'I', 'J', 'K', 'L', 'M'],
        ['N', 'O', 'P', 'Q', 'R', 'S'],
        ['T', 'U', 'V', 'W', 'X', 'Y'],
        ['Z', 'A', 'B', 'C', 'D', 'E']
    ]
    word = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    assert exist(board, word) == True
