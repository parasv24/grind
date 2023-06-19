class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi) // 2
            print(lo, hi, mid)
            if(nums[mid] == target):
                return mid
            elif (nums[mid] >= nums[lo]):
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid -1
                else:
                    lo = mid + 1
            else:
                if target <= nums[hi] and target > nums[mid] :
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
                
        