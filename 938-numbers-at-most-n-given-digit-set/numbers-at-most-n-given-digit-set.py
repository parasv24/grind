class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        @cache
        def rec(i, limit_on, started):
            # print(i, limit_on)
            if i == len(s):
                return int(started)
            limit = s[i] if limit_on else "9"
            ans = 0
            if not started:
                ans+= rec(i+1, limit_on and 0 == limit, started)
            for digit in digits:
                if digit <= limit:
                    ans += rec(i+1, limit_on and digit == limit, True)
            return ans
        return rec(0, True, False)