import pytest
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


@pytest.fixture
def solution():
    return Solution()


def test_empty_tree(solution):
    assert solution.getMinimumDifference(None) == float('inf')


def test_single_node_tree(solution):
    root = TreeNode(1)
    assert solution.getMinimumDifference(root) == float('inf')


def test_two_nodes_tree(solution):
    root = TreeNode(1)
    root.right = TreeNode(3)
    assert solution.getMinimumDifference(root) == 2


def test_complete_tree(solution):
    # Constructing the BST
    #       4
    #      / \
    #     2   6
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    assert solution.getMinimumDifference(root) == 1


def test_unbalanced_tree(solution):
    # Constructing the BST
    #       10
    #         \
    #          20
    #            \
    #             30
    root = TreeNode(10)
    root.right = TreeNode(20)
    root.right.right = TreeNode(30)
    
    assert solution.getMinimumDifference(root) == 10


def test_tree_with_negative_values(solution):
    # Constructing the BST
    #       -10
    #       /  \
    #     -20   0
    #     /
    #   -30
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.left.left = TreeNode(-30)
    root.right = TreeNode(0)

    assert solution.getMinimumDifference(root) == 10
