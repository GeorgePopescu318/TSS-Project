# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import SearchInsertPosition as module_0


def test_case_0():#PASSED
    bytes_0 = b"\xf8\x93"
    bool_0 = True
    solution_0 = module_0.Solution()
    int_0 = solution_0.searchInsert(bytes_0, bool_0)
    assert int_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_1():#FAILED: local variable 'm' referenced before assignment
    list_0 = []
    bool_0 = True
    list_1 = []
    solution_0 = module_0.Solution(*list_0)
    solution_1 = module_0.Solution(*list_1)
    solution_1.searchInsert(list_0, bool_0)


def test_case_2():#PASSED
    solution_0 = module_0.Solution()


def test_case_3():#PASSED
    bool_0 = False
    list_0 = [bool_0]
    bool_1 = False
    solution_0 = module_0.Solution()
    int_0 = solution_0.searchInsert(list_0, bool_1)
    assert int_0 == 0


def test_case_4():#PASSED
    solution_0 = module_0.Solution()
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    bool_1 = False
    int_0 = solution_0.searchInsert(list_0, bool_1)
    assert int_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_5():#FAILED: object of type 'Solution' has no len()
    solution_0 = module_0.Solution()
    bool_0 = False
    list_0 = [bool_0, bool_0]
    int_0 = solution_0.searchInsert(list_0, bool_0)
    assert int_0 == 0
    solution_1 = module_0.Solution()
    int_1 = 1820
    int_2 = solution_0.searchInsert(list_0, int_1)
    assert int_2 == 2
    int_3 = solution_0.searchInsert(list_0, int_1)
    assert int_3 == 2
    solution_1.searchInsert(solution_1, int_1)
