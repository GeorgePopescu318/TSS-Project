# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import cod as module_0
#https://github.com/gahogg/Leetcode-Solutions/blob/main/Letter%20Combinations%20of%20a%20Phone%20Number%20-%20Leetcode%2017/Letter%20Combinations%20of%20a%20Phone%20Number%20-%20Leetcode%2017.py

# @pytest.mark.xfail(strict=True)
def test_case_0(): #XFAIL FAILED test_cod.py::test_case_0 - KeyError: '"'
    str_0 = '4"#O4Z_H$d8,ZQL:P~Uk'
    module_0.letterCombinations(str_0)


def test_case_1():#PASSED 
    list_0 = []
    list_1 = module_0.letterCombinations(list_0)


# @pytest.mark.xfail(strict=True)
def test_case_2():# XFAIL FAILED test_cod.py::test_case_2 - KeyError: 'c'
    str_0 = ""
    list_0 = module_0.letterCombinations(str_0)
    str_1 = "8ca0&XeAi9"
    module_0.letterCombinations(str_1)


# @pytest.mark.xfail(strict=True)
def test_case_3():# XFAIL FAILED test_cod.py::test_case_3 - KeyError: 't'
    str_0 = "8"
    list_0 = module_0.letterCombinations(str_0)
    list_1 = module_0.letterCombinations(str_0)
    module_0.letterCombinations(list_1)
