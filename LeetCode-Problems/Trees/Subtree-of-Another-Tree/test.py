# https://github.com/gahogg/Leetcode-Solutions/blob/main/Subtree%20of%20Another%20Tree%20-%20Leetcode%20572/Subtree%20of%20Another%20Tree%20-%20Leetcode%20572.py

from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def has_subtree(root):
            if not root:
                return False

            if sameTree(root, subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)

        return has_subtree(root)

# Time Complexity: O(m * n)
# Space Complexity: O(n)