# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from ArrayAndHashMap.MergeSort import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def isTargetNode(node: Optional[ListNode], count: int) -> bool:
            if count > 1:
                return isTargetNode(node.next, count - 1)
            
            if count == 1 and not node.next:
                return True
            
            return False

        res = ListNode(0, head)
        prev = res
        tail = res.next
        while tail:
            if isTargetNode(tail, n):
                prev.next = tail.next
                return res.next

            prev = tail
            tail = tail.next

        return res.next