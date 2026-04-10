class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1
        idx = 0
        while l <= r:
            mid = (l+r) // 2
            print(l, r, mid)
            left = -5001
            right = 5001
            if mid > 0:
                left = nums[mid-1]
            if mid < len(nums) - 1:
                right = nums[mid + 1]
            
            if left > nums[mid] < right:
                idx = mid
                break
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[idx]

        