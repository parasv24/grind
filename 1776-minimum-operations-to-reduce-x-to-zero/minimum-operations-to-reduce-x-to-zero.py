class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        k = sum(nums) - x
        if k == 0:
            return len(nums)
        lens = {}
        lens[0] = -1
        prev = 0
        ans = -2
        for i in range(0, len(nums)):
            prev += nums[i]
            if lens.get(prev-k, -2) >= -1:
                ans = max(ans, i - lens[prev - k])
            if lens.get(prev, 0) == 0:
                lens[prev] = i
        return len(nums) - ans if ans != -2 else -1
        