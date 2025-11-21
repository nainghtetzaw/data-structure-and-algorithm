class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, seen, distance):
            if (r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or (r, c) in seen
                or grid[r][c] == -1
                or (grid[r][c] == 0 and distance > 0)
                or grid[r][c] < distance):
                return
            
            seen.append((r,c))
            grid[r][c] = distance
            dfs(r + 1, c, seen, distance + 1)
            dfs(r - 1, c, seen, distance + 1)
            dfs(r, c - 1, seen, distance + 1)
            dfs(r, c + 1, seen, distance + 1)
            seen.pop()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    dfs(row, col, [], 0)