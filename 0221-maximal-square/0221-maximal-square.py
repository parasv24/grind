class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1]*m for _ in range(n)]
        maxi = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = int(matrix[i][j])
                maxi = max(maxi, dp[i][j])
        for i in range(1,n):
            for j in range(1,m):
                if dp[i][j] == 1:
                    dp[i][j] = int(dp[i][j]) + min(int(dp[i-1][j]), int(dp[i-1][j-1]), int(dp[i][j-1]))
                    maxi = max(maxi, dp[i][j])
        print(dp)
        return maxi * maxi
        