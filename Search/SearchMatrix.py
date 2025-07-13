from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixLeft, matrixRight = 0, len(matrix) - 1
        while matrixLeft <= matrixRight:
            matrixMid = (matrixLeft + matrixRight) // 2
            l, r = 0, len(matrix[matrixMid]) - 1
            
            while l <= r:
                m = (l + r) // 2

                if target < matrix[matrixMid][m]:
                    r = m - 1
                elif target > matrix[matrixMid][m]:
                    l = m + 1
                else:
                    return True
                
            if l < len(matrix[matrixMid]):
                matrixRight = matrixMid - 1
            else:
                matrixLeft = matrixMid + 1
            
        return False
    

matrix = [[1], [3], [5]]
print(Solution.searchMatrix(Solution, matrix, 1))