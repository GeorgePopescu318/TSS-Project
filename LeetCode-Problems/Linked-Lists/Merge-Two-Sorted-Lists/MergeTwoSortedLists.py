#https://github.com/gahogg/Leetcode-Solutions/blob/main/Merge%20Two%20Sorted%20Lists%20-%20Leetcode%2021/Merge%20Two%20Sorted%20Lists%20-%20Leetcode%2021.py

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    d = ListNode()  # Dummy node
    cur = d

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            cur = list1
            list1 = list1.next
        else:
            cur.next = list2
            cur = list2
            list2 = list2.next

    cur.next = list1 if list1 else list2
    return d.next
