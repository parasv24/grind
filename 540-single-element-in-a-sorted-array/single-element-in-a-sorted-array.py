class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # approach 1 xor O(1)
        # xor = 0
        # for el in nums:
        #     xor ^= el
        # return xor

        # approach 2 logn B.S

        start , end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            prev = -1
            if mid -1 >= 0:
                prev = nums[mid-1]
            nxt = -1
            if mid + 1 <= len(nums) - 1:
                nxt = nums[mid+1]
            if prev == nums[mid]:
                if (len(nums) - 1 - mid) % 2 == 0:
                    end = mid - 2
                else:
                    start = mid + 1
            elif nums[mid] == nxt:
                if (len(nums) - mid) % 2 == 0:
                    end = mid - 1
                else:
                    start = mid + 2
            else:
                return nums[mid]

            
        