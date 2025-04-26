#https://github.com/gahogg/Leetcode-Solutions/blob/main/Search%20Insert%20Position%20-%20Leetcode%2035/Search%20Insert%20Position%20-%20Leetcode%2035.py

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        if nums[m] < target:
            return m + 1
        else:
            return m
