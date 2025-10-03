# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from ArrayAndHashMap.MergeSort import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        res = ListNode()
        tail = res
        carry = 0
        while tail:
            if not p1:
                p1 = ListNode(0)
            if not p2:
                p2 = ListNode(0)

            add = str(p1.val + p2.val + carry)
            if len(add) == 2:
                carry = int(add[0])
                tail.val = int(add[1])
            else:
                carry = 0
                tail.val = int(add[0])
            
            tail.next = ListNode() if p1.next or p2.next or carry > 0 else None
            tail = tail.next
            p1 = p1.next
            p2 = p2.next

        return res