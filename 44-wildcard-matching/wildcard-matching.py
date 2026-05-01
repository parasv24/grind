class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        pattern = [p[0]]
        for i in range(1, len(p)):
            if p[i] == p[i-1] == "*":
                pass
            else:
                pattern.append(p[i])
        p = "".join(pattern)
        @cache
        def rec(i, j):
            if i == len(s) and j == len(p):
                return True
            
            if i == len(s):
                if p[j] == "*":
                    return rec(i, j+1)
                return False
            
            if j == len(p):
                return False

            if s[i] == p[j] or p[j] == "?":
                return rec(i+1, j + 1)
            if p[j] == "*":
                return rec(i+1, j) or rec(i+1, j+1) or rec(i, j+1)
            
            return False
        return rec(0,0)
        