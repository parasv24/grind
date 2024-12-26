class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def target_sum(i, val):
            if val == 0 and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            return target_sum(i+1,val + nums[i]) + target_sum(i+1, val - nums[i])
        return target_sum(0, target)
        