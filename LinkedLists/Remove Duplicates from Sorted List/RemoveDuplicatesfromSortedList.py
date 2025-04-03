#https://github.com/gahogg/Leetcode-Solutions/blob/main/Remove%20Duplicates%20from%20Sorted%20List%20-%20Leetcode%2083/Remove%20Duplicates%20from%20Sorted%20List%20-%20Leetcode%2083.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

