class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            prevRect, nextRect = i, i + 1
            area = 0
            
            while prevRect >= 0:
                if heights[prevRect] < heights[i]:
                    break
                area += heights[i]
                prevRect -= 1
                
            
            while nextRect < len(heights):
                if heights[nextRect] < heights[i]:
                    break
                area += heights[i]
                nextRect += 1
            
            res = max(res, area)
        
        return res
                     