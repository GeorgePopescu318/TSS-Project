import pytest
from leetcode42 import Solution

@pytest.fixture
def solution():
    return Solution()

def test_trap_empty_list(solution):
    assert solution.trap([]) == 0

def test_trap_no_trapping(solution):
    assert solution.trap([1, 2, 3, 4, 5]) == 0
    assert solution.trap([5, 4, 3, 2, 1]) == 0

def test_trap_single_peak(solution):
    assert solution.trap([0, 1, 0]) == 0
    assert solution.trap([0, 2, 0]) == 0

def test_trap_simple_valley(solution):
    assert solution.trap([0, 1, 0, 1, 0]) == 1
    assert solution.trap([0, 2, 0, 2, 0]) == 2

def test_trap_complex_terrain(solution):
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solution.trap([4, 2, 0, 3, 2, 5]) == 9

def test_trap_flat_surface(solution):
    assert solution.trap([0, 0, 0, 0]) == 0
    assert solution.trap([1, 1, 1, 1]) == 0

def test_trap_large_numbers(solution):
    assert solution.trap([1000, 0, 1000]) == 1000
    assert solution.trap([1000, 500, 1000]) == 500

def test_trap_alternating_peaks_and_valleys(solution):
    assert solution.trap([0, 2, 0, 2, 0, 2]) == 4
    assert solution.trap([3, 0, 3, 0, 3, 0, 3]) == 9

def test_trap_single_element(solution):
    assert solution.trap([1]) == 0

def test_trap_two_elements(solution):
    assert solution.trap([1, 2]) == 0
    assert solution.trap([2, 1]) == 0
