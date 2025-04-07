class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        h = {}
        n = len(nums)
        s = set()

        for i, num in enumerate(nums):
            h[num] = i

        for i in range(n):
            for j in range(i + 1, n):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted([nums[i], nums[j], desired])))

        return s


#Source : https://github.com/gahogg/Leetcode-Solutions/blob/main/3Sum%20-%20Leetcode%2015/3Sum%20-%20Leetcode%2015.py