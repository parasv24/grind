class Solution:
    def findIntegers(self, n: int) -> int:
        s = bin(n)[2:]
        @cache
        def rec(i, limit_on, prev_one):
            if i == len(s):
                return 1
            
            limit = int(s[i]) if limit_on else 1
            ans = 0
            for j in range(limit+1):
                if j == 1 and prev_one:
                    continue
                ans += rec(i+1, limit_on and j == limit, j == 1)
            return ans
        return rec(0, True, False)
        
            
