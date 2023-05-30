class Solution:
    def fib(self, n: int) -> int:
        # REcursive
        def f(n):
            return f(n-1) + f(n-2) if n > 1 else n
        # return f(n)
    
        # Memo
        dp = [-1 for _ in range(n+1)]
        def m(n):
            if n <=1:
                return n
            if dp[n]!= -1:
                return dp[n]
            dp[n] = m(n-1) + m(n-2)
            return dp[n]
        # return m(n)
        
        if n <=1:
            return n
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]