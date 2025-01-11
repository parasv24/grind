class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        left = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                left = mid
                hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if left == -1:
            return [-1, -1]
        right = -1
        lo = 0 
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                right = mid
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [left, right]

        