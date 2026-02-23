class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = pow(2, k)
        seen = set()
        i = k - 1
        while i < len(s):
            seen.add(s[i-k+1: i+1])
            i+=1
        return len(seen) == n