class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7
        def get_count(s):
            @cache
            def rec(i, limit_on , digit_sum):
                if i == len(s):
                    return  int(min_sum <= digit_sum <= max_sum)
                
                limit = int(s[i]) if limit_on else 9
                ans = 0
                for j in range(limit+1):
                    ans += rec(i+1, limit_on and j == limit, digit_sum + j)
                return ans % MOD
            return rec(0, True, 0)
        sm = 0
        for i in num1:
            sm += int(i)
        return (get_count(num2) - get_count(num1) + int(min_sum <= sm <= max_sum)) % MOD

        