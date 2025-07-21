class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo , hi = 0 , len(nums) - 1
        ans = [-1, -1]
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    ans[0] = mid
                hi = mid - 1
            else:
                lo = mid + 1
        lo , hi = 0 , len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    ans[1] = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

        