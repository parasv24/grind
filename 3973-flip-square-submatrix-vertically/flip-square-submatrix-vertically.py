class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        x2 = x + k - 1
        while x2 > x:
            for i in range(y, y+k):
                grid[x][i], grid[x2][i] = grid[x2][i], grid[x][i]
            x += 1
            x2 -= 1
        return grid

        