# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import tests.C1P6 as module_0


def test_case_0():
    str_0 = "xihGIc-MMZI^LE"
    list_0 = [str_0, str_0]
    solution_0 = module_0.Solution()
    str_1 = solution_0.longestCommonPrefix(list_0)
    assert str_1 == "xihGIc-MMZI^LE"


def test_case_1():
    solution_0 = module_0.Solution()


def test_case_2():
    str_0 = "|jZ3"
    str_1 = "\"ZdTL,'(-k=z*[y:qh\t"
    list_0 = [str_0, str_0, str_1, str_0]
    list_1 = []
    solution_0 = module_0.Solution(*list_1)
    str_2 = solution_0.longestCommonPrefix(list_0)
    assert str_2 == ""
    solution_1 = module_0.Solution()


def test_case_3():
    str_0 = "|jZ3"
    str_1 = ""
    list_0 = [str_0, str_0, str_1, str_0]
    list_1 = []
    solution_0 = module_0.Solution(*list_1)
    str_2 = solution_0.longestCommonPrefix(list_0)
    assert str_2 == ""
    solution_1 = module_0.Solution()
