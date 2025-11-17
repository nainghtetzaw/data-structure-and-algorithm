class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            index = ord(c) - ord("a")
            
            if not cur.nodes[index]:
                cur.nodes[index] = TrieNode()
                
            cur = cur.nodes[index]

        cur.isLast = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(i, cur):
            if not cur:
                return False

            if i >= len(word):
                return cur.isLast            
            
            if word[i] == ".":
                for index in range(26):
                    if not cur.nodes[index]:
                        continue
                        
                    if dfs(i + 1, cur.nodes[index]):
                        return True
            else:
                index = ord(word[i]) - ord("a")

                if cur.nodes[index]:
                    if dfs(i + 1, cur.nodes[index]):
                        return True
        
        if dfs(0, cur):
            return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)