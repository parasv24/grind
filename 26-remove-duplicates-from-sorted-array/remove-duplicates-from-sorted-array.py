class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        prev = -1000
        for i in range(0, len(nums)):
            if nums[i] != prev:
                nums[k] = nums[i]
                k += 1
            prev = nums[i]
        return k
