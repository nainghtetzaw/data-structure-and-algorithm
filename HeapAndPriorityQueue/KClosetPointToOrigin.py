import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = [pow(i[0], 2) + pow(i[1], 2) for i in points]

        heapq.heapify(minHeap)

        smallestVals = heapq.nsmallest(k, minHeap)
        for i in points:
            if (pow(i[0], 2) + pow(i[1], 2) in smallestVals):
                res.append(i)

            if len(res) == k:
                break

        return res