class Solution:
    def longestDupSubstring(self, s: str) -> str:
        MOD = 10 ** 9 + 7
        def is_ans(length):
            print(length)
            mul = pow(26, length -1 , MOD)
            i, j = 0, 0
            mp = defaultdict(list)
            hash_val = 0
            while j < len(s):
                hash_val = (hash_val * 26 + ord(s[j]) - ord("a")) % MOD
                if j - i == length - 1:
                    for idx in mp[hash_val]:
                        if s[i: i+length] == s[idx: idx+ length]:
                            return s[i:i+length]
                    mp[hash_val].append(i)
                    hash_val = (hash_val - (mul * (ord(s[i]) - ord("a")))) % MOD
                    i += 1
                j += 1
            return ""

        l, r = 1, len(s) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            string = is_ans(mid)
            if  string != "":
                l = mid + 1
                ans = string
            else:
                r = mid - 1
        return ans
