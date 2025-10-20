# Definition for a binary tree node.
from typing import Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        self.res = ""
        def recursive(root):
            if not root:
                self.res += "null,"
                return
            self.res += str(root.val) + ","
            recursive(root.left)
            recursive(root.right)

        recursive(root)
        return self.res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        dataList = data.split(',')
        self.i = 0

        def dfs() -> Optional[TreeNode]:
            if dataList[self.i] == "null":
                self.i += 1
                return None
            
            node = TreeNode(int(dataList[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()