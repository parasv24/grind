class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        leftr,leftc= 10000, 10000
        rightr, rightc = -1 , -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    leftr = min(leftr, i)
                    rightr = max(leftr, i)
                    leftc = min(leftc, j)
                    rightc = max(rightc, j)

        return (rightr - leftr + 1) * (rightc-leftc+1)