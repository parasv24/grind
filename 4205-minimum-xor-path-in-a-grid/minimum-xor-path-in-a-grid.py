class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        self.ans = 100000
        n , m = len(grid), len(grid[0])
        dp = [[set() for j in range(m)] for i in range(n)]
        def rec(i, j, cur):
            if i >= len(grid) or j >= len(grid[0]):
                return
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                cur ^= grid[i][j]
                if cur < self.ans:
                    self.ans = cur
                return
            rec(i+1, j, cur ^ grid[i][j])
            rec(i, j+1, cur ^ grid[i][j])
            return
        dp[0][0].add(grid[0][0])
        prev = grid[0][0]
        for i in range(1, n):
            prev ^= grid[i][0]
            dp[i][0].add(prev)
        
        prev = grid[0][0]
        for i in range(1, m):
            prev ^= grid[0][i]
            dp[0][i].add(prev)

        for i in range(1, n):
            for j in range(1, m):
                for el in dp[i-1][j]:
                    dp[i][j].add(el ^ grid[i][j])
                for el in dp[i][j-1]:
                    dp[i][j].add(el ^ grid[i][j])
        
        return min(dp[n-1][m-1])