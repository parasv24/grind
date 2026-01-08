class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1.0:
            return x
        if x == -1.0:
            return 1.0 if n % 2 == 0 else -1.0
        if n < -1000000:
            return 0
        x = pow(x, abs(n))
        return x if n > 0 else 1/x
        