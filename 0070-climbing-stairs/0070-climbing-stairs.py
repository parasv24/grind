class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        def rec(n):
            return rec(n-1) + rec(n-2) if n > 2 else n
        dp = [0 for i in range(n+1)]
        dp2 = [0 for i in range(n+1)]
        dp2[1], dp2[2] = 1 ,2
        dp[1] = 1
        dp[2] = 2
        def recM(n):
            if dp[n] != 0:
                return dp[n]
            dp[n] = recM(n-1) + recM(n-2)
            return dp[n]
        for i in range(3, n+1):
            dp2[i] = dp2[i-1] + dp2[i-2]
        print(recM(n))
        return dp2[n]