class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # MOD = 10 ** 9 + 7
        # RADIX = 26

        # if len(needle) > len(haystack):
        #     return -1
        
        # n , m = len(haystack), len(needle)

        # MAX = 1
        # for _ in range(m - 1):
        #     MAX = (MAX * RADIX) % MOD

        # hash_ned, cur = 0, 0
        # for i in range(m):
        #     hash_ned = (hash_ned * RADIX + (ord(needle[i]) - ord("a"))) % MOD
        #     cur = (cur * RADIX + (ord(haystack[i]) - ord("a"))) % MOD
        
        # if cur == hash_ned:
        #     return 0

        # i, j = 0, m
        # while j < n:
        #     cur = (cur - (ord(haystack[i]) - ord("a")) * MAX) % MOD
        #     cur = (cur * RADIX) % MOD
        #     cur = (cur + (ord(haystack[j]) - ord("a"))) % MOD

        #     i += 1
        #     j += 1

        #     if cur == hash_ned:
        #         return i

        # return -1

        # KMP ALGO

        # if len(needle) > len(haystack):
        #     return -1
        # lps = [0]
        # new_str = needle + "#" + haystack
        # for i in range(1, len(new_str)):
        #     prev = lps[i-1]
        #     while prev > 0 and new_str[i] != new_str[prev]:
        #         prev = lps[prev-1]
        #     lps.append(prev + int(new_str[i] == new_str[prev]))
        #     if lps[i] == len(needle):
        #         return i - len(needle) - len(needle)
        # return -1

        if len(needle) > len(haystack):
            return -1
        
        lps = [0]
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[j] != needle[i]:
                j = lps[j-1]
            print(i, j)
            if needle[j] == needle[i]:
                j += 1
            lps.append(j)
        print(lps)
        j = 0
        for i in range(0, len(haystack)):
            print("inside", j, i)
            while j > 0 and needle[j] != haystack[i]:
                j = lps[j-1]
            
            if needle[j] == haystack[i]:
                j += 1
            
            if j == len(needle):
                return i - j + 1
        
        return -1