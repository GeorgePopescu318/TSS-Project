#https://github.com/gahogg/Leetcode-Solutions/blob/main/Reverse%20Linked%20List%20-%20Leetcode%20206/Reverse%20Linked%20List%20-%20Leetcode%20206.py

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