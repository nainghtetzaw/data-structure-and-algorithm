from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, i) -> bool:
            if i == len(word):
                return True
            
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in path or word[i] != board[row][col]):
                return False
            
            path.add((row, col))
            res = (dfs(row + 1, col, i + 1) or
                    dfs(row - 1, col, i + 1) or
                    dfs(row, col + 1, i + 1) or
                    dfs(row, col - 1, i + 1))
            path.remove((row, col))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
            
        return False