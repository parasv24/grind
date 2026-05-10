class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        @cache
        def rec(i, limit_on):
            if i == len(s):
                return [1, 0]
            limit = int(s[i]) if limit_on else 9

            total = 0
            ans = 0
            for j in range(0, limit+1):
                small_total, small_ans = rec(i+1, limit_on and j == limit)

                if j == 1:
                    ans += small_total
                ans += small_ans
                total += small_total
            return [total, ans]
        return rec(0, True)[1]

