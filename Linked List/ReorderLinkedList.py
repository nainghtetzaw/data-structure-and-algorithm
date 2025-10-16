# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        orderList = []

        tail = head
        while tail:
            orderList.append(tail)
            tail = tail.next

        l, r = 0, len(orderList) - 1
        while l < r:
            temp = orderList[l].next
            orderList[r].next = temp
            orderList[l].next = orderList[r] 
            l += 1
            r -= 1
            
        orderList[l].next = None
        head = orderList[0]