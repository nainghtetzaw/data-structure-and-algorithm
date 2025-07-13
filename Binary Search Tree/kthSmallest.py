from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        treeList = self.toList(self, root)
        return treeList[k - 1]
    
    def toList(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.toList(self, root.left) + [root.val] + self.toList(self, root.right)
    
left = TreeNode(2, None, TreeNode(3))
right = TreeNode(5)
root = TreeNode(4, left, right)

print(Solution.kthSmallest(Solution, root, 2))