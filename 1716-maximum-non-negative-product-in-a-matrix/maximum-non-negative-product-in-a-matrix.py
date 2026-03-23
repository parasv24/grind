class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        dp = [[grid[i][j] for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                ans1 = grid[i][j] * dp[i-1][j]
                ans2 = grid[i][j] * dp[i][j-1]
                dp[i][j] = max(ans1, ans2)
        # print(dp)
        # return dp[n-1][m-1] if dp[n-1][m-1] >= 0 else -1
        @cache
        def rec(i, j):
            if i >= n or j >= m:
                return None

            if i == n-1 and j == m-1:
                return (grid[i][j], grid[i][j])

            res = []

            for ni, nj in [(i+1, j), (i, j+1)]:
                child = rec(ni, nj)
                if child is None:
                    continue

                cmax, cmin = child
                res.extend([
                    grid[i][j] * cmax,
                    grid[i][j] * cmin
                ])
            if not res:
                return None

            return (max(res), min(res))
        ans, _ = rec(0,0)
        return ans % 1000000007 if ans >= 0 else -1
            
