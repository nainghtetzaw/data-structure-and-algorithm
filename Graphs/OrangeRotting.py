class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while fresh > 0 and q:
            length = len(q)

            for i in range(length):
                qr, qc = q.popleft()

                for dr, dc in directions:
                    r, c = qr + dr, qc + dc

                    if (r in range(ROWS)
                        and c in range(COLS)
                        and grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
                
            time += 1
        
        return time if fresh == 0 else -1