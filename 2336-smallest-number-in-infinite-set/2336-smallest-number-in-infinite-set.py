import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.lis = [i for i in range(1, 1001)]
        heapq.heapify(self.lis)
        

    def popSmallest(self) -> int:
        return heapq.heappop(self.lis)

    def addBack(self, num: int) -> None:
        if num not in self.lis:
            heapq.heappush(self.lis, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)