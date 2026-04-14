class MedianFinder:

    def __init__(self):
        self.mx_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.mx_heap, -num)
        heappush(self.min_heap, -heappop(self.mx_heap))
        if len(self.min_heap) > len(self.mx_heap):
            heappush(self.mx_heap, -heappop(self.min_heap))
    def findMedian(self) -> float:
        if (len(self.mx_heap) + len(self.min_heap)) % 2 == 0:
            return (-self.mx_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.mx_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()