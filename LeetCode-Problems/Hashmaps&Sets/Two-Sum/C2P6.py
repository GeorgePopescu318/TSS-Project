### GitHub
### https://github.com/gahogg/Leetcode-Solutions/blob/main/Two%20Sum%20-%20Leetcode%201/Two%20Sum%20-%20Leetcode%201.py
###
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        n = len(nums)
        for i, x in enumerate(nums):
            y = target - x
            if y in h:
                return [i, h[y]]
            else:
                h[x] = i
# Time Complexity: O(n)
# Space Complexity: O(n)