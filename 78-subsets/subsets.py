class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(i):
            if i == len(nums):
                return [[]]
            small_ans = rec(i+1)
            new_ans = []
            for el in small_ans:
                new_ans.append(el)
                new_ans.append(el + [nums[i]])
            return new_ans
        return rec(0)
        