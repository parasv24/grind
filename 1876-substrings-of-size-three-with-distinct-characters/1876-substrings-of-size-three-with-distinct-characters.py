class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        mp = {}
        i = j = 0
        count = 0
        while j < len(s):
            mp[s[j]] = mp.get(s[j], 0) + 1
            if j - i + 1 < k :
                j += 1
            elif j - i + 1 == k:
                if len(mp) == k:
                    count += 1
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    del mp[s[i]]
                i += 1
                j += 1
        return count

        