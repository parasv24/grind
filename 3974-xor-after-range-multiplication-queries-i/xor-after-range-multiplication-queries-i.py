class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        for tup in queries:
            l, r, k, v = tup
            while l <= r:
                nums[l] = (nums[l] * v) % MOD
                l += k
        xor = 0
        for el in nums:
            xor = xor ^ el
        return xor

        