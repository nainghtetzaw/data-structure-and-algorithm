"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def getNodeLen(self, node: 'Node') -> int:
        count = []
         
        def dfs(node):
            if node.val in count:
                return
            
            count.append(node.val)

            if node.neighbors:
                for i in node.neighbors:
                    dfs(i)
                
        dfs(node)
        return len(count)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        res = []

        for i in range(self.getNodeLen(node)):
            res.append(Node())

        def clone(n):
            cur = res[n.val - 1]
            if res[n.val - 1].val != 0:
                return

            temp = res[n.val - 1]
            temp.val = n.val

            res[n.val - 1] = temp

            if n.neighbors:
                for i in n.neighbors:
                    temp.neighbors.append(res[i.val - 1])
                    clone(i)
                
            res[n.val - 1] = temp
        
        clone(node)
        return res[0]