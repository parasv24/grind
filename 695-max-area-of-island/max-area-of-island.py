class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    stck = [(i, j)]
                    grid[i][j]=0
                    while stck:
                        i, j = stck.pop()
                        area += 1
                        for dx, dy in delta:
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                                stck.append((nx, ny))
                                grid[nx][ny] = 0
                    ans = max(ans, area)
        return ans
        