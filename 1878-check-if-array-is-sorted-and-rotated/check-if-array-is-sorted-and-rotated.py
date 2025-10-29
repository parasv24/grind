class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                cnt += 1
            if cnt >= 1 and nums[i+1] > nums[0]:
                return False
            if cnt > 1:
                return False
        return True