class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            if lsum == sm - lsum - nums[i]:
                return i
            lsum += nums[i]
        return -1
        