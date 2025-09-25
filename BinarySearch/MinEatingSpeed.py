from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        l, r = 1, total
        k = 0

        while l <= r:
            m = (l + r) // 2
            estimateHour = Solution.calculateEstimateHour(self, m, piles)

            if estimateHour <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        
        return k

    def calculateEstimateHour(self, num: int, piles: List[int]) -> int:
        h = 0
        for i in piles:
            h += math.ceil(i / num)
        
        return h


# piles = [3,6,7,11]
piles = [312884470]
h = 312884469
# h = 8
print(Solution.minEatingSpeed(Solution, piles, h))