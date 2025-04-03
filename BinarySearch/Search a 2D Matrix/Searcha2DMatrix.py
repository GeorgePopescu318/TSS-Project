#https://github.com/gahogg/Leetcode-Solutions/blob/main/Search%20a%202D%20Matrix%20-%20Leetcode%2074/Search%20a%202D%20Matrix%20-%20Leetcode%2074.py

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    t = m * n
    l = 0
    r = t - 1

    while l <= r:
        mid = (l + r) // 2
        mid_i = mid // n
        mid_j = mid % n
        mid_num = matrix[mid_i][mid_j]

        if target == mid_num:
            return True
        elif target < mid_num:
            r = mid - 1
        else:
            l = mid + 1

    return False
