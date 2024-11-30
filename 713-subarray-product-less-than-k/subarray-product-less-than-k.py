class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        win = 0
        sm = 1
        ans = 0
        while(end < len(nums)):
            if (nums[end]>=k or win < 0):
                win = 0
                sm = 1
                end += 1
                continue
            if sm * nums[end] < k :
                win += 1
                ans += win
                sm *= nums[end]
                end += 1
            else:
                win -= 1
                sm //= nums[start]
                start +=1
        return ans
        