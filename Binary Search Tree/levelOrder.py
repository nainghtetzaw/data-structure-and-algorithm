from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result: List[List[int]] = []
        queue = [root]
        level = 0

        while len(queue) > 0:
            print("level", level)
            
            for i in range(len(queue)):
                curr = queue.pop(0)

                try:
                    result[level].append(curr.val)
                except:
                    result.append([curr.val])
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            level += 1

        return result
                    
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
result = Solution.levelOrder(Solution, root)

for i in result:
    print(i)