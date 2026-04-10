class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low  , hi = 0, len(nums) - 1
        while low <= hi:
            mid = (low + hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                low = mid + 1
        return low