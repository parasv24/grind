class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        suffixes = [0] * len(nums)
        for i in range(0, len(nums)):
            if i > 0:
                prefixes[i] = nums[i] * prefixes[i-1]
                suffixes[len(nums) - i -1] = nums[len(nums) - i -1] * suffixes[len(nums) - i] 
            else:
                prefixes[i] = nums[i]
                suffixes[len(nums) - i -1] = nums[len(nums)-1]
        ans = []
        #print(prefixes, suffixes)
        for i in range(0, len(nums)):
            left , right = 1, 1
            if i > 0:
                left = prefixes[i-1]
            if i < len(nums) - 1:
                right = suffixes[i+1]
            ans.append(left*right)
        return ans
            

        