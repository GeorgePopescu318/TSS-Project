# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import tests.C1P4 as module_0


def test_case_0():
    str_0 = "gq;"
    solution_0 = module_0.Solution()
    bool_0 = solution_0.isSubsequence(str_0, str_0)
    assert bool_0 is True


def test_case_1():
    solution_0 = module_0.Solution()


def test_case_2():
    solution_0 = module_0.Solution()
    str_0 = "*]v$N4iq>T|"
    list_0 = []
    solution_1 = module_0.Solution(*list_0)
    solution_2 = module_0.Solution(*list_0)
    bool_0 = solution_2.isSubsequence(str_0, str_0)
    assert bool_0 is True
    str_1 = "RI~J|yq#\ra#|Fu&\\F"
    bool_1 = solution_0.isSubsequence(str_1, str_0)
    assert bool_1 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "goM=jbyOX\x0ctkc"
    solution_0 = module_0.Solution()
    bool_0 = solution_0.isSubsequence(str_0, str_0)
    assert bool_0 is True
    str_1 = "~UJW"
    solution_1 = module_0.Solution()
    bool_1 = solution_1.isSubsequence(str_1, str_1)
    assert bool_1 is True
    none_type_0 = None
    str_2 = "l4g+("
    str_3 = "J\\1f5Z|->y\x0c)\t"
    str_4 = "%2Q"
    bool_2 = solution_1.isSubsequence(str_3, str_4)
    assert bool_2 is False
    bool_3 = solution_0.isSubsequence(str_2, str_0)
    assert bool_3 is False
    solution_2 = module_0.Solution()
    solution_2.isSubsequence(none_type_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ""
    solution_0 = module_0.Solution()
    bool_0 = True
    solution_1 = module_0.Solution()
    list_0 = []
    solution_2 = module_0.Solution(*list_0)
    list_1 = []
    str_1 = "DJw(1;cskxkvGYP/3We"
    bool_1 = solution_1.isSubsequence(str_0, str_1)
    assert bool_1 is True
    module_0.Solution(*list_1, **bool_0)
