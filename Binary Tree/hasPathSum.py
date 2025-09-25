from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, sum: int = 0) -> bool:
        if not root:
            return False
        
        sum += root.val
        if not root.left and not root.right:
            return sum == targetSum
        if self.hasPathSum(self, root.left, targetSum, sum):
            return True
        if self.hasPathSum(self, root.right, targetSum, sum):
            return True
        
        return False
    
left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
root = TreeNode(5, left, right)

print(Solution.hasPathSum(Solution, root, 22))