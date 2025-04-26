import pytest
from test import TreeNode, Solution
# Import the class and method from the module if stored separately
# from module_name import TreeNode, Solution

@pytest.fixture
def solution():
    return Solution()

def test_empty_tree(solution):
    assert solution.isBalanced(None) == True

def test_single_node_tree(solution):
    root = TreeNode(1)
    assert solution.isBalanced(root) == True

def test_balanced_tree(solution):
    # Constructing the following balanced tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert solution.isBalanced(root) == True

def test_unbalanced_tree_due_to_left_depth(solution):
    # Constructing the following unbalanced tree:
    #       1
    #      /
    #     2
    #    /
    #   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert solution.isBalanced(root) == False

def test_unbalanced_tree_due_to_right_depth(solution):
    # Constructing the following unbalanced tree:
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert solution.isBalanced(root) == False

def test_balanced_tree_with_varying_depth(solution):
    # Constructing the following balanced tree:
    #      1
    #     / \
    #    2   3
    #   /     \
    #  4       5
    #           \
    #            6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    assert solution.isBalanced(root) == True

def test_complex_unbalanced_tree(solution):
    # Constructing an unbalanced tree:
    #        1
    #       / \
    #      2   2
    #     / \
    #    3   3
    #   / 
    #  4 
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert solution.isBalanced(root) == False

# To run the tests, execute the command: pytest -q test_script.py
