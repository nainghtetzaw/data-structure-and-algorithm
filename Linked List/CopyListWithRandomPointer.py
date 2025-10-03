"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

import collections
from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        hm = collections.defaultdict(lambda: Node(0))
        hm[None] = None

        curr = head
        while curr:
            hm[curr].val = curr.val
            hm[curr].next = hm[curr.next]
            hm[curr].random = hm[curr.random]
            curr = curr.next
        
        return hm[head]