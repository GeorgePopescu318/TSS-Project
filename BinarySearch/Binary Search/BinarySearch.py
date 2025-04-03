#https://github.com/gahogg/Leetcode-Solutions/blob/main/Binary%20Search%20-%20Leetcode%20704/Binary%20Search%20-%20Leetcode%20704.py

from typing import List

def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (right + left) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1
