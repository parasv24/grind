class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, el in enumerate(nums):
            y = target - el
            if mp.get(y, -1) != -1:
                return [mp.get(y), idx]
            mp[el] = idx
        