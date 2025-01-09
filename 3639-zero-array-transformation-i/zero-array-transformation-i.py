class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        line = [0] * (len(nums) + 2)
        for x, y in queries:
            line[x] -= 1
            line[y+1] += 1
        prev = 0
        for i in range(len(nums)):
            prev += line[i]
            if prev + nums[i] > 0:
                return False
        return True


        