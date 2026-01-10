class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def lcs(str1, str2, i, j):
            if i >= len(str1) or j >= len(str2):
                return 0
            ans = 0
            if str1[i] == str2[j]:
                ans = 1 + lcs(str1, str2, i+1, j+1)
            ans2 = lcs(str1, str2, i+1, j)
            ans3 = lcs(str1, str2, i, j+1)
            return max([ans, ans2, ans3])
        return lcs(text1, text2, 0, 0)
        