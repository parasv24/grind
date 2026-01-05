class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            elif nums[i] == 0:
                nums[start] , nums[i] = nums[i], nums[start]
                if i == start:
                    i += 1
                start += 1
            else:
                i += 1
            print(i, start, end, nums)
        