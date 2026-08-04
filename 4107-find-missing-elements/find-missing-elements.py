class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        x = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] != x:
                ans.append(x)
                i -= 1
            x += 1
            i += 1
        return ans
        
        