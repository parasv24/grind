class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def rec(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                ans = rec(i + 1, j-1)
            else:
                ans = 1 + min(rec(i, j-1), rec(i+1, j))
            return ans
        return rec(0, len(s)-1)