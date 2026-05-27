class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mp = {}
        ans = 0
        for idx, ch in enumerate(word):
            if "a" <= ch <= "z":
                mp[ch] = idx
            elif mp.get(ch, -1) == -1:
                mp[ch] = idx
        for i in range(26):
            idx = mp.get(chr(97+i), -1)
            caps_idx = mp.get(chr(65+i), -1)
            if  idx != -1 and caps_idx != -1 and caps_idx > idx:
                ans += 1
        return ans
        


        