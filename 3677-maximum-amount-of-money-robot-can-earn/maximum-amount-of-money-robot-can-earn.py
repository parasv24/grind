class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n, m = len(coins), len(coins[0])

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
        return maxp(0,0,2)