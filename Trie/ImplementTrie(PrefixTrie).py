class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.isLeaf = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord("a")

            if not cur.nodes[index]:
                cur.nodes[index] = TrieNode()
            
            cur = cur.nodes[index]
        
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            index = ord(c) - ord("a")

            if cur.nodes[index]:
                cur = cur.nodes[index]
            else:
                return False
            
        return cur.isLeaf
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            index = ord(c) - ord("a")

            if not cur.nodes[index]:
                return False
            
            cur = cur.nodes[index]

        return True