from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(self, root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(self, root.left, val)

        return root

root = TreeNode(
    4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(7)
)
