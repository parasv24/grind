class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = int(1e9)
        distance = [[INF]* m for i in range(n)]
        distance[0][0] = 0
        delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dq = deque()
        dq.appendleft([0,0])
        while dq:
            x, y = dq.popleft()
            val = grid[x][y]
            for idx, pair in enumerate(delta):
                i , j = pair
                cost = 0 if val == idx + 1 else 1
                if 0 <= x + i <= n-1 and 0 <= y + j <= m-1 and distance[x][y] + cost < distance[x+i][y+j]:
                    distance[x+i][y+j] = min(distance[x+i][y+j], distance[x][y]+cost)
                    if idx + 1 == val:
                        dq.appendleft([x+i, y+j])
                    else:
                        dq.append([x+i, y+j])
        return distance[n-1][m-1]

        