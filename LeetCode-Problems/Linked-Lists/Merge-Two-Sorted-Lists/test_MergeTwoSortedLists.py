import pytest
from MergeTwoSortedLists import mergeTwoLists
from MergeTwoSortedLists import ListNode

# A helper function to create a linked list from a list of values.
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# A helper function to convert linked list to normal list for easy comparison in tests.
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_merge_both_empty():
    assert mergeTwoLists(None, None) is None

def test_merge_one_empty():
    list1 = create_linked_list([1, 3, 5])
    assert linked_list_to_list(mergeTwoLists(list1, None)) == [1, 3, 5]
    assert linked_list_to_list(mergeTwoLists(None, list1)) == [1, 3, 5]

def test_merge_disjoint():
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])
    result = mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

def test_merge_with_duplicates():
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([1, 3, 5])
    result = mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 3, 3, 5, 5]

def test_merge_nested():
    list1 = create_linked_list([1, 2, 3, 5, 6])
    list2 = create_linked_list([4, 7, 8])
    result = mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_single_element_lists():
    list1 = create_linked_list([1])
    list2 = create_linked_list([2])
    result = mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2]

def test_merge_interleaved():
    list1 = create_linked_list([1, 4, 7])
    list2 = create_linked_list([2, 5, 6, 8])
    result = mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 4, 5, 6, 7, 8]

