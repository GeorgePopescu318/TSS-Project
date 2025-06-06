#https://github.com/gahogg/Leetcode-Solutions/blob/main/Koko%20Eating%20Bananas%20-%20Leetcode%20875/Koko%20Eating%20Bananas%20-%20Leetcode%20875.py

from typing import List
from math import ceil

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
