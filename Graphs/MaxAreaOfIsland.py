from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or grid[r][c] == 0):
                return
            
            self.area += 1
            grid[r][c] = 0
            self.res = max(self.res, self.area)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
                
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    print()
                    self.area = 0
                    dfs(row, col)
            
        return self.res