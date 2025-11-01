import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []

    def addNum(self, num: int) -> None:
        self.minHeap.append(num)

    def findMedian(self) -> float:
        temp = [] + self.minHeap
        res = 0

        m = len(temp) // 2

        heapq.heapify(temp)

        for i in range(len(temp)):
            a = heapq.heappop(temp)

            if len(self.minHeap) % 2 == 0:
                if i == m or i == m - 1:
                    # print("a = ", a)
                    res += a
                if i == m:
                    return res / 2
            else:
                if i == m:
                    return a
