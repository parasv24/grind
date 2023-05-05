class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        delr = [-1 , 0 , 0 , 1]
        delc = [ 0 , -1, 1, 0]
        def dfs(i,j):
            vis[i][j] = 1
            for k in range(4):
                nrow = i + delr[k]
                ncol = j + delc[k]
                if 0 <= nrow < n and 0<= ncol <m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 0:
                    dfs(nrow, ncol)
        for i in range(m):
            if vis[0][i] == 0 and grid[0][i] == 0:
                dfs(0,i)
            if vis[n-1][i] == 0 and grid[n-1][i] == 0:
                dfs(n-1,i)
        for i in range(n):
            if vis[i][0] == 0 and grid[i][0] == 0:
                dfs(i,0)
            if vis[i][m-1] == 0 and grid[i][m-1] == 0:
                dfs(i,m-1)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == 0:
                    dfs(i,j)
                    ans += 1
        return ans
                    
