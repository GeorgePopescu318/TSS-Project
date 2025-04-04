### GitHub
### http://github.com/gahogg/Leetcode-Solutions/blob/main/Contains%20Duplicate%20-%20Leetcode%20217/Contains%20Duplicate%20-%20Leetcode%20217.py
###
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)