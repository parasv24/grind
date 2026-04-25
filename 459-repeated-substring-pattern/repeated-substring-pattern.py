class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lps = [0] * len(s)
        i = 1
        length = 0
        while i < len(s):
            if s[i] == s[length]:
                lps[i] = length + 1
                length += 1
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    i += 1
        return length > 0 and len(s) % (len(s) - length) == 0