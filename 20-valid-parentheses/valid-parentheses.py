class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        mp = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in mp.keys():
                stck.append(ch)
            elif len(stck) > 0 and mp[stck[-1]] == ch:
                stck.pop()
            else:
                return False
        return len(stck) == 0
        