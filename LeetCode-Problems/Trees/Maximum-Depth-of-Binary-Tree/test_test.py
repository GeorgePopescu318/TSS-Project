import pytest
from collections import deque
from test import TreeNode, Solution

# Assuming the TreeNode and Solution classes have been defined as per the provided code

def create_tree_from_list(values):
    """Helper function to create a binary tree from a list of values using level order insertion"""
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    queue = deque([root])
    for val in it:
        current = queue.popleft()
        if val is not None:
            current.left = TreeNode(val)
            queue.append(current.left)
        if val := next(it, None):
            current.right = TreeNode(val)
            queue.append(current.right)
    return root

@pytest.mark.parametrize("values, expected_depth", [
    ([], 0),  # Test empty tree
    ([1], 1),  # Single node
    ([1, 2, 3], 2),  # Simple two-level tree
    ([1, 2, 3, 4, None, None, 5], 3),  # Unbalanced tree
    ([1, None, 2, None, 3], 3),  # Right skewed tree
    ([1, 2, None, 3], 3),  # Left skewed tree
])
def test_max_depth(values, expected_depth):
    """Test maxDepth method for various tree structures"""
    root = create_tree_from_list(values)
    solution = Solution()
    assert solution.maxDepth(root) == expected_depth
