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
        return m(n)