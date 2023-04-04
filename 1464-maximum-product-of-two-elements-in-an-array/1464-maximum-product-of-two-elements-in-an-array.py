import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq._heapify_max(nums)
        print(nums)
        a = heapq._heappop_max(nums)
        b = heapq._heappop_max(nums)
        return (a-1) * (b-1)