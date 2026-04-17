class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        for ch in t:
            if ch not in mp:
                return False
            mp[ch] -= 1
            if mp[ch] == 0:
                mp.pop(ch)
        return len(mp.keys()) == 0
        