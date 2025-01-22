class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            ans = 1
        else:
            ans = 0
        delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        n , m = len(grid), len(grid[0])
        queue = deque([[0,0, ans]])
        grid[0][0] = -1
        while queue:
            x, y, z = queue.popleft()
            if x == n - 1 and y == m - 1:
                return z
            for i , j in delta:
                xj, yj = x + i, y + j
                if 0 <= xj <= n-1 and 0 <= yj <= m - 1 and grid[xj][yj] != -1:
                    if grid[xj][yj] == 1:
                        queue.append([xj, yj, z + 1])
                    else:
                        queue.appendleft([xj, yj, z])
                    grid[xj][yj] = -1
        return -1

        