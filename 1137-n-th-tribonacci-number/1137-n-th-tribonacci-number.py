class Solution(object):
    def tribonacci(self, n):
        dp = [-1 for _ in range(100)]

        def tribonaccirec(n):
            """
            :type n: int
            :rtype: int
            """
            return tribonaccirec(n - 1) + tribonaccirec(n - 2) + tribonaccirec(n - 3) if n > 2 else int(n != 0)
        def tribonaccimem(n):
            """
            :type n: int
            :rtype: int
            """
            if n < 3:
                dp[n] = int(n != 0)
                return dp[n]
            if dp[n] != -1:
                return dp[n]
            else:
                dp[n] = tribonaccimem(n-1) + tribonaccimem(n-2) + tribonaccimem(n-3)
                return dp[n]
        def tribonaccidp(n):
            """
            :type n: int
            :rtype: int
            """
            dp[0] = 0
            dp[1] = 1
            dp[2] = 1
            for i in range(3,100):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            return dp[n]
        print(tribonaccidp(n))
        return tribonaccimem(n)

