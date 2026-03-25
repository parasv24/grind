class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n,m = len(grid), len(grid[0])
        row_sums = [sum(grid[i]) for i in range(n)]
        total = sum(row_sums)
        col_sums = [sum([grid[i][j] for i in range(n)]) for j in range(m)]
        prev = 0
        for i in range(n):
            prev += row_sums[i]
            if total - prev == prev:
                return True
        prev = 0
        for i in range(m):
            prev += col_sums[i]
            if total - prev == prev:
                return True
        return False
        