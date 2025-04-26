import pytest
from typing import Optional
from test import TreeNode, Solution

# Assuming the original class definitions for TreeNode and Solution are available.

def test_diameter_of_binary_tree_empty():
    solution = Solution()
    assert solution.diameterOfBinaryTree(None) == 0

def test_diameter_of_binary_tree_single_node():
    solution = Solution()
    root = TreeNode(1)
    assert solution.diameterOfBinaryTree(root) == 0

def test_diameter_of_binary_tree_two_nodes():
    solution = Solution()
    root = TreeNode(1, TreeNode(2))
    assert solution.diameterOfBinaryTree(root) == 1

def test_diameter_of_binary_tree_balanced():
    solution = Solution()
    # Balanced tree: depth 2, diameter should be 2
    #     1
    #    / \
    #   2   3
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert solution.diameterOfBinaryTree(root) == 2

def test_diameter_of_binary_tree_linear():
    solution = Solution()
    # Linear tree: depth 4, diameter should be 3
    # 1 - 2 - 3 - 4
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert solution.diameterOfBinaryTree(root) == 3

def test_diameter_of_binary_tree_skewed_right():
    solution = Solution()
    # Skewed tree to the right: depth 4, diameter should be 3
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert solution.diameterOfBinaryTree(root) == 3

def test_diameter_of_binary_tree_complex():
    solution = Solution()
    # Complex tree: diameter should be 4
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    #     /
    #    6
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6))),
                    TreeNode(3))
    assert solution.diameterOfBinaryTree(root) == 4

def test_diameter_of_binary_tree_large():
    solution = Solution()
    # Larger, more complex tree
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    #     / \
    #    6   7
    #       /
    #      8
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7, TreeNode(8)))),
                    TreeNode(3))
    assert solution.diameterOfBinaryTree(root) == 6

# You can execute the tests using a command like "pytest [name_of_this_file.py]"
