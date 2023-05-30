class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1]*n for _ in range(n)]
        for i in range(n):
            dp[n-1][i] = matrix[n-1][i]
        
        for i in range(n-2, -1, -1):
            for j in range(n-1, -1, -1):
                x = y = 0
                if j + 1 > n - 1:
                    x = 10000000
                else:
                    x = dp[i+1][j+1]
                if j - 1 < 0:
                    y = 10000000
                else:
                    y = dp[i+1][j-1]
                dp[i][j] = matrix[i][j] + min(dp[i+1][j], x, y)
                
        return min(dp[0])