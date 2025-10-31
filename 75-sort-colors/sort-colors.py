class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx, i , j = 0, 0, len(nums) - 1
        while idx < len(nums):
            if nums[idx] == 0 and i < idx:
                nums[i], nums[idx] = nums[idx], nums[i]
                i += 1
                idx -= 1
            elif nums[idx] == 2 and idx < j:
                nums[j], nums[idx] = nums[idx], nums[j]
                j -= 1
                idx -= 1
            idx += 1
        
        
        