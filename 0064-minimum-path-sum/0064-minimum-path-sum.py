class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def f(i,j):
            if i == n-1 and j == m- 1:
                return grid[i][j]
            if i >= n or j >= m:
                return 1000000000
            
            return grid[i][j] + min(f(i+1,j), f(i,j+1))
        
        dp = [[-1] * m for _ in range(n)]
        def mem(i,j):
            if i == n-1 and j == m- 1:
                return grid[i][j]
            if i >= n or j >= m:
                return 1000000000
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(mem(i+1,j), mem(i,j+1))
            return dp[i][j]
        return mem(0,0)
        