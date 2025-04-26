#https://github.com/gahogg/Leetcode-Solutions/blob/main/Copy%20List%20with%20Random%20Pointer%20-%20Leetcode%20138/Copy%20List%20with%20Random%20Pointer%20-%20Leetcode%20138.py

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
        node = Node(x=curr.val)
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
