class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def rec(i):
            if i == len(nums)-1:
                return 0
            ans = -1
            for j in range(i+1, len(nums)):
                if -target <= nums[j] - nums[i] <= target:
                    small_ans = rec(j)
                    if small_ans != -1:
                        ans = max(ans, 1+small_ans)
            return ans
        return rec(0)
        
        