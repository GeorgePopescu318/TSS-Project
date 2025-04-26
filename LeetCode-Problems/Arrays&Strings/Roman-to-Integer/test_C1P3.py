import pytest
from C1P3 import Solution 
# Create a fixture for the Solution class to avoid redundancy
@pytest.fixture
def solution():
    return Solution()

def test_single_roman_numerals(solution):
    assert solution.romanToInt("I") == 1
    assert solution.romanToInt("V") == 5
    assert solution.romanToInt("X") == 10
    assert solution.romanToInt("L") == 50
    assert solution.romanToInt("C") == 100
    assert solution.romanToInt("D") == 500
    assert solution.romanToInt("M") == 1000

def test_compound_roman_numerals(solution):
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("IX") == 9
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("XCIX") == 99
    assert solution.romanToInt("CMXCIV") == 994
    assert solution.romanToInt("MCMXCIV") == 1994

def test_subtractive_notation(solution):
    assert solution.romanToInt("XL") == 40
    assert solution.romanToInt("XC") == 90
    assert solution.romanToInt("CD") == 400
    assert solution.romanToInt("CM") == 900

def test_invalid_inputs(solution):
    with pytest.raises(KeyError):  # Assuming there is no error handling in the original code
        solution.romanToInt("A")
    with pytest.raises(KeyError):
        solution.romanToInt("")
    with pytest.raises(KeyError):
        solution.romanToInt("IIIIIIII")
    with pytest.raises(KeyError):
        solution.romanToInt("VX")
