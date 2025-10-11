# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = []
        qQueue = []

        def inputQueue(curr: Optional[TreeNode], queue: List):
            if curr:
                queue.append(str(curr.val))
            else:
                queue.append("null")
                return
            inputQueue(curr.left, queue)
            inputQueue(curr.right, queue)
        
        inputQueue(p, pQueue)
        inputQueue(q, qQueue)

        return pQueue == qQueue