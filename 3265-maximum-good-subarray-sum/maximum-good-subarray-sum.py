class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        psums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            psums[i+1] = psums[i] + nums[i]
        mp = {}
        ans = -1e15
        for i in range(len(nums)):
            if k + nums[i] in mp:
                ans = max(ans, psums[i+1] - psums[mp[k + nums[i]]])
            if nums[i] - k in mp:
                ans = max(ans, psums[i+1] - psums[mp[nums[i] - k]])
            if nums[i] not in mp or psums[i] < psums[mp[nums[i]]]:
                        mp[nums[i]] = i
        
        return ans if ans != -1e15 else 0