class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        cur_sum = 0
        ans = 0
        for i in range(0, len(nums)- 1):
            cur_sum += nums[i]
            if cur_sum >= total_sum - cur_sum:
                ans += 1
        return ans


        