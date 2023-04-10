class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            mx = max(curr_sum, mx)
        return mx