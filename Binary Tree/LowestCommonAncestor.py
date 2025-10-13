# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pNodes = []
        qNodes = []

        def listDownAncestors(curr: 'TreeNode', target: 'TreeNode', ancestors: List['TreeNode']) -> bool:
            if not curr:
                return False
            
            if curr.val == target.val:
                ancestors.append(curr)
                return True
            
            if (listDownAncestors(curr.left, target, ancestors) 
            or listDownAncestors(curr.right, target, ancestors)):
                ancestors.append(curr)
                return True

            return False
        
        listDownAncestors(root, p, pNodes)
        listDownAncestors(root, q, qNodes)

        while pNodes and qNodes and pNodes[0].val != qNodes[0].val:
            if len(pNodes) > len(qNodes):
                del pNodes[0]
            else:
                del qNodes[0]

        return pNodes[0]