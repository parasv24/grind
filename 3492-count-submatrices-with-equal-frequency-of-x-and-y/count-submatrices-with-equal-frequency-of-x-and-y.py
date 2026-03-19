class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n , m = len(grid) , len(grid[0])
        hasg = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            prev = 0
            flag = False
            for j in range(m):
                if grid[i][j] == "X":
                    grid[i][j] = 1
                    hasg[i][j] = 1
                if grid[i][j] == "Y":
                    grid[i][j] = -1
                if grid[i][j] == ".":
                    grid[i][j] = 0
                prev += grid[i][j]
                hasg[i][j] += hasg[i][j-1]
                jst_prev = grid[i-1][j] if i > 0 else 0
                grid[i][j] = prev + jst_prev
                hasg[i][j] += (hasg[i-1][j] if i > 0 else 0)
                if grid[i][j] == 0 and hasg[i][j] > 0:
                    ans += 1
        # print(grid)
        return ans

        