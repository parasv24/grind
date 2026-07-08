class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # SQRT DECOMPOSITION : T.L.E
        # Sparse Table : done
        # prefix array
        n = len(s)
        MOD = 10 ** 9 + 7
        pre = [(0, 0, 0)]
        for i in range(0, n):
            prea, sma, lena = pre[-1]
            if s[i] != "0":
                prea = (prea * 10 + int(s[i])) % MOD
                sma = (sma + int(s[i])) % MOD
                lena += 1
            pre.append((prea, sma, lena))
        ans = []
        for l, r in queries:
            prea, sma, lena = pre[l]
            preb, smb, lenb = pre[r+1]
            sm = smb - sma
            prefix = (preb - prea * pow(10, lenb - lena, MOD)) % MOD
            ans.append((prefix * sm) % MOD )
        return ans