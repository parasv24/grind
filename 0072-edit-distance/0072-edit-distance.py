class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1] * m for _ in range(n)]

        def f(i, j):
            if i >= n:
                return m - j
            if j >= m:
                return n-i
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = 0 + f(i + 1, j + 1)
            else:
                dp[i][j] = 1 + min(f(i, j+1), f(i+1, j), f(i+1, j+1))
            return dp[i][j]

        x = f(0, 0)
        print(x)
        return x
        