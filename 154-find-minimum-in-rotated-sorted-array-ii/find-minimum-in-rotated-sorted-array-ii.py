class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            # print(lo, hi)
            mid = (lo + hi) // 2
            if nums[lo] < nums[hi]:
                return nums[lo]
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                lo += 1
                hi -= 1
        return nums[hi]