class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        xor = 0
        for el in nums:
            xor = xor ^ el
        for tup in queries:
            l, r, k, v = tup
            while l <= r:
                xor = xor ^ nums[l]
                nums[l] = (nums[l] * v) % MOD
                xor = xor ^ nums[l]
                l += k
        return xor

        