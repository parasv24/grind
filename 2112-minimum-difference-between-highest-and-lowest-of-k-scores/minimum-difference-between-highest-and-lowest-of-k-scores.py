class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        print(nums)
        k -= 1
        mini = 1000000000000
        for i in range(k, len(nums)):
            mini = min(mini, nums[i] - nums[i-k])
        return mini