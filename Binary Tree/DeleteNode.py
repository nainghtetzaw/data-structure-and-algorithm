# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minNode(self, root: TreeNode) -> TreeNode:
        current = root
        while current and current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(self, root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(self, root.left, key)
        else :
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minNode(self, root.right)
                root.val = minNode.val
                root.right = self.deleteNode(self, root.right, minNode.val)    

        return root

# root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
root = TreeNode(2, TreeNode(1))
result = Solution.deleteNode(Solution, root, 2)
print(result)