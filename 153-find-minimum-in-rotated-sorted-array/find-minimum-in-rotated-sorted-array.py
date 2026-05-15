class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[0]



        