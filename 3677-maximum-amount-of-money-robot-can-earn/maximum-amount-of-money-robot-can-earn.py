class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n, m = len(coins), len(coins[0])

        # approach 1 : basic recursion just did what they asked for
        @cache
        def maxp(i, j, kill):
            if i == n-1 and j == m-1:
                return coins[i][j] if coins[i][j] >= 0 else 0 if kill > 0 else coins[i][j]

            ans = -10000000
            for di, dj in [(i+1, j), (i, j+1)]:
                if di < n and dj < m:
                    ans = max(ans, coins[i][j] + maxp(di, dj, kill))
                    if kill > 0:
                        ans = max(ans, maxp(di, dj, kill-1))
            return ans
        # return maxp(0,0,2)

        # dp where state reperesents the total with skips done
        dp = [[[0, 0, 0] for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    if coins[i][j] >= 0:
                        dp[i][j] = [coins[i][j], coins[i][j], coins[i][j]]
                    else:
                        dp[i][j] = [coins[i][j], 0, 0]
                else:
                    for k in range(3):
                        best = -100000000
                        val = coins[i][j]
                        for di, dj in [(i-1, j), (i, j-1)]:
                            if di >= 0 and dj >= 0:
                                best = max(best, val + dp[di][dj][k])
                                if k > 0:
                                    best = max(best, dp[di][dj][k-1])
                        dp[i][j][k] = best
        return max(dp[n-1][m-1])
                            
