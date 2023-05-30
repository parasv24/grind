class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1]*m for _ in range(n)]
        def mem(i,j):
            if i == n-1 and j == m-1:
                return int(obstacleGrid[i][j] == 0)
            if i >= n or j >=m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if obstacleGrid[i][j] == 1:
                return 0
            dp[i][j] = mem(i+1,j) + mem(i, j+1)
            return dp[i][j]
        return mem(0,0)
        
        