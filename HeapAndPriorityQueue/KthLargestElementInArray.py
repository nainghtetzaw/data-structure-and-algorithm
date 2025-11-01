import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-i for i in nums]
    
        heapq.heapify(maxHeap)
        res = 0
        while k != 0:
            res = -heapq.heappop(maxHeap)
            k -= 1
        return res
        
    
arr = [3,4,1,4,5,6,3]
res = []
heapq.heapify(arr)
for i in range(len(arr)):
    res.append(heapq.heappop(arr))
print(res)