class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2!= 0:
            return False
        target = sm // 2
        @cache
        def exists(cur_sum, target, i):
            if cur_sum == target:
                return True
            if i >= len(nums):
                return False
            if exists(cur_sum + nums[i], target, i+1) or exists(cur_sum, target, i+1):
                return True
            return False
        return exists(0, target, 0)
            
        