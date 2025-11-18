class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        COLS, ROWS = len(board), len(board[0])
        res = []

        def dfs(i, a, row, column, stack):
            if i >= len(a):
                return True
            
            if ((row, column) in stack
                or (column < 0) 
                or (column >= COLS)
                or (row < 0)
                or (row >= ROWS)
                or (a[i] != board[column][row])):
                return False
            
            stack.append((row, column))
            if (dfs(i + 1, a, row - 1, column, stack)
                or dfs(i + 1, a, row + 1, column, stack)
                or dfs(i + 1, a, row, column + 1, stack)
                or dfs(i + 1, a, row, column - 1, stack)):
                return True
            stack.pop()
            return False

            
        for i in words:
            flag = False
            for column in range(len(board)):
                if flag:
                    break
                for row in range(len(board[column])):
                    if dfs(0, i, row, column, []):
                        res.append(i)
                        flag = True
                        break

        
        return res