class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache
        def rec(i, limit_on, started, mask):
            if i == len(s):
                return int(started)
            limit = int(s[i]) if limit_on else 9
            ans = 0
            for j in range(limit+1):
                if mask & (1 << j) == 0:
                    if not started and j == 0:
                        ans += rec(i+1, limit_on and j == limit, False, mask)
                    else:
                        ans += rec(i+1, limit_on and j == limit, True, mask | (1 << j))
            return ans
        return rec(0, True, False, 0)
