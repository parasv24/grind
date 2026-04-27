class Solution:
    def shortestPalindrome(self, s: str) -> str:
        combined = s + "#" + s[::-1]
        i = 1
        length = 0
        lps = [0] * len(s)
        while i < len(combined):
            if combined[i] == combined[length]:
                length += 1
                if i < len(s):
                    lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    i += 1
        idx = len(s) - length
        return s[::-1][:idx] + s