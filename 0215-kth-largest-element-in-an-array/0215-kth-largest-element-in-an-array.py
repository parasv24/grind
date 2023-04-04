class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for i in range(k,len(nums)):
            if nums[i] > heap[0]:
                heapreplace(heap, nums[i])
        return heap[0]
        