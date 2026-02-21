class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            n, mod = divmod(n, 2)
            if mod == 1:
                ans += 1
        return ans
        