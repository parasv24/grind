class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        hapn = False
        for i in range(0, len(s)):
            if s[i] == "1":
                if not hapn:
                    hapn = True
                elif s[i-1] == "1":
                    pass
                else:
                    return False
        return True
        