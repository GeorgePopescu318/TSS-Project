# https://github.com/gahogg/Leetcode-Solutions/blob/main/Minimum%20Absolute%20Difference%20in%20BST%20-%20Leetcode%20530/Minimum%20Absolute%20Difference%20in%20BST%20-%20Leetcode%20530.py

from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_distance = [float('inf')]
        prev = [None]

        def dfs(node):
            if node is None:
                return
                
            dfs(node.left)

            if prev[0] is not None:
                min_distance[0] = min(min_distance[0], node.val - prev[0])

            prev[0] = node.val
            dfs(node.right)

        dfs(root)
        return min_distance[0]
        # Time: O(n)
        # Space: O(n)