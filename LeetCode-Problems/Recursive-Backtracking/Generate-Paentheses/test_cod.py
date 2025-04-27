import pytest
from cod import generateParenthesis  # Replace 'your_module' with the actual module name

def test_generateParenthesis_zero():
    # Test case for n = 0
    assert generateParenthesis(0) == []#AssertionError: assert [''] == []

def test_generateParenthesis_one():
    # Test case for n = 1
    assert generateParenthesis(1) == ["()"]

def test_generateParenthesis_two():
    # Test case for n = 2
    assert sorted(generateParenthesis(2)) == sorted(["(())", "()()"])

def test_generateParenthesis_three():
    # Test case for n = 3
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(generateParenthesis(3)) == sorted(expected)

def test_generateParenthesis_four():
    # Test case for n = 4
    expected = [
        "(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
        "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
        "()(()())", "()(())()", "()()(())", "()()()()"
    ]
    assert sorted(generateParenthesis(4)) == sorted(expected)

def test_generateParenthesis_invalid_input():
    # Test case for invalid input (negative number)
    with pytest.raises(ValueError):#Failed: DID NOT RAISE <class 'ValueError'>
        generateParenthesis(-1)

def test_generateParenthesis_large_input():
    # Test case for a larger input to check performance or timeout issues
    # This test might be skipped in a real-world scenario due to performance constraints
    result = generateParenthesis(5)
    assert len(result) == 42  # There are 42 valid combinations for n = 5

# Note: The invalid input test assumes that the function should raise a ValueError for negative inputs.
# If the function does not currently handle such cases, you might need to modify the function to handle them.
