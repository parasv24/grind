class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prev = 0
        ans = 0
        mp = {}
        mp[0] = -1
        for i in range(0, len(nums)):
            el = nums[i]
            if nums[i] == 0:
                el = -1
            prev += el
            if mp.get(prev, -2)!= -2:
                ans = max(ans, i - mp[prev])
            if mp.get(prev, -2)==-2:
                mp[prev] = i
        return ans
        