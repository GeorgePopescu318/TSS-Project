import pytest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        current_self, current_other = self, other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

def to_list(head: Optional[ListNode]) -> list:
    """Helper function to convert ListNode to Python list for easier assertion."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def to_linked_list(elements: list) -> Optional[ListNode]:
    """Helper function to convert Python list to ListNode for test setup."""
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# Import the main function to test
from RemoveNthNodefromEndofList import removeNthFromEnd  # Replace 'your_module' with the actual module name

def test_remove_nth_from_list_of_length_5():
    head = to_linked_list([1, 2, 3, 4, 5])
    n = 2
    expected = to_linked_list([1, 2, 3, 5])
    result = removeNthFromEnd(head, n)
    assert result == expected

def test_remove_head_of_list():
    head = to_linked_list([1, 2, 3, 4, 5])
    n = 5
    expected = to_linked_list([2, 3, 4, 5])
    result = removeNthFromEnd(head, n)
    assert result == expected

def test_remove_tail_of_list():
    head = to_linked_list([1, 2, 3, 4, 5])
    n = 1
    expected = to_linked_list([1, 2, 3, 4])
    result = removeNthFromEnd(head, n)
    assert result == expected

def test_remove_from_single_element_list():
    head = to_linked_list([1])
    n = 1
    expected = to_linked_list([])
    result = removeNthFromEnd(head, n)
    assert result == expected

def test_large_n_greater_than_length():
    head = to_linked_list([1, 2, 3, 4, 5])
    n = 6
    with pytest.raises(AttributeError):
        removeNthFromEnd(head, n)

def test_corner_case_empty_list():#FAILED: AttributeError: 'NoneType' object has no attribute 'next'
    head = to_linked_list([])
    n = 1
    expected = to_linked_list([])
    result = removeNthFromEnd(head, n)
    assert result == expected
