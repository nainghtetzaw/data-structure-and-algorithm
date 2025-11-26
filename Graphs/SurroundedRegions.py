from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(r, c, visited):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or (r, c) in visited
                or board[r][c] == "X"):
                return
            
            visited.add((r,c))
            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)
        
        for c in range(COLS):
            dfs(0, c, seen)
            dfs(ROWS - 1, c, seen)

        for r in range(ROWS):
            dfs(r, 0, seen)
            dfs(r, COLS - 1, seen)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in seen:
                    board[r][c] = "X"
            
                