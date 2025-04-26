import pytest
from test import Solution, TreeNode

# Assuming the TreeNode and Solution classes have been imported as mentioned

def build_tree_from_list(lst, index=0):
    """ Helper function to build a tree from a list using level order traversal """
    if index < len(lst):
        value = lst[index]
        if value is not None:
            node = TreeNode(value)
            node.left = build_tree_from_list(lst, 2*index+1)
            node.right = build_tree_from_list(lst, 2*index+2)
            return node
    return None

def test_subtree_present():
    root = build_tree_from_list([3, 4, 5, 1, 2])
    subRoot = build_tree_from_list([4, 1, 2])
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == True

def test_subtree_not_present():
    root = build_tree_from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = build_tree_from_list([4, 1, 2])
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == False

def test_same_tree():
    root = build_tree_from_list([1, 2, 3])
    subRoot = build_tree_from_list([1, 2, 3])
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == True

def test_subtree_at_leaf_level():
    root = build_tree_from_list([3, 4, 5, 1, None, None, 2])
    subRoot = build_tree_from_list([2])
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == True

def test_empty_subroot():
    root = build_tree_from_list([1])
    subRoot = None
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == True

def test_empty_root():
    root = None
    subRoot = build_tree_from_list([1])
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == False

def test_both_empty():
    root = None
    subRoot = None
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == True

def test_subtree_not_present_due_to_value_mismatch():
    root = build_tree_from_list([1, 2, 3])
    subRoot = build_tree_from_list([2, 3])
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == False
