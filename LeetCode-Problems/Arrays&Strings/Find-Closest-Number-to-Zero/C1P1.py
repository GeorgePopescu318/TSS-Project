### GitHub
### https://github.com/gahogg/Leetcode-Solutions/blob/main/Find%20Closest%20Number%20to%20Zero%20-%20Leetcode%202239/Find%20Closest%20Number%20to%20Zero%20-%20Leetcode%202239.py
###

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
        # Time: O(n)
        # Space: O(1)``