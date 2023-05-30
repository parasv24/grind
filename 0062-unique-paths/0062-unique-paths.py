class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def f(i,j):
        #     if i > m or j > n:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1
        #     return f(i+1, j) + f(i, j+1) 
        # return f(0,0)
        dp = [[-1 for j in range(n)] for i in range(m)]
        # print(dp)
        def mem(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = mem(i+1, j) + mem(i, j+1) 
            return dp[i][j]
        return mem(0,0)