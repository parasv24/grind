class Solution(object):
    def fibrec(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fib(n-1) + self.fib(n-2) if n > 1 else n
    def fib(self, n):
        dp = [-1 for _ in range(100)]
        def fibmem(n):
            """
            :type n: int
            :rtype: int
            """
            if n < 2:
                dp[n] = n
                return dp[n]
            if dp[n] != -1:
                return dp[n]
            else:
                dp[n] = fibmem(n-1) + fibmem(n-2)
                return dp[n]
        def fibdp(n):
            """
            :type n: int
            :rtype: int
            """
            dp[0] = 0
            dp[1] = 1
            for i in range(2,100):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]
        print(fibdp(n))
        return fibmem(n)
        

        