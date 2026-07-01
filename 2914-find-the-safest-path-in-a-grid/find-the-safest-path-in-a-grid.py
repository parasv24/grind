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

        nodes = [(v, k) for k, v in dist.items()]
        nodes.sort(reverse=True)
        parent = list(range(n*n))
        rank = [0] * (n * n)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            rx, ry = rank[px], rank[py]
            
            if px == py:
                return False
            if rx < ry:
                px, py = py, px
                rx, ry = ry, rx
            
            parent[py] = px
            if rx == ry:
                rank[px] += 1
            return True
        active = set()
        mini = 1000000
        
        for value, node in nodes:
            active.add(node)
            mini = min(mini, value)
            i , j = node // n, node % n
            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n and nx * n + ny in active:
                    union(nx*n + ny, node)
                
                if find(0) == find(n * n - 1):
                    return mini
        return -1
