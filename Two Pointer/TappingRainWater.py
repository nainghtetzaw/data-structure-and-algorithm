from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r, res = 0, len(height) - 1, 0
        maxL, maxR = height[l], height[r]

        while l <= r:
            if maxL < maxR or maxL == maxR:
                if maxL - height[l] >= 0:
                    res += maxL - height[l]
                else:
                    maxL = height[l]
                
                l += 1
            elif maxR < maxL:
                if maxR - height[r] >= 0:
                    res += maxR - height[r]
                else:
                    maxR = height[r]

                r -= 1

        return res        