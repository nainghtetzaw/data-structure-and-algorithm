class MedianFinder:
    def __init__(self):
        self.small = [] # Max Heap
        self.large = [] # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            temp = -heapq.heappop(self.small)
            heapq.heappush(self.large, temp)

        if len(self.small) > len(self.large) + 1:
            temp = -heapq.heappop(self.small)
            heapq.heappush(self.large, temp)
        if len(self.large) > len(self.small) + 1:
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -temp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2