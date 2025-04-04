# https://github.com/gahogg/Leetcode-Solutions/blob/main/Balanced%20Binary%20Tree%20-%20Leetcode%20110/Balanced%20Binary%20Tree%20-%20Leetcode%20110.py

from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            if balanced[0] is False:
                return 0


            right_height = height(root.right)
            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]

# Time Complexity: O(n)
# Space Complexity: O(h) { here "h" is the height of the tree }