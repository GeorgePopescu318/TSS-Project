#https://github.com/gahogg/Leetcode-Solutions/blob/main/Remove%20Nth%20Node%20from%20End%20of%20List%20-%20Leetcode%2019/Remove%20Nth%20Node%20from%20End%20of%20List%20-%20Leetcode%2019.py

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]: 
    dummy = ListNode()
    dummy.next = head
    behind = ahead = dummy

    for _ in range(n + 1):
        ahead = ahead.next

    while ahead:
        behind = behind.next
        ahead = ahead.next

    behind.next = behind.next.next
    return dummy.next