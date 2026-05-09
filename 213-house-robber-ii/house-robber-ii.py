class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rec(i, prev, zero):
            if i == len(nums) - 1:
                if not prev and not zero:
                    return nums[-1]
                else:
                    return 0
            if prev:
                return rec(i+1, False, zero)
            return max(nums[i] + rec(i+1, True, zero or i == 0), rec(i+1, False, zero))
        return rec(0, False, False)
        
        