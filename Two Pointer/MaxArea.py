from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:        
        maxArea, l, r = 0, 0, len(height) - 1
        
        while l < r:
            if maxArea < min(height[l], height[r]) * (r - l):
                maxArea = min(height[l], height[r]) * (r - l)
            
            if height[l] == height[r] or height[l] > height[r]:
                r -= 1
            elif height[r] > height[l]:
                l += 1
        
        return maxArea
    
print(Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,1,7]))