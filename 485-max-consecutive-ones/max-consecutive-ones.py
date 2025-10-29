class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cns, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = ans if ans > cns else cns
                cns = 0
            else:
                cns += 1
        return ans if ans > cns else cns
        