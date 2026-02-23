class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = pow(2, k)
        mp = [0] * n
        i = k - 1
        while i < len(s):
            num = int(s[i-k+1: i+1], 2)
            mp[num] = 1
            i+=1
        return sum(mp) == n