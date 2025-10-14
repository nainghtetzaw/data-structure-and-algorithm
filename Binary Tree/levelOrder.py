from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        hm = {0:[root.val]}

        def order(root: Optional[TreeNode], level: int):
            if not root:
                return
            
            hm[level] = hm.get(level, [])
            hm[level].append(root.val)

            order(root.left, level + 1)
            order(root.right, level + 1)
        
        order(root.left, 1)
        order(root.right, 1)

        return list(hm.values())
                    
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
result = Solution.levelOrder(Solution, root)

for i in result:
    print(i)