from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHm, columnHm, subBoxHm = defaultdict(list), defaultdict(list), defaultdict(list)
        r, c = 0, 0

        while True:
            if r >= 8 and c > 8:
                break
            
            if c == 9:
                r += 1
                c = 0
                continue
            
            n = board[r][c]
            if n == ".":
                c += 1
                continue

            if n in rowHm[r] or n in columnHm[c] or n in subBoxHm[(r//3, c//3)]:
                return False
            
            rowHm[r].append(n)
            columnHm[c].append(n)
            subBoxHm[(r//3, c//3)].append(n)
            c += 1

        return True

print(Solution.isValidSudoku(Solution, [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(Solution.isValidSudoku(Solution, [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))