# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import cod as module_0

#https://github.com/gahogg/Leetcode-Solutions/blob/main/Last%20Stone%20Weight%20-%20Leetcode%201046/Last%20Stone%20Weight%20-%20Leetcode%201046.py
#Optimal solution
# @pytest.mark.xfail(strict=True)
def test_case_0(): #FAILED test_cod.py::test_case_0 - TypeError: object of type 'complex' has no len()  
    complex_0 = 2770.8191 + 138.86384j
    module_0.lastStoneWeight(complex_0)
