class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def rec(i):
            if i == len(nums) - 1:
                return 0
            j = 1
            ans = len(nums)
            while j <= nums[i] and i + j < len(nums):
                ans = min(rec(i+j) + 1, ans)
                j += 1
            return ans
        return rec(0)


        