class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        L, R = 0, n-1
        result = [0] * n

        for i in range(n):
            nums[i] = nums[i] ** 2

        j = n-1
        while L <= R:
            if nums[L] > nums[R]:
                result[j] = nums[L]
                L += 1
            else:
                result[j] = nums[R]
                R -= 1

            j -= 1
        
        return result


#Source : https://github.com/gahogg/Leetcode-Solutions/blob/main/Squares%20of%20a%20Sorted%20Array%20-%20Leetcode%20977/Squares%20of%20a%20Sorted%20Array%20-%20Leetcode%20977.py