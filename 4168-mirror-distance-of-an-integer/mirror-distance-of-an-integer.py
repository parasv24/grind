class Solution:
    def mirrorDistance(self, n: int) -> int:
        k = n
        rev = 0
        while k > 0:
            rev = rev * 10 + (k % 10)
            k = k // 10
        return abs(n - rev)

        