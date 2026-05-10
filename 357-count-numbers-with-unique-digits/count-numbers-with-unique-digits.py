class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        new_n = pow(10, n)
        new_n -= 1
        s = str(new_n)
        def rec(i, limit_on, mask, started):
            if i == len(s):
                return 1
            limit = int(s[i]) if limit_on else 9
            ans = 0
            for j in range(limit+1):
                if not started and j == 0:
                    ans += rec(i+1, limit_on and j == limit, mask, False)
                elif mask & (1 << j) == 0:
                    ans += rec(i+1, limit_on and j == limit, mask | (1 << j), True)
            return ans
        return rec(0, True, 0, False)
                
        