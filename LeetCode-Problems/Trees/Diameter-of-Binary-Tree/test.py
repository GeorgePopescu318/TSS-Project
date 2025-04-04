# https://github.com/gahogg/Leetcode-Solutions/blob/main/Diameter%20of%20Binary%20Tree%20-%20Leetcode%20543/Diameter%20of%20Binary%20Tree%20-%20Leetcode%20543.py

from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]

        def height(root):
            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height

            largest_diameter[0] = max(largest_diameter[0], diameter)
            
            return 1 + max(left_height, right_height)

        height(root)
        return largest_diameter[0]

# Time Complexity: O(n)
# Space Complexity: O(h) { here "h" is the height of the tree }