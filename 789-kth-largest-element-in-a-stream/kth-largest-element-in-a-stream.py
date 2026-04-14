class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_hp = []
        self.k = k
        for el in nums:
            heappush(self.min_hp, el)
            if len(self.min_hp) > k:
                heappop(self.min_hp)
        

    def add(self, val: int) -> int:
        heappush(self.min_hp, val)
        if len(self.min_hp) > self.k:
            heappop(self.min_hp)
        return self.min_hp[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)