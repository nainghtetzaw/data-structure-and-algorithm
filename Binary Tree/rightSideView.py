from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        q = [root]

        while q:
            rightSideVal = None

            for i in range(len(q)):
                curr = q.pop(0)
                rightSideVal = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            result.append(rightSideVal)

        return result
    
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
result = Solution.rightSideView(Solution, root)
for i in result:
    print(i)