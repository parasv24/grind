class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mp = [0] * 10001
        for num in nums:
            mp[num] += 1
        def f(i):
            if i >= 10001:
                return 0
            return max(mp[i] * i + f(i+2), f(i+1))
        dp = [-1] * 10001
        def m(i):
            if i >= 10001:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(mp[i] * i + m(i+2), m(i+1))
            return dp[i]
        # return m(0)
        dp[10000] = mp[10000] * 10000
        dp[9999] = max(mp[9999] * 9999, dp[10000]) 
        for i in range(9998, -1, -1):
            dp[i] = max(mp[i] * i + dp[i+2] , dp[i+1])
        return dp[0]