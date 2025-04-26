import pytest
from RemoveDuplicatesfromSortedList import deleteDuplicates
from RemoveDuplicatesfromSortedList import ListNode

# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def linkedlist_to_list(node):
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases

def test_empty_list():
    head = list_to_linkedlist([])
    modified_head = deleteDuplicates(head)
    assert linkedlist_to_list(modified_head) == []

def test_single_element_list():
    head = list_to_linkedlist([1])
    modified_head = deleteDuplicates(head)
    assert linkedlist_to_list(modified_head) == [1]

def test_no_duplicates():
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    modified_head = deleteDuplicates(head)
    assert linkedlist_to_list(modified_head) == [1, 2, 3, 4, 5]

def test_all_duplicates():
    head = list_to_linkedlist([1, 1, 1, 1, 1])
    modified_head = deleteDuplicates(head)
    assert linkedlist_to_list(modified_head) == [1]

def test_some_duplicates():
    head = list_to_linkedlist([1, 1, 2, 3, 3, 4, 5, 5])
    modified_head = deleteDuplicates(head)
    assert linkedlist_to_list(modified_head) == [1, 2, 3, 4, 5]

def test_duplicates_at_beginning():
    head = list_to_linkedlist([1, 1, 2, 3, 4, 5])
    modified_head = deleteDuplicates(head)
    assert linkedlist_to_list(modified_head) == [1, 2, 3, 4, 5]

def test_duplicates_at_end():
    head = list_to_linkedlist([1, 2, 3, 4, 5, 5])
    modified_head = deleteDuplicates(head)
    assert linkedlist_to_list(modified_head) == [1, 2, 3, 4, 5]

