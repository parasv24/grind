class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def f(i):
            if i >= n:
                return 0
            return max(nums[i] + f(i+2), f(i+1))
        # return f(0)
        dp = [-1 for _ in range(n+1)]
        def m(i):
            if i >= n:
                return 0
            if dp[i]!= -1:
                return dp[i]
            dp[i] = max(nums[i] + m(i+2), m(i+1))
            return dp[i]
        return m(0)