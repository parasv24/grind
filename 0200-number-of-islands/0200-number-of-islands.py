class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        delr = [ -1 , 0 , 0 , 1]
        delc = [ 0, -1, 1, 0]
        def dfs(r , c):
            vis[r][c] = 1
            for i in range(0, 4):
                nr = r + delr[i]
                nc = c + delc[i]
                if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and grid[nr][nc] == '1':
                    dfs(nr, nc)
        count = 0

        for i in range(0, n):
            for j in range(0, m):
                if vis[i][j] == 0 and grid[i][j] == '1':
                    queue = []
                    queue.append([i, j])
                    vis[i][j] = 1
                    while len(queue) > 0:
                        r, c = queue[0]
                        vis[r][c] = 1
                        queue.pop(0)
                        for k in range(0, 4):
                            nr = r + delr[k]
                            nc = c + delc[k]
                            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and grid[nr][nc] == '1':
                                queue.append([nr, nc])
                                vis[nr][nc] = 1
                    # dfs(i, j)
                    count += 1
        return count