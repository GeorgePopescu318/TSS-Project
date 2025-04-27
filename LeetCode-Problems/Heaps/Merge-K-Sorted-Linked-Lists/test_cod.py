import pytest
# Helper function to convert a list to a linked list
from cod import mergeKLists #nu a importat asta
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to convert a linked list to a list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

@pytest.mark.parametrize("lists, expected", [
    # Test case 1: Merging three sorted linked lists
    (
        [list_to_linkedlist([1, 4, 5]), list_to_linkedlist([1, 3, 4]), list_to_linkedlist([2, 6])],
        [1, 1, 2, 3, 4, 4, 5, 6]
    ),
    # Test case 2: Merging lists where one list is empty
    (
        [list_to_linkedlist([]), list_to_linkedlist([1, 3, 4]), list_to_linkedlist([2, 6])],
        [1, 2, 3, 4, 6]
    ),
    # Test case 3: Merging lists where all lists are empty
    (
        [list_to_linkedlist([]), list_to_linkedlist([]), list_to_linkedlist([])],
        []
    ),
    # Test case 4: Merging lists with different lengths
    (
        [list_to_linkedlist([1, 2]), list_to_linkedlist([3]), list_to_linkedlist([4, 5, 6])],
        [1, 2, 3, 4, 5, 6]
    ),
    # Test case 5: Merging a single non-empty list
    (
        [list_to_linkedlist([1, 2, 3])],
        [1, 2, 3]
    ),
    # Test case 6: Merging a single empty list
    (
        [list_to_linkedlist([])],
        []
    ),
    # Test case 7: Merging lists with duplicate values
    (
        [list_to_linkedlist([1, 1, 1]), list_to_linkedlist([1, 1]), list_to_linkedlist([1])],
        [1, 1, 1, 1, 1, 1]
    ),
])
def test_mergeKLists(lists, expected):
    result = mergeKLists(lists)
    assert linkedlist_to_list(result) == expected
