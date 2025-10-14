# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 1

        def isGood(curr: TreeNode, maxVal: int):
            if not curr:
                return

            if maxVal <= curr.val:
                self.count += 1
            maxVal = max(maxVal, curr.val)

            isGood(curr.left, maxVal)
            isGood(curr.right, maxVal)
        
        isGood(root.left, root.val)
        isGood(root.right, root.val)
        return self.count
