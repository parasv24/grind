class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        string = []
        i, j = n, m
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                string.append(text1[i-1])
                prevx = i -1
                prevy = j - 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    prevx, prevy = i-1, j
                else:
                    prevx, prevy = i, j-1
                
                if dp[i-1][j-1] > dp[prevx][prevy]:
                    prevx, prevy = i-1, j-1
            i, j = prevx, prevy
        ans = "".join(string)[::-1]
        return dp[n][m]
        