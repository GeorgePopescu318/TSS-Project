# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import tests.C1P2 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "vu7FG96{"
    bool_0 = False
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    solution_0 = module_0.Solution()
    solution_0.mergeAlternately(str_0, tuple_0)


def test_case_1():
    list_0 = []
    solution_0 = module_0.Solution(*list_0)
    str_0 = solution_0.mergeAlternately(list_0, list_0)
    assert str_0 == ""
    str_1 = solution_0.mergeAlternately(str_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    solution_0 = module_0.Solution(*list_0)
    str_0 = "hVqRRrW g9UyF2Raf"
    str_1 = solution_0.mergeAlternately(str_0, str_0)
    assert str_1 == "hhVVqqRRRRrrWW  gg99UUyyFF22RRaaff"
    none_type_0 = None
    module_0.Solution(*none_type_0)


def test_case_3():
    list_0 = []
    solution_0 = module_0.Solution(*list_0)


def test_case_4():
    str_0 = "u7"
    str_1 = ")Ap"
    solution_0 = module_0.Solution()
    str_2 = solution_0.mergeAlternately(str_0, str_1)
    assert str_2 == "u)7Ap"
    list_0 = []
    solution_1 = module_0.Solution(*list_0)
    solution_2 = module_0.Solution()
    str_3 = solution_2.mergeAlternately(str_0, str_0)
    assert str_3 == "uu77"


@pytest.mark.xfail(strict=True)
def test_case_5():
    dict_0 = {}
    str_0 = "f"
    solution_0 = module_0.Solution(*dict_0)
    str_1 = solution_0.mergeAlternately(dict_0, str_0)
    assert str_1 == "f"
    solution_1 = module_0.Solution()
    solution_2 = module_0.Solution(**dict_0)
    str_2 = '?a3qmj.Lr\nX"pg0['
    str_3 = ""
    str_4 = solution_2.mergeAlternately(str_2, str_3)
    assert str_4 == '?a3qmj.Lr\nX"pg0['
    str_5 = "Bgg"
    dict_1 = {str_3: str_3, str_3: str_3, str_5: str_3, str_5: str_5}
    module_0.Solution(**dict_1)
