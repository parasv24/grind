class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            right = -10 ** 13
            left = -10 ** 13
            if mid > 0:
                left = nums[mid-1]
            if mid < len(nums) - 1:
                right = nums[mid+1]
            
            if  left < nums[mid] > right:
                return mid
            elif right > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l