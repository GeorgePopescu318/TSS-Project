### GitHub
### https://github.com/gahogg/Leetcode-Solutions/blob/main/Jewels%20and%20Stones%20-%20Leetcode%20771/Jewels%20and%20Stones%20-%20Leetcode%20771.py
###
class Solution:
    def numJewelsInStones (self, jewels: str, stones: str) -> int:
        # O(n + m)
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count

# Time Complexity: O(n + m)
# Space Complexity: O(n)