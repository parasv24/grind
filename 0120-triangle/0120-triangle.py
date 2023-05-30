class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1]*n for _ in range(n)]
        def mem(i,j):
            if j > i:
                return 100000000
            if i == n-1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = triangle[i][j] + min(mem(i+1,j), mem(i+1, j+1))
            return dp[i][j]
        return mem(0,0)