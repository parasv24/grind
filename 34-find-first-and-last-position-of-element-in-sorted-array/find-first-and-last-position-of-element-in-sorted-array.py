class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        is_present = False
        low  , hi = 0, len(nums) - 1
        while low <= hi:
            mid = (low + hi) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    is_present = True
                low = mid + 1
            else:
                hi = mid - 1
        if not is_present:
            return ans
        ans[1] = hi

        low  , hi = 0, len(nums) - 1
        while low <= hi:
            mid = (low + hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                low = mid + 1
        ans[0] = low
        return ans
        