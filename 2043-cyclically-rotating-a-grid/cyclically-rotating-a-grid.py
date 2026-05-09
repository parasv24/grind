class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n , m = len(grid), len(grid[0])
        rows = [0, n-1, 0, m-1]
        while rows[0] < rows[1] and rows[2] < rows[3]:
            helper = []
            for i in range(rows[2], rows[3]):
                helper.append(grid[rows[0]][i])
            for i in range(rows[0], rows[1]):
                helper.append(grid[i][rows[3]])
            for i in range(rows[3], rows[2], -1):
                helper.append(grid[rows[1]][i])
            for i in range(rows[1], rows[0], -1):
                helper.append(grid[i][rows[2]])
            new_k = k % len(helper)
            j = new_k
            for i in range(rows[2], rows[3]):
                grid[rows[0]][i] = helper[j]
                j = (j + 1) % len(helper)
            for i in range(rows[0], rows[1]):
                grid[i][rows[3]] = helper[j]
                j = (j + 1) % len(helper)
            for i in range(rows[3], rows[2], -1):
                grid[rows[1]][i] = helper[j]
                j = (j + 1) % len(helper)
            for i in range(rows[1], rows[0], -1):
                grid[i][rows[2]] = helper[j]
                j = (j + 1) % len(helper)

            for i in range(len(rows)):
                if i % 2  == 0:
                    rows[i] += 1
                else:
                    rows[i] -= 1
        return grid
