# https://github.com/gahogg/Leetcode-Solutions/blob/main/Longest%20Repeating%20Character%20Replacement%20-%20Leetcode%20424/Longest%20Repeating%20Character%20Replacement%20-%20Leetcode%20424.py

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1

            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest

# Time Complexity: O(n)
# Space Complexity: O(1)