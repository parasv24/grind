class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        og_sum = n * (n + 1) // 2
        normal_sum = sum(nums)
        return og_sum - normal_sum
        