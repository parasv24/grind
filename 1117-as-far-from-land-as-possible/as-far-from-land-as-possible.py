class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append([i,j])
        lvl = -1
        delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            new_q = []
            for x, y in queue:
                for i , j in delta:
                    xi , yi = x + i , y + j
                    if 0 <= xi <= n-1 and 0 <= yi <= m-1 and grid[xi][yi] == 0:
                        new_q.append([xi,yi])
                        grid[xi][yi] = 1
            queue = new_q
            lvl += 1
        return lvl if lvl > 0 else -1


        