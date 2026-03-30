class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def rec(start):
            if start == len(s):
                return -1
            ans = 1000000
            for i in range(start, len(s)):
                cur = s[start: i +1]
                if cur == cur[::-1]:
                    ans = min(ans, 1 + rec(i+1))
            return ans
        return rec(0)