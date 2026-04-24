class Solution:
    def maxPathScore(self, grid, k):
        n, m = len(grid), len(grid[0])
        NEG = -10**15

        dp = [[[NEG] * (k + 1) for _ in range(m)] for _ in range(n)]

        start_cost = 1 if grid[0][0] > 0 else 0
        if start_cost <= k:
            dp[0][0][start_cost] = grid[0][0]

        for i in range(n):
            for j in range(m):
                for c in range(k + 1):
                    if dp[i][j][c] == NEG:
                        continue

                    # right
                    if j + 1 < m:
                        nc = c + (1 if grid[i][j+1] > 0 else 0)
                        if nc <= k:
                            dp[i][j+1][nc] = max(
                                dp[i][j+1][nc],
                                dp[i][j][c] + grid[i][j+1]
                            )

                    # down
                    if i + 1 < n:
                        nc = c + (1 if grid[i+1][j] > 0 else 0)
                        if nc <= k:
                            dp[i+1][j][nc] = max(
                                dp[i+1][j][nc],
                                dp[i][j][c] + grid[i+1][j]
                            )

        ans = max(dp[n-1][m-1])
        return ans if ans != NEG else -1