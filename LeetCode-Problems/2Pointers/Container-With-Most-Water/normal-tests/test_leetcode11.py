# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import leetcode11 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0(): #FAILED test_leetcode11.py::test_case_0 - TypeError: object of type 'NoneType' has no len()
    solution_0 = module_0.Solution()
    none_type_0 = None
    solution_1 = module_0.Solution()
    bytes_0 = b"H\x87\r"
    int_0 = solution_0.maxArea(bytes_0)
    assert int_0 == 72
    solution_1.maxArea(none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_1(): #FAILED test_leetcode11.py::test_case_1 - TypeError: object of type 'NoneType' has no len()
    solution_0 = module_0.Solution()
    none_type_0 = None
    solution_1 = module_0.Solution()
    bytes_0 = b""
    int_0 = solution_0.maxArea(bytes_0)
    assert int_0 == 0
    solution_1.maxArea(none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2(): #FAILED test_leetcode11.py::test_case_2 - TypeError: object of type 'Solution' has no len()
    solution_0 = module_0.Solution()
    solution_1 = module_0.Solution()
    solution_1.maxArea(solution_0)
