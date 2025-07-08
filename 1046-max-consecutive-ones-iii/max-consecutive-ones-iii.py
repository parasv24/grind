class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi, i , j, used = 0 , 0 , 0, 0
        while j < len(nums):
            if nums[j] == 1 or used < k:
                if nums[j] == 0 and used < k:
                    used += 1
                j += 1
            elif k > 0:
                maxi = max(maxi, j - i)
                while i < j and used >= k:
                    if nums[i] == 0:
                        used -= 1
                    i += 1
            else:
                maxi = max(maxi, j - i)
                i = j + 1
                j += 1
        maxi = max(maxi, j - i)
        return maxi 


                    