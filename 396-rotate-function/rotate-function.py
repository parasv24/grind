class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        init = 0
        sm = 0
        for idx , el in enumerate(nums):
            init += idx * el
            sm += el
        ans = init
        idx = len(nums) - 1
        # print(ans)
        while idx > 0:
            init -= (len(nums) * nums[idx])
            init += sm
            ans = max(ans, init)
            idx -= 1
        return ans