class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [-1]*n
        for i in range(n):
            dp[i] = triangle[n-1][i]
        
        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
        