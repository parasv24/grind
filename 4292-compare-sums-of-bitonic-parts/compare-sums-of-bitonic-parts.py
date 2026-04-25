class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        i = 1
        left = nums[0]
        right = 0
        while i < len(nums) and nums[i] > nums[i-1]:
            left += nums[i]
            i += 1
        
        right = nums[i-1]
        while i < len(nums) and nums[i-1] > nums[i]:
            right += nums[i]
            i += 1
        if left == right:
            return -1
        return int(right > left)