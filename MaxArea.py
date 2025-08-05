from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        for i, a in enumerate(height):
            r, j = len(height) - 1, height[len(height) - 1]
            
            while i < r:
                if maxArea < min(a, height[r]) * (r - i):
                    maxArea = min(a, height[r]) * (r - i)
                    
                r -= 1
                while i < r and height[r] <= j:
                    r -= 1 
        
        return maxArea
    
print(Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,7]))