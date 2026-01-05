class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        j = len(nums) - 2
        while j >= 0:
            if nums[j+1] > nums[j]:
                break
            j -= 1
        min , idx = 1000000, -1

        if j!= -1:
            for i in range(j+1, len(nums)):
                if nums[i] > nums[j] and nums[i] <= min:
                    min = nums[i]
                    idx = i

            nums[idx], nums[j] = nums[j], nums[idx]
        start, end = j + 1, len(nums) - 1
        # print(start, end)
        # print(nums)
        while start < end:
            nums[start], nums[end] = nums[end], nums[start] 
            start += 1
            end -= 1
        print(nums, nums[j+1:])



        