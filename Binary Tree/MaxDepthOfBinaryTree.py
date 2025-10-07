from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode], count: int = 0) -> int:
        if not root:
            return count

        return max(self.maxDepth(root.left, count + 1), self.maxDepth(root.right, count + 1))