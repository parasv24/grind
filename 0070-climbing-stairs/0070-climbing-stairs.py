class Solution:
    def climbStairs(self, n: int) -> int:
        def f(n):
            return f(n-1) + f(n-2) if n > 2 else n
        
        dp = [-1 for _ in range(n+1)]
        
        def m(n):
            if n <= 2:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = m(n-1) + m(n-2)
            return dp[n]
        
        # Tabulation
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]