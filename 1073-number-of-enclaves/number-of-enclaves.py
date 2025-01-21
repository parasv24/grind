class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        delta = [[-1,0], [1,0], [0,1], [0,-1]]
        n , m = len(grid), len(grid[0])
        def dfs(i,j):
            grid[i][j] = 0
            ans = 1
            for xi, yi in delta:
                if 0<=i + xi < n and 0<= j+yi < m and grid[i+xi][j+yi] == 1:
                    ans += dfs(i+xi, j+yi)
            return ans
        marked = 0
        for i in range(m):
            if grid[0][i] == 1:
                marked += dfs(0,i)
            if grid[n-1][i] == 1:
                marked += dfs(n-1,i) 
        
        for i in range(n):
            if grid[i][0] == 1:
                marked += dfs(i,0)
            if grid[i][m-1] == 1:
                marked += dfs(i,m-1)
        print(marked)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans += 1
        return ans



        