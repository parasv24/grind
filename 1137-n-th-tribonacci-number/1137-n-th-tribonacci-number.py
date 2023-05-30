class Solution:
    def tribonacci(self, n: int) -> int:
        def f(n):
            return f(n-1)+f(n-2)+f(n-3) if n > 2 else int(n != 0)
        # return f(n)
        
        dp = [-1 for _ in range(n+1)]
        def m(n):
            if n < 3:
                return int(n!=0)
            if dp[n]!= -1:
                return dp[n]
            dp[n]=m(n-1)+m(n-2)+m(n-3)
            return dp[n]
        return m(n)
        