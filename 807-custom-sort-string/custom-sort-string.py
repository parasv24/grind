class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {}
        for el in s:
            mp[el] = mp.get(el, 0) + 1
        ans = ""
        for el in order:
            ans += mp.get(el, 0) * el
            mp[el] = 0
        for el in mp.keys():
            if mp[el] > 0:
                ans += mp.get(el, 0) * el
        return ans
        