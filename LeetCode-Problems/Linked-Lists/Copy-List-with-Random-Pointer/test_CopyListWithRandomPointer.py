import pytest
from typing import Optional

class Node:
    def __init__(self, val: int = 0, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    curr = head
    old_to_new = {}

    # First pass: Copy all the nodes.
    while curr:
        node = Node(val=curr.val)
        old_to_new[curr] = node
        curr = curr.next

    # Second pass: Set next and random pointers.
    curr = head
    while curr:
        new_node = old_to_new[curr]
        new_node.next = old_to_new[curr.next] if curr.next else None
        new_node.random = old_to_new[curr.random] if curr.random else None
        curr = curr.next

    return old_to_new[head]

def test_empty_list():
    assert copyRandomList(None) is None

def test_single_node_no_random():
    node = Node(1)
    copied = copyRandomList(node)
    assert copied is not node
    assert copied.val == node.val
    assert copied.next is None
    assert copied.random is None

def test_single_node_with_random():
    node = Node(1)
    node.random = node
    copied = copyRandomList(node)
    assert copied is not node
    assert copied.val == node.val
    assert copied.next is None
    assert copied.random is copied

def test_multiple_nodes():
    # Create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    # Link nodes
    node1.next = node2
    node2.next = node3
    
    # Assign random pointers
    node1.random = node3
    node2.random = node1
    node3.random = node3

    # Copy list
    copied_head = copyRandomList(node1)

    # Validate structure and values
    assert copied_head is not node1
    assert copied_head.val == node1.val
    assert copied_head.next.val == node2.val
    assert copied_head.next.next.val == node3.val
    assert copied_head.random.val == node3.val
    assert copied_head.next.random.val == node1.val
    assert copied_head.next.next.random.val == node3.val
    assert copied_head.next.random is not node1
    assert copied_head.random is not node3

if __name__ == "__main__":
    pytest.main()
