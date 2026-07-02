class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        queue = deque([(0, 0, grid[0][0])])
        grid[0][0] = 2
        delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            i, j, unsafe_count = queue.popleft()

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                # print(unsafe_count, grid[-1][-1], health)
                return unsafe_count < health
            
            for di , dj in delta:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != 2:
                    if grid[ni][nj] == 0:
                        queue.appendleft((ni, nj, unsafe_count))
                    else:
                        queue.append((ni, nj, unsafe_count + 1))
                    grid[ni][nj] = 2
            
