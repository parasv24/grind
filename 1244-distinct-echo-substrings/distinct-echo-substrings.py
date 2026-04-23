class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        
        MOD = 10**9 + 7
        BASE = 31
        
        prefix = [0] * (n + 1)
        power = [1] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = (prefix[i] * BASE + ord(text[i]) - ord('a')) % MOD
            power[i+1] = (power[i] * BASE) % MOD
        
        def get_hash(l, r):
            return (prefix[r] - prefix[l] * power[r-l]) % MOD
        
        seen = set()
        
        for length in range(1, n // 2 + 1):
            for i in range(n - 2 * length + 1):
                if get_hash(i, i+length) == get_hash(i+length, i+2*length):
                    seen.add(text[i: i+length])
        
        return len(seen)