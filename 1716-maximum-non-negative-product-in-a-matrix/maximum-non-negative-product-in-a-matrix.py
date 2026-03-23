class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        dp = [[[grid[i][j], grid[i][j]] for j in range(m)] for i in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                if i > 0 or j > 0:
                    arr = []
                    for ni, nj in [(i-1, j), (i, j-1)]:
                        if ni >= 0 and nj >= 0:
                            arr.append(grid[i][j] * dp[ni][nj][0])
                            arr.append(grid[i][j] * dp[ni][nj][1])
                    dp[i][j] = [max(arr), min(arr)]
        # print(dp)
        ans  = dp[n-1][m-1][0]
        return ans % 1000000007 if ans >= 0 else -1 
        # print(dp)
        # return dp[n-1][m-1] if dp[n-1][m-1] >= 0 else -1
        # @cache
        # def rec(i, j):
        #     if i >= n or j >= m:
        #         return None

        #     if i == n-1 and j == m-1:
        #         return (grid[i][j], grid[i][j])

        #     res = []

        #     for ni, nj in [(i+1, j), (i, j+1)]:
        #         child = rec(ni, nj)
        #         if child is None:
        #             continue

        #         cmax, cmin = child
        #         res.extend([
        #             grid[i][j] * cmax,
        #             grid[i][j] * cmin
        #         ])
        #     if not res:
        #         return None

        #     return (max(res), min(res))
        # ans, _ = rec(0,0)
        # return ans % 1000000007 if ans >= 0 else -1
            
