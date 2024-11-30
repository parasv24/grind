class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for el in strs:
            sorted_key = ''.join(sorted(el))
            if mp.get(sorted_key, False):
                mp[sorted_key].append(el)
            else:
                mp[sorted_key] = [el]
        return list(mp.values())
        