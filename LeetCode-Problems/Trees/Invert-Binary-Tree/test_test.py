import pytest
from test import TreeNode, Solution

# Utility function to help build a tree from list input for testing purposes
def build_tree(nodes):
    """
    Build a binary tree from the list of values using level-order insertion.
    A value of 'None' signifies there is no child node at that position.
    """
    if not nodes:
        return None
    
    it = iter(nodes)
    root = TreeNode(next(it))
    queue = [root]
    for val in it:
        current = queue.pop(0)
        if val is not None:
            current.left = TreeNode(val)
            queue.append(current.left)
        if val is not None:
            current.right = TreeNode(next(it, None))
            queue.append(current.right)
    return root

# Utility function to convert tree structure to a list using level-order traversal
def convert_to_list(node):
    if not node:
        return []

    result, queue = [], [node]
    while any(queue):
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result

def test_invertTree_empty():
    sol = Solution()
    assert sol.invertTree(None) is None

def test_invertTree_single_node():
    sol = Solution()
    root = TreeNode(1)
    inverted = sol.invertTree(root)
    assert inverted.val == 1
    assert inverted.left is None
    assert inverted.right is None

def test_invertTree_complete_tree():
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    inverted = sol.invertTree(root)
    result = convert_to_list(inverted)
    assert result == [1, 3, 2, 7, 6, 5, 4]

def test_invertTree_left_heavy_tree():
    sol = Solution()
    root = build_tree([1, 2, None, 3, None, None, None])
    inverted = sol.invertTree(root)
    result = convert_to_list(inverted)
    assert result == [1, None, 2, None, None, 3]

def test_invertTree_right_heavy_tree():
    sol = Solution()
    root = build_tree([1, None, 2, None, None, None, 3])
    inverted = sol.invertTree(root)
    result = convert_to_list(inverted)
    assert result == [1, 2, None, 3, None]

def test_invertTree_asymmetric_tree():
    sol = Solution()
    root = build_tree([1, 2, 3, None, 4, None, 5])
    inverted = sol.invertTree(root)
    result = convert_to_list(inverted)
    assert result == [1, 3, 2, 5, None, 4, None]

if __name__ == "__main__":
    pytest.main()
