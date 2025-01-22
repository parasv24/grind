class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])
        delta = [[-1, 0], [1, 0], [0,1], [0,-1]]
        def dfs(i, j):
            grid[i][j] = 2
            bfs_queue.append([i,j])
            for x, y in delta:
                xi, yj = x+ i , y + j
                if 0 <= xi <= n-1 and 0<= yj <= m-1 and grid[xi][yj] == 1:
                    dfs(xi,yj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    source = [i, j]
                    break

        bfs_queue = []
        dfs(source[0], source[1])
        distance = 0

        while bfs_queue:
            new_bfs = []
            for x, y in bfs_queue:
                for cur_x, cur_y in [
                    (x + 1, y),
                    (x - 1, y),
                    (x, y + 1),
                    (x, y - 1),
                ]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1
            bfs_queue = new_bfs
            distance += 1
        return distance
                
        




        