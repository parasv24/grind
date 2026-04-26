class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        vis = set()
        queue = deque()
        n , m = len(grid), len(grid[0])
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(n):
            for j in range(m):
                if not (i, j) in vis:
                    vis.add((i,j))
                    queue.append([i,j, -1, -1])
                    while queue:
                        x, y, px, py = queue.popleft()
                        for dx, dy in delta:
                            nx , ny = x + dx , y + dy
                            if  0 <= nx < n and 0 <= ny < m:
                                if grid[nx][ny] == grid[x][y] and not (nx == px and ny == py):
                                    if (nx, ny) in vis:
                                        return True
                                    vis.add((nx, ny))
                                    queue.append([nx, ny, x, y])
        return False
