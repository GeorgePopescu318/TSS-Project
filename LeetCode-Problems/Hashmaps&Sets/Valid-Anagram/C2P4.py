### GitHub
### https://github.com/gahogg/Leetcode-Solutions/blob/main/Valid%20Anagram%20-%20Leetcode%20242/Valid%20Anagram%20-%20Leetcode%20242.py
###
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict

# Let n be the length of the longest word
# Time complexity: O(n)
# Space complexity: O(n)