class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mp = Counter()
        for el in nums:
            mp[el] += 1
            if mp[el] == len(nums) // 2:
                return el
        