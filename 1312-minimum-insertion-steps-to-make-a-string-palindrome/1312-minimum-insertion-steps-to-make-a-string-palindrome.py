class Solution:
    def minInsertions(self, s: str) -> int:
        rev = s[::-1]
        print(s, rev)
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        def f(i,j):
            if i >= n or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == rev[j]:
                dp[i][j] = 1 + f(i+1, j+1)
            else:
                dp[i][j] = max(f(i+1, j), f(i, j+1))
            return dp[i][j]
        
        x = f(0,0)
        # print(dp)
        return len(s) - x