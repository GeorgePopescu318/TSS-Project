import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    cur = head
    prev = None

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev

def list_to_linkedlist(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(node):
    elements = []
    current = node
    while current:
        elements.append(current.val)
        current = current.next
    return elements

@pytest.mark.parametrize("input_list, expected_output_list", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [3, 2, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
])
def test_reverseList(input_list, expected_output_list):
    head = list_to_linkedlist(input_list)
    reversed_head = reverseList(head)
    output_list = linkedlist_to_list(reversed_head)
    assert output_list == expected_output_list

def test_reverseList_with_one_element():
    head = ListNode(1)
    reversed_head = reverseList(head)
    assert reversed_head.val == 1
    assert reversed_head.next is None

def test_reverseList_with_none():
    reversed_head = reverseList(None)
    assert reversed_head is None
