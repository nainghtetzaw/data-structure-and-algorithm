import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            minHeap.append([(pow(x, 2) + pow(y, 2)), x, y])
        
        res = []
        heapq.heapify(minHeap)
        while k != 0:
            point, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res