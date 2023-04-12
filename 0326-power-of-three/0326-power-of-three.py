class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        val = (math.log10(n) / math.log10(3))
        return 3**int(val) == n
        