class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        lens = {0: -1}
        ans = 1000000
        rem = sum(nums) % p
        if rem == 0:
            return rem
        prev = 0
        for i in range(0, len(nums)):
            prev = (prev + nums[i])%p
            if lens.get((prev - rem)% p ,-2) != -2:
                ans = min(ans, i - lens[(prev - rem)%p])
            lens[prev] = i
        return ans if ans < len(nums) else -1

        