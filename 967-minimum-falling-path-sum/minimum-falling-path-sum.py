class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        @cache
        def rec(i, j):
            val = matrix[i][j]
            if i == n-1:
                return val
            ans = float('inf')
            for k in range(j-1, j+2):
                if 0 <= k <= m-1:
                    ans = min(ans, rec(i+1, k))
            return ans + val
        ans = float('inf')
        for j in range(m):
            ans = min(ans, rec(0, j))
        return ans