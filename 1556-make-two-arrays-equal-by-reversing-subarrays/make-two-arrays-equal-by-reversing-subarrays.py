class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        mp = [0] * 1001
        for el in target:
            mp[el] += 1
        for el in arr:
            mp[el] -= 1
            if mp[el] < 0:
                return False
        return True
        