class Solution:
    def minOperations(self, nums: List[int]) -> int:
        is_right_rotated = True
        j = 0
        n = len(nums)
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                j += 1
            if j > 1 or (j >= 1 and nums[i] > nums[0]):
                is_right_rotated = False
                break
        
        if is_right_rotated:
            i = nums.index(0)
            return min(i, 2 + n - i)
        else:
            nums = nums[::-1]
            is_right_rotated = True
            j = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    j += 1
                if j > 1 or (j >= 1 and nums[i] > nums[0]):
                    is_right_rotated = False
                    break
            
            if is_right_rotated:
                i = nums.index(0)
                return min(i, n-i) + 1
            else:
                return -1
            


        
            