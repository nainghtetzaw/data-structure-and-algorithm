# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional, Set

from ArrayAndHashMap.MergeSort import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        
        def isLinkedListCycle(head: Optional[ListNode], nodes: Set) -> bool:
            if not head:
                return False

            if head in nodes:
                return True

            nodes.add(head)
            
            if head.next:
                return isLinkedListCycle(head.next, nodes)

            return False
            
            
        return isLinkedListCycle(head, nodes)