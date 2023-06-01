class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = []
        q.append([0,0, 1])
        grid[0][0] = 1
        while len(q) > 0:
            i, j, ans = q.pop(0)
            
            if i == n-1 and j == n-1:
                return ans
            
            dt = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
            
            for tup in dt:
                xi , xj= tup
                if 0<= i + xi<n and 0 <=j+xj < n and not grid[i+xi][j+xj]:
                    q.append([i+xi, j+xj, ans+1])
                    grid[i+xi][j+xj] = 1
        return -1
        