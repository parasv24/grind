class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mp = {}
        for el in arr:
            if mp.get(2*el, False) or (el % 2 == 0 and mp.get(el//2, False)):
                return True
            mp[el] = True
        return False
        