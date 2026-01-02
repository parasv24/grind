class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mp = {}
        for el in nums:
            if el in mp:
                return el
            mp[el] = 1
        