class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for el in nums:
            val = mp.get(el, 0)
            if val == 1:
                return True
            mp[el] = 1
        return False
        