class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        run_nums = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            run_nums[i] = nums[i - 1] + run_nums[i -1]
        return run_nums[1:] 
            

