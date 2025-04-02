# https://github.com/gahogg/Leetcode-Solutions/blob/main/Maximum%20Average%20Subarray%20I%20-%20Leetcode%20643/brute%20force.py

# pynguin --project-path . --module-name run_tests --output-path . --verbose --minimum-coverage 75 --maximum-coverage 79 --minimum-plateau-iterations 1
# $env:PYNGUIN_DANGER_AWARE="true"  

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        def avg(vals):
            return sum(vals) / float(len(vals))

        # Note, setting max_avg to any constant numeric value 
        # here is incorrect!!! 
        # Say 0, if nums = [-1, -2, -3, -4], k = 2, 
        # the output would be incorrect
        max_avg = avg(nums[:k])
        for i in range(len(nums) - k + 1):
            max_avg = max(max_avg, avg(nums[i:i+k])) # avg is O(k)
        return max_avg

