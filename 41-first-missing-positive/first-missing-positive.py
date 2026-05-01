class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = nums[i]
            while not (val <= 0 or val > len(nums) or nums[val-1] == val):
                temp = nums[val-1]
                nums[val-1] = val
                val = temp
        for i in range(len(nums)):
            if nums[i]!= i+1:
                return i+1
        return len(nums) + 1


        