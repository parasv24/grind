class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        z = 0
        if grid[0][0] == 1:
            z = 1
        queue = deque([[0,0,z]])
        n,m = len(grid), len(grid[0])
        delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        grid[0][0] = -1
        while queue:
            x, y, z = queue.popleft()
            # print(x,y,z)
            if x == n - 1 and y == m - 1:
                if z < health:
                    return True
                else:
                    return False 
            for i , j in delta:
                xi, yi = x + i , y + j
                if 0 <= xi <= n-1 and 0 <= yi <= m-1 and grid[xi][yi] != -1:
                    if grid[xi][yi] == 0:
                        queue.appendleft([xi, yi,z])
                    else:
                        queue.append([xi, yi, z+1])
                    grid[xi][yi] = -1
        return False

        