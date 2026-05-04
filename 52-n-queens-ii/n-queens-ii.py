class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diagonals1 = set()
        diagonals2 = set()
        def rec(i):
            if i == n:
                return 1
            
            ans = 0
            for j in range(n):
                if j not in cols and i+j not in diagonals1 and i-j not in diagonals2:
                    cols.add(j)
                    diagonals1.add(i+j)
                    diagonals2.add(i-j)
                    ans += rec(i+1)
                    cols.remove(j)
                    diagonals1.remove(i+j)
                    diagonals2.remove(i-j)
            return ans
        return rec(0)
