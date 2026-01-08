class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1.0:
            return x
        if x == -1.0:
            return 1.0 if n % 2 == 0 else -1.0
        def is_zero(x, eps=1e-6):
            return abs(x) < eps
        mp = {}
        power = abs(n)
        ans = 1
        while power > 0:
            if power & 1 == 1:
                ans *= x
                if is_zero(ans):
                    return ans
            x*= x
            power //=2
        return ans if n > 0 else 1/ans




        