class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cns, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max([cns, ans])
                cns = 0
            else:
                cns += 1
        return max([cns, ans])
        