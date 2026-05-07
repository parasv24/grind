class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        cnt = 0
        prev = -1000000
        ans = 0
        while i < len(nums):
            if nums[i] == prev:
                cnt += 1
            else:
                cnt = 1
            
            if cnt <= 2:
                # print(i, j)
                nums[j] = nums[i]
                j +=1
                ans += 1
            prev = nums[i]
            i += 1
        return ans
        