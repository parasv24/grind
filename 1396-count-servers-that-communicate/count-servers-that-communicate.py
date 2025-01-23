class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            grid[i][j] = 2
            cnt = 1
            for k in range(len(grid)):
                if grid[k][j] == 1:
                    cnt += dfs(k,j)
            for k in range(len(grid[0])):
                if grid[i][k] == 1:
                    cnt += dfs(i,k)
            return cnt
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = dfs(i,j)
                    if temp != 1:
                        ans += temp
        return ans

        