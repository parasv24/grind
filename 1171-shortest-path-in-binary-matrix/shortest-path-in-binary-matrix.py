class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 0:
            queue = deque([(0, 0, 1)])
            grid[0][0] = 1
            while queue:
                x, y, dist = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return dist
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        newx, newy = x + dx, y + dy
                        if newx == x and newy == y:
                            continue
                        if 0 <= newx < n and 0 <= newy < n and grid[newx][newy] == 0:
                            queue.append((newx, newy, dist + 1))
                            grid[newx][newy] = 1
        return -1