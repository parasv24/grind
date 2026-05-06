class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # def rec(i, arr):
        #     if i == len(s) and j == len(t):
        #         return int("".join(arr) == t)
        #     return rec(i+1, arr) + rec(i+1, arr + [s[i]])
        # return rec(0, [])
        @cache
        def rec(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] != t[j]:
                return rec(i+1, j)
            return rec(i+1, j) + rec(i+1, j+1)
        return rec(0, 0)
        