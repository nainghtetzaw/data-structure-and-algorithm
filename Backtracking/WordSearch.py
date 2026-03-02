from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COLUMN, WORDLEN = len(board), len(board[0]), len(word)

        def bfs(r, c, index, stack):
            if index > WORDLEN - 1:
                return True

            if (r > ROW - 1 or r < 0
                or c > COLUMN - 1 or c < 0
                or board[r][c] != word[index]
                or (r, c) in stack):
                return False

            stack.append((r, c))
            result = (bfs(r + 1, c, index + 1, stack) 
                or bfs(r - 1, c, index + 1, stack)
                or bfs(r, c + 1, index + 1, stack)
                or bfs(r, c - 1, index + 1, stack))
            stack.pop()

            return result

        for r in range(ROW):
            for c in range(COLUMN):
                if bfs(r, c, 0, []):
                    return True
        
        return False