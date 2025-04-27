import pytest
from cod import letterCombinations
def test_letter_combinations_empty_input():
    assert letterCombinations("") == []

def test_letter_combinations_single_digit():
    assert set(letterCombinations("2")) == {"a", "b", "c"}
    assert set(letterCombinations("3")) == {"d", "e", "f"}

def test_letter_combinations_two_digits():
    result = letterCombinations("23")
    expected = {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
    assert set(result) == expected

def test_letter_combinations_multiple_digits():
    result = letterCombinations("234")
    expected = {
        "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
        "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
        "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
    }
    assert set(result) == expected

def test_letter_combinations_with_7_and_9():
    result = letterCombinations("79")
    expected = {
        "pw", "px", "py", "pz",
        "qw", "qx", "qy", "qz",
        "rw", "rx", "ry", "rz",
        "sw", "sx", "sy", "sz"
    }
    assert set(result) == expected

def test_letter_combinations_all_digits():
    result = letterCombinations("23456789")
    # Due to the large number of combinations, we will only check the length
    expected_length = 3 * 3 * 3 * 3 * 4 * 3 * 3 * 4  # 3^5 * 4^3
    assert len(result) == expected_length

def test_letter_combinations_invalid_digit():
    with pytest.raises(KeyError):
        letterCombinations("1")

def test_letter_combinations_mixed_valid_invalid():
    with pytest.raises(KeyError):
        letterCombinations("23a")
