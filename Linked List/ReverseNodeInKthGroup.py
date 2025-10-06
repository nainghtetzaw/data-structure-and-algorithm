# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodeList = []
        tail = head
        while tail:
            nodeList.append(tail)
            tail = tail.next

        l = 0
        window = k - 1
        while window < len(nodeList):
            r = window
            while l <= r:
                temp = nodeList[l].val
                nodeList[l].val = nodeList[r].val
                nodeList[r].val = temp
                
                if r - 1 > l:
                    nodeList[r - 1].next = nodeList[r]
                
                l += 1
                r -= 1
            
            l = window + 1
            window = window + k
        
        return nodeList[0]

                
            