class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def can_place(i, j, grid):
            for k in range(0, n):
                if grid[k][j] == "Q":
                    return False
                if grid[i][k] == "Q":
                    return False
            
            di , dj = i, j
            while di >= 0 and dj >=0:
                if grid[di][dj] == "Q":
                    return False
                di -= 1
                dj -= 1
            
            di , dj = i, j
            while di >=0 and dj < n:
                if grid[di][dj] == "Q":
                    return False
                di -= 1
                dj += 1
            
            return True

        def back(i, grid):
            if i > n:
                return
            if i == n:
                cp_grid = ["" for _ in range(n)]
                for di in range(n):
                    cp_grid[di] = "".join(grid[di])
                ans.append(cp_grid)
                return
            for j in range(n):
                if can_place(i, j, grid):
                    grid[i][j] = "Q"
                    back(i+1, grid)
                    grid[i][j] = "."
            return
        back(0, [["." for _ in range(n)] for _ in range(n)])
        return ans
            

                        

        