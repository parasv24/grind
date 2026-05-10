class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        def get_counts(s):
            s = s.zfill(101)
            MOD = 10 ** 9 + 7
            @cache
            def rec(i, limit_on, prev, started):
                if i == len(s):
                    return 1
                limit = int(s[i]) if limit_on else 9
                ans = 0
                for j in range(limit+1):
                    if not started and j == 0:
                        ans += rec(i+1, limit_on and j == limit, prev, False)
                    elif not started or abs(prev - j) == 1:
                        ans += rec(i+1, limit_on and j == limit, j, True)
                return ans % MOD
            return rec(0, True, -1, False)
        highs = get_counts(high)
        lows = get_counts(low)
        valid = True
        for i in range(1, len(low)):
            if abs(int(low[i]) - int(low[i-1])) != 1:
                valid = False
                break
        return (highs - lows + int(valid)) % (10 ** 9 + 7)

                
        