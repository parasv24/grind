class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mp = Counter(word)
        ans = 0
        for i in range(26):
            if mp[chr(ord('a') + i)] > 0 and mp[chr(ord('A') + i)] > 0:
                ans += 1
        return ans

        