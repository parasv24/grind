class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # SQRT DECOMPOSITION : T.L.E
        # Sparse Table
        n = len(s)
        MOD = 10 ** 9 + 7
        pow10 = [pow(10, i, MOD) for i in range(n+1)]
        logn = n.bit_length()
        sparse_table = [[] for _ in range(logn)]

        for j in range(0, n):
            length = 1 if s[j] != "0" else 0
            sparse_table[0].append((int(s[j]), int(s[j]), length))

        for i in range(1, logn):
            span_size = pow(2, i-1)
            for j in range(0, n - span_size - span_size + 1):
                prefa, sma, lena = sparse_table[i-1][j]
                prefb, smb, lenb = sparse_table[i-1][j + span_size]
                mul = pow10[lenb]
                sparse_table[i].append(((prefa * mul + prefb) % MOD, (sma + smb) % MOD, lena + lenb))

        # print(sparse_table)
        ans = []
        for l, r in queries:
            diff = r - l + 1
            prefa, sma, lena = 0, 0 , 0
            while diff > 0:
                span = diff.bit_length() - 1
                prefb, smb, lenb = sparse_table[span][l]
                mul = pow10[lenb]
                prefa, sma, lena = (prefa * mul + prefb) % MOD, (sma + smb) % MOD, lena + lenb
                span_size = pow(2, span)
                l += span_size
                diff -= span_size
            ans.append((prefa * sma) % MOD)
        return ans
