class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        delta = [[-1,0], [1,0], [0,1],[0, -1]]
        n, m = len(grid), len(grid[0])
        def dfs(r,c):
            ans = grid[r][c]
            grid[r][c] = 0
            for x, y in delta:
                if 0 <= r+x <= n-1 and 0<= c+y <= m-1 and grid[r+x][c+y] > 0:
                    ans += dfs(r+x, c+y)
            return ans
        maxi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    maxi = max(maxi, dfs(i,j))
        return maxi



        