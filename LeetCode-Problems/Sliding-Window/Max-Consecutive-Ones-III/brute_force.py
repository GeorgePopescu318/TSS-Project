# https://github.com/gahogg/Leetcode-Solutions/blob/main/Max%20Consecutive%20Ones%20III%20-%20Leetcode%201004/brute%20force.py

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        longest_ones = 0
        
        # Iterate over all starting points
        for i in range(len(nums)):

            # Iterate over all possible subarrays starting from i
            for j in range(i + 1, len(nums) + 1):
                window_len = j - i
                num_zeros = nums[i:j].count(0)  # O(k) operation
                if num_zeros <= k:
                    longest_ones = max(longest_ones, window_len)
        return longest_ones
