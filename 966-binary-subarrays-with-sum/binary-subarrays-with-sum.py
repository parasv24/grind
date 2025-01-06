class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prev = 0
        ans = 0
        mp = {}
        mp[0] = 1
        for i in range(0,len(nums)):
            prev += nums[i]
            ans += mp.get(prev - goal,0)
            mp[prev] = mp.get(prev,0) + 1
        return ans
        