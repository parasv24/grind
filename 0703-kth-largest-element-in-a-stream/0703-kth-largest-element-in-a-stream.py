import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.heap = []
        if k <= len(nums):
            self.heap = nums[: k]
            heapq.heapify(self.heap)
            for i in range(k, len(nums)):
                if nums[i] > self.heap[0]:
                    heapq.heapreplace(self.heap, nums[i])
        else:
            self.heap = nums
            heapq.heapify(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
        if not self.heap:
            self.heap = []
            heapq.heappush(self.heap, val)
        elif self.heap and len(self.heap) < self.K:
            print(self.K, self.heap)
            heapq.heappush(self.heap, val) 
            print(self.heap)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)