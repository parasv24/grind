class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        grid = [["." for _ in range(n)] for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()
        def back(i):
            if i > n:
                return
            if i == n:
                ans.append([ "".join(grid[di]) for di in range(n)])
                return
            for j in range(n):
                if j not in cols and (i+j) not in diag1 and (i-j) not in diag2:
                    grid[i][j] = "Q"
                    cols.add(j)
                    diag1.add(i+j)
                    diag2.add(i-j)
                    back(i+1)
                    grid[i][j] = "."
                    cols.remove(j)
                    diag1.remove(i+j)
                    diag2.remove(i-j)
            return
        back(0)
        return ans
            

                        

        