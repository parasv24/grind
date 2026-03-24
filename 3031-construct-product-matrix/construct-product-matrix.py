class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n , m = len(grid), len(grid[0])
        pref_prod = [1 for i in range(n*m)]
        suff_prod = [1 for i in range(n*m)]
        pre, suf = 1, 1
        MOD = 12345
        for i in range(n):
            for j in range(m):
                ni, nj = n - i - 1, m -j - 1
                pref_prod[(i * m) + j ]  = pre
                pre = (pre * (grid[i][j] % MOD)) % MOD
                suff_prod[(ni * m) + nj] = suf
                suf = (suf * (grid[ni][nj] % MOD)) % MOD
        ans = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = (pref_prod[(m * i) + j] * suff_prod[(m * i ) + j]) % MOD
        return ans

