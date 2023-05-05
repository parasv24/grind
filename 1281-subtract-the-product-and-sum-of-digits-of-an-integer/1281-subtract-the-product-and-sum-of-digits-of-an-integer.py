class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        while n > 0 :
            nums.append(n % 10)
            n = n // 10
        # print(nums)
        return prod(nums) - sum(nums)
