class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l + 1, r + 1]
            elif summ < target:
                l += 1
            else:
                r -= 1

#Source : https://github.com/gahogg/Leetcode-Solutions/blob/main/Two%20Sum%20II%20-%20Leetcode%20167/Two%20Sum%20II%20-%20Leetcode%20167.py