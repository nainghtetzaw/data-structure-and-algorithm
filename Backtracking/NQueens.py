from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(cur, prev, taken, solution):
            if cur >= n:
                res.append(solution.copy())
                return
            
            for i in range(n):
                taken.append(i)

                if self.isValid(taken, i, cur):
                    temp = ""
                    for j in range(n):
                        temp = temp + ("Q" if i == j else ".")

                    solution.append(temp)
                    backtrack(cur + 1, i, taken, solution)
                    solution.pop()
                
                taken.pop()
        
        backtrack(0, -10, [], [])
        return res
                

    def isValid(self, taken, cur, level) -> bool:
        l = r = cur
        level -= 1

        while level >= 0:
            l = l - 1
            r = r + 1

            if l == taken[level] or r == taken[level] or cur == taken[level]:
                return False
            
            level -= 1

        return True