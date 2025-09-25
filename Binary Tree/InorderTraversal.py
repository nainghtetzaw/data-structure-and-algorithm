from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(self, root.left) + [root.val] + self.inorderTraversal(self, root.right)
    
left = TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7)))
right = TreeNode(3, None, TreeNode(8, TreeNode(9)))
root = TreeNode(1, left, right)
result = Solution.inorderTraversal(Solution, root)

for i in result:
    print(i)