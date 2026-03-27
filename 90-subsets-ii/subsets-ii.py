class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def rec(i, arr, taken):
            if i == len(nums):
                ans.append(arr)
                return
            rec(i+1, arr + [nums[i]], 1)
            if i > 0 and nums[i] == nums[i-1] and taken > 0:
                return
            rec(i+1, arr, 0)
        rec(0, [], 0)
        return ans
        