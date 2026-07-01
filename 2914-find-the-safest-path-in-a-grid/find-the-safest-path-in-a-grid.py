class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dist = defaultdict(int)
        n = len(grid)
        thieves = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append((i, j))
                    dist[n * i + j] = 0
        queue = deque(thieves)
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            i, j = queue.popleft()
            d = dist[i * n + j]

            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx * n + ny] == 0 and grid[nx][ny] == 0:
                    dist[nx * n + ny] = d + 1
                    queue.append((nx, ny))

        dis = [-1] * (n*n)
        dis[0] = dist[0]
        heap = [(-dist[0], 0)]
        while heap:
            d, node = heapq.heappop(heap)
            d = -d

            if d < dis[node]:
                continue
            
            if node == n * n - 1:
                return d
            i , j = node // n, node % n
            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    val = min(d, dist[nx*n + ny])
                    if val > dis[nx *n + ny]:
                        heapq.heappush(heap, (-val, nx *n + ny))
                        dis[nx*n + ny] = val
        return -1
            
        