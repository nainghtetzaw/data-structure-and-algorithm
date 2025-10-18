# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")
        self.dfs(root)
        return self.max
        
    
    def dfs(self, node) -> Optional[int]:
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.max = max([self.max, (node.val + left + right), node.val, max(left, right) + node.val])

        if (max(left, right) + node.val) > node.val:
            return max(left, right) + node.val
        
        return node.val