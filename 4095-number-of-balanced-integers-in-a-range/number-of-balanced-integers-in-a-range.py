class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def count(s):
            s = str(s)
            @cache
            def rec(i, limit_on, diff):
                if i == len(s):
                    return diff == 0

                limit = int(s[i]) if limit_on else 9
                ans = 0
                for j in range(limit+1):
                    diff_new = diff + j if i % 2 != 0 else diff - j
                    ans += rec(i+1, limit_on and j == limit, diff_new)
                return ans
            return rec(0, True, 0)
        odd, even = 0,0
        for idx, i in enumerate(str(low)):
            if idx % 2 == 0:
                even = even + int(i)
            else:
                odd = odd + int(i)
        return count(high) - count(low) + int(odd == even)



        