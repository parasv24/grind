class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        mp = {}
        for el in arr1:
            s = ""
            for ch in str(el):
                s += ch
                mp[s] = s
        ans = 0
        for el in arr2:
            s = ""
            for ch in str(el):
                s += ch
                word = mp.get(s, "")
                ans = max(ans, len(word))
        return ans

        