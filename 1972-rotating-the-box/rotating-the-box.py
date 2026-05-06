class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n, m = len(boxGrid), len(boxGrid[0])
        for i in range(n):
            prev = 0
            for j in range(m):
                if boxGrid[i][j] == '#':
                    boxGrid[i][j] = "."
                    prev += 1
                if j > 0 and boxGrid[i][j] == '*' and prev > 0:
                    k = j
                    while k > 0 and prev > 0:
                        boxGrid[i][k-1] = "#"
                        k -= 1
                        prev -= 1
                elif j == m - 1 and prev > 0:
                    k = j
                    while k >= 0 and prev > 0:
                        boxGrid[i][k] = "#"
                        k -= 1
                        prev -= 1
        newGrid = [["."] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                newGrid[j][n- i - 1] = boxGrid[i][j]
        return newGrid