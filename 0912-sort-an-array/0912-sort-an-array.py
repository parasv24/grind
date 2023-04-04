class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        ans = []
        while len(nums) > 0:
            ans.append(heappop(nums))
        return ans
