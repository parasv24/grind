class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        # @cache
        # def rec(i, limit_on, started):
        #     if i == len(s):
        #         return int(started)
        #     limit = int(s[i]) if limit_on else 9

        #     ans = 0
        #     if not started:
        #         ans += rec(i+1, limit_on and 0 == limit, False)
        #     for j in range(1, limit + 1):
        #         ans += rec(i+1, limit_on and j == limit, True)
        #     return ans
        # return rec(0, True, False)
        @cache
        def rec(i, limit_on, started, has_zero):
            if i == len(s):
                return started and has_zero
            limit = int(s[i]) if limit_on else 9
            ans = 0
            for j in range(limit+1):
                if not started and j == 0:
                    ans += rec(i+1, limit_on and j == limit, False, False)
                else:
                    ans += rec(i+1, limit_on and j == limit,True, has_zero or j == 0)
            return ans
        return n - rec(0, True, False, False)


        