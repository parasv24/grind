class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @cache
        def rec(r1, c1, c2):
            if r1 == n:
                return 0
            ans = 0
            val = grid[r1][c1]
            if c1 != c2:
                val += grid[r1][c2]
            for dy1 in [-1, 0, 1]:
                for dy2 in [-1, 0, 1]:
                    if 0 <= c1 + dy1 <= m-1 and 0 <= c2 + dy2 <= m-1:
                        ans = max(ans, val + rec(r1+1, c1+dy1, c2+dy2))
            return ans
        return rec(0, 0, m-1)

