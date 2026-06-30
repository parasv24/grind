class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i, j = 0, 0
        valid = 0
        counts = defaultdict(int)
        ans = 0
        while j < len(s):
            counts[s[j]] += 1
            if counts[s[j]] == 1:
                valid += 1
            if valid == 3:
                ans += len(s) - j
            while valid == 3:
                if counts[s[i]] == 1:
                    valid -= 1
                if valid == 3:
                    ans += len(s) - j
                counts[s[i]] -= 1
                i += 1
            j += 1
        return ans