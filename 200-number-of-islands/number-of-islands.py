class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(i, j):
            grid[i][j] = '0'
            delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in delta:
                next_i, next_j = i + dx, j + dy
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == '1':
                    dfs(next_i, next_j)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count