class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        psums = [list(accumulate(grid[0])), list(accumulate(grid[1]))]
        ans2 = 10000000000
        for idx in range(len(grid[0])):
            if idx == 0:
                temp = psums[0][-1] - psums[0][0]
            else:
                temp = max(psums[0][-1] - psums[0][idx], psums[1][idx-1])
            if temp < ans2:
                ans2 = temp
        return ans2
        