class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums) - 2):
            if i != 0:
                if nums[i] == nums[i-1]:
                    continue
            first = nums[i]
            print(first)
            target = 0 - nums[i]
            mp = {}
            second = 1e9
            for j in range(i+1, len(nums)):
                y = target - nums[j]
                if mp.get(y, False) != False:
                    if nums[j] != second:
                        ans.append([first, nums[j], y])
                    second = nums[j]
                mp[nums[j]] = True
        return ans
            


