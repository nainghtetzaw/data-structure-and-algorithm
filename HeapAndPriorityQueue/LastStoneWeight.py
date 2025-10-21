import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for i in stones:
            maxheap.append(-i)

        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            y, x = -heapq.heappop(maxheap), -heapq.heappop(maxheap)

            if x != y:
                heapq.heappush(maxheap, -(y - x))
            
        return -maxheap[0] if maxheap else 0