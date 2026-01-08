class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1.0:
            return x
        if x == -1.0:
            return 1.0 if n % 2 == 0 else -1.0
        if n < -1000000:
            return 0
        @cache
        def power(x, n):
            if n == 0:
                return 1
            if n & 1 == 0:
                return power(x, n//2) * power(x, n//2)
            else:
                return x * power(x, n//2) * power(x, n//2)
        return power(x, abs(n)) if n > 0 else 1/power(x,abs(n))
        