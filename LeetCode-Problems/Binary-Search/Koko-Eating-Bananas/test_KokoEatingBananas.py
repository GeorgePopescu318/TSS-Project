import pytest
from math import ceil
from typing import List

# Assuming the existing function is imported
# from my_module import minEatingSpeed

def minEatingSpeed(piles: List[int], h: int) -> int:
    def k_works(k):
        hours = 0
        for p in piles:
            hours += ceil(p / k)
        return hours <= h

    l = 1
    r = max(piles) 

    while l < r:
        k = (l + r) // 2
        if k_works(k):
            r = k
        else:
            l = k + 1

    return r

# Test cases
def test_single_pile():
    assert minEatingSpeed([4], 4) == 1

def test_multiple_piles():
    assert minEatingSpeed([3, 6, 7, 11], 8) == 4

def test_edge_case_min_speed():
    assert minEatingSpeed([30, 11, 23, 4, 20], 5) == 30

def test_edge_case_max_speed():
    assert minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

def test_large_piles():
    assert minEatingSpeed([312884470], 312884469) == 2

def test_all_small_piles():
    assert minEatingSpeed([1, 1, 1, 1], 4) == 1

def test_large_hrs():
    assert minEatingSpeed([5, 10, 15], 100) == 1

def test_large_input():#FAILED: assert 10000 == 10 +  where 10000 = minEatingSpeed([10000000, 10000000, 10000000, 10000000, 10000000, 10000000, ...], 1000000)
    piles = [10000000] * 1000
    h = 1000000
    assert minEatingSpeed(piles, h) == 10

@pytest.mark.parametrize("input_data, expected", [
    ([1], 1),
    ([1,2,3,4,5,6,7,8,9,10], 5), #FAILED: assert 1 == 5 +  where 1 = minEatingSpeed([1, 2, 3, 4, 5, 6, ...], 55)
    ([1000000000], 1000000000) #FAILED: assert 1 == 1000000000 +  where 1 = minEatingSpeed([1000000000], 1000000000)
])
def test_various_cases(input_data, expected):
    h = sum(input_data)
    assert minEatingSpeed(input_data, h) == expected

