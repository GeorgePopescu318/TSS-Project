# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import test as module_0


# @pytest.mark.xfail(strict=True)
def test_case_0(): # FAILED - TypeError: ord() expected string of length 1, but int found
    bytes_0 = b"\x91 [z\x95\xf9A(\xe0\x1f[Bc\xb8\x93\xea\xc3"
    int_0 = 205
    dict_0 = {}
    solution_0 = module_0.Solution(**dict_0)
    solution_0.characterReplacement(bytes_0, int_0)


# @pytest.mark.xfail(strict=True)
def test_case_1(): # FAILED - TypeError: Solution() takes no arguments
    bytes_0 = b"\xa9\xfd\x84#yPR\x08\xa5%=C"
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0]
    module_0.Solution(*list_1)


# @pytest.mark.xfail(strict=True)
def test_case_2(): # FAILED - IndexError: list index out of range
    str_0 = "81$8"
    bool_0 = False
    solution_0 = module_0.Solution()
    solution_0.characterReplacement(str_0, bool_0)


# @pytest.mark.xfail(strict=True)
def test_case_3(): # FAILED - IndexError: list index out of range
    str_0 = ""
    solution_0 = module_0.Solution()
    int_0 = solution_0.characterReplacement(str_0, str_0)
    assert int_0 == 0
    int_1 = -20
    str_1 = "81$8"
    solution_1 = module_0.Solution()
    solution_1.characterReplacement(str_1, int_1)
