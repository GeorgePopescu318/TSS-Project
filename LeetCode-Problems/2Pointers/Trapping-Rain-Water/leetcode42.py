class Solution:
    def trap(self, height: list[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])

        return summ
    
    
#Source : https://github.com/gahogg/Leetcode-Solutions/blob/main/Trapping%20Rain%20Water%20-%20Leetcode%2042/Trapping%20Rain%20Water%20-%20Leetcode%2042.py