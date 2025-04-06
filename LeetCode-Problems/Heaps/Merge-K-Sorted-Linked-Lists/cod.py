import heapq
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    D = ListNode()
    cur = D
    
    # n log k
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = node
        node = node.next
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    return D.next