class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # brute de force
        n = len(grid)

        # def rec(i, j, trip):
        #     if i == 0 and j == 0 and trip == 1:
        #         return grid[0][0]

        #     cherry = 0
        #     picked = False

        #     if grid[i][j] == 1:
        #         cherry = 1
        #         grid[i][j] = 0
        #         picked = True

        #     if i == n - 1 and j == n - 1 and trip == 0:
        #         ans = rec(n - 1, n - 1, 1)

        #         if picked:
        #             grid[i][j] = 1

        #         return cherry + ans

        #     best = float("-inf")

        #     if trip == 0:
        #         if i + 1 < n and grid[i + 1][j] != -1:
        #             best = max(best, rec(i + 1, j, 0))

        #         if j + 1 < n and grid[i][j + 1] != -1:
        #             best = max(best, rec(i, j + 1, 0))

        #     else:
        #         if i - 1 >= 0 and grid[i - 1][j] != -1:
        #             best = max(best, rec(i - 1, j, 1))

        #         if j - 1 >= 0 and grid[i][j - 1] != -1:
        #             best = max(best, rec(i, j - 1, 1))

        #     if picked:
        #         grid[i][j] = 1

        #     return cherry + best

        # if grid[0][0] == -1 or grid[-1][-1] == -1:
        #     return 0

        # return max(rec(0, 0, 0), 0)

        @cache
        def rec(r1, c1, r2, c2):
            if r1 == n - 1 and c1 == n - 1 and r2 == n-1 and c2 == n-1:
                return grid[n-1][n-1]
            if r1 >= n or r2 >= n or c1 >= n or c2 >=n:
                return -1000000000
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -1000000000
            best = max(rec(r1+1, c1, r2+1, c2), rec(r1, c1+1, r2+1, c2), rec(r1, c1+1, r2, c2+1), rec(r1+1, c1, r2, c2+1))
            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]
            return best + cherries
        return max(rec(0, 0, 0, 0), 0)
            