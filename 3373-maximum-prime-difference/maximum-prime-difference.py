class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        mp = [True] * 101
        mp[0], mp[1] = False, False
        for i in range(2, 11):
            if mp[i]:
                for j in range(i * i, 101, i):
                    mp[j] = False
        i, j = 0, len(nums) - 1
        while i <= j:
            if mp[nums[i]] and mp[nums[j]]:
                return j - i
            if not mp[nums[i]]:
                i+=1
            if not mp[nums[j]]:
                j-=1

        